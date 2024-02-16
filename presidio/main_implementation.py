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
def create_recognizer_registry():

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




    # intialize the registry
    registry = RecognizerRegistry() 


    # adding the user recognizer
    registry.add_recognizers_from_yaml("private_yaml_files/user_recognizer.yaml")


    # adding email recognizer
    registry.add_recognizers_from_yaml("private_yaml_files/email_recognizer.yaml")


    # adding group names
    registry.add_recognizers_from_yaml("private_yaml_files/groupnames_recognizer.yaml")


    # adding directory/ file paths
    registry.add_recognizers_from_yaml("private_yaml_files/dir_recognizer.yaml")


    # adding ip address
    ip_recog = IpRecognizer()
    registry.add_recognizer(ip_recog)  


    # adding hostname (check)


    # adding job id
    registry.add_recognizers_from_yaml("private_yaml_files/job_id_recognizer.yaml")


    # adding ssh keys
    registry.add_recognizers_from_yaml("private_yaml_files/ssh_recognizer.yaml")


    # adding the xid and uid recognizer 
    registry.add_recognizers_from_yaml("private_yaml_files/uid_xid_recognizers.yaml")  


    # returning the entire registry
    return registry  





def main():


    # input output flags
    parser = argparse.ArgumentParser(description='Input Output Parser')
    parser.add_argument('-i', '--input', type=str, help='Input file path', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output file path', required=True)
    
    args = parser.parse_args()
    input_file = args.input
    output_file = args.output




    # instantiate registry
    registry = create_recognizer_registry()


    # instantiate analyzer
    analyzer = AnalyzerEngine(registry=registry) # or your custom way of creating the analyzer engine


    # reading the system log message
    with open(input_file, 'r') as file:
        content = file.read()


    # print list of all recognizers
    print(analyzer.get_recognizers(language='en')) 


    # run analyzer
    results = analyzer.analyze(text=content, language="en") 

 
    # intializing the anonymizer engine
    anonymizer = AnonymizerEngine()


    # adding new operator
    presidio_anonymizer.operators.__all__.append(operator_typehash)


    # anonymized result
    anonymized_output = anonymizer.anonymize(text=content, analyzer_results=results, 
                                     operators={ "XID": OperatorConfig("typehash",), "IP_ADDRESS": OperatorConfig("typehash",),  
                                                 "UID": OperatorConfig("typehash",), "DirPath Key": OperatorConfig("typehash",), 
                                                 "USERS": OperatorConfig("typehash",), "SSH Key": OperatorConfig("typehash",),  
                                                 "EMAILS": OperatorConfig("typehash",), "GROUP_NAMES": OperatorConfig("typehash",), 
                                                 "JOB_ID": OperatorConfig("typehash",),  })


    # output anonymized message
    with open(output_file, 'w') as file:
        file.write(str(anonymized_output))    



# run main()
main() 