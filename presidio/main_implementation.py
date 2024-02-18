from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from typing import List
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult
from presidio_analyzer.predefined_recognizers import IpRecognizer
import argparse
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig
import operator_typehash
import presidio_anonymizer.operators
import os
import yaml



# To generate list of users for yaml file
def add_dash_to_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        word_list = content.split()
        dashed_words = ['- {}'.format(word) for word in word_list]

    with open(filename, 'w') as file:
        file.write('\n'.join(dashed_words))




# To fetch group names
def get_group_names(filename):
    content = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('cn: x'):
                content.append('\n- ' + line.split('cn: x-', 1)[1].strip())

    with open("group_names_final", 'a') as file:
        file.writelines(content)




# function for creating customized registries
def create_recognizer_registry(yaml_dir):

    '''
    # intialize the registry
    all_registry = RecognizerRegistry()
    
    # Loads all the predefined recognizers (Credit card, phone number etc.)
    all_registry.load_predefined_recognizers()
    
    # get the ip address recognizer
    ip_rec = all_registry.get_recognizers(language="en", entities="IP_ADDRESS")

    # instantiate analyzer
    analyzer = AnalyzerEngine(registry=all_registry) # or your custom way of creating the analyzer engine
    
    # print list of all recognizers
    print(analyzer.get_recognizers(language='en'))
    
    '''

    # fetching all yaml files
    pwd = os.path.abspath(yaml_dir)
    files = [os.path.join(pwd, file) for file in os.listdir(pwd) if os.path.isfile(os.path.join(pwd, file)) and file.endswith('.yaml')]

    # intialize the registry
    registry = RecognizerRegistry() 

    # adding recognizres to the registry    
    for file in files:
        registry.add_recognizers_from_yaml(file)
    

    # adding ip address
    ip_recog = IpRecognizer()
    registry.add_recognizer(ip_recog)  


    # returning the entire registry
    return registry  





def main():

    # input output flags
    parser = argparse.ArgumentParser(description='Input Output Parser')
    parser.add_argument('-i', '--input', type=str, help='Input File path', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output File path', required=True)
    parser.add_argument('-y', '--yaml', type=str, help='Yaml Directory path', required=True)
    parser.add_argument('-e', '--entity', type=str, help='Entity Types Yaml File path', required=True)

    # creating parser
    args = parser.parse_args()

    # input file check
    input_file = args.input
    if not os.path.isfile(input_file): return 0

    # output file check
    output_file = args.output
    if not os.path.isfile(output_file): return 0
    
    # yaml dir check
    yaml_dir = args.yaml
    if not os.path.exists(yaml_dir): return 0
    
    # entity file check
    entity_file = args.entity
    if not os.path.isfile(entity_file): return 0


    # adding operators
    with open(entity_file, 'r') as file:
            yaml_data = yaml.safe_load(file)

    # changing yaml data into list type
    result_list = list(yaml_data)

    # creating operators dictionary
    ops = {}
    for item in result_list:
        ops["\""+item+"\""] = "OperatorConfig(\"typehash\",)"

    # instantiate registry
    registry = create_recognizer_registry(yaml_dir)

    # instantiate analyzer
    analyzer = AnalyzerEngine(registry=registry) # or your custom way of creating the analyzer engine

    # reading the input file - system log message
    with open(input_file, 'r') as file:
        content = file.read()

    # print list of all recognizers
    print("\nList of Recognizers:")
    print(analyzer.get_recognizers(language='en')) 

    # run analyzer
    results = analyzer.analyze(text=content, language="en") 

    # letting user know that sensitive info has been identified
    print("\n\nContent Analyzed...")

    # intializing the anonymizer engine
    anonymizer = AnonymizerEngine()

    # adding new operator TYPEHASH
    presidio_anonymizer.operators.__all__.append(operator_typehash)

    # anonymized result
    anonymized_output = anonymizer.anonymize(text=content, analyzer_results=results, operators=ops)

    # output anonymized message
    with open(output_file, 'w') as file:
        file.write(str(anonymized_output))    

    print("\n\nContent Anonymized and written to output file given by user...")



# run main()
main() 