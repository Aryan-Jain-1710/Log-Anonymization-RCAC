from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from typing import List
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult
from presidio_analyzer.predefined_recognizers import IpRecognizer
import argparse



# function for creating customized registries
def create_recognizer_registry():

    # all_registry = RecognizerRegistry() # intialize the registry
    # all_registry.load_predefined_recognizers() # Loads all the predefined recognizers (Credit card, phone number etc.)
    # ip_rec = all_registry.get_recognizers(language="en", entities="IP_ADDRESS") # get the ip address recognizer
    # # instantiate analyzer
    # # analyzer = AnalyzerEngine(registry=all_registry) # or your custom way of creating the analyzer engine
    # print(analyzer.get_recognizers(language='en')) # print list of all recognizers


    # User name
    # Names/last names
    # Email
    # Group names
    # Directory/file paths
    # IP addr
    # Hostname
    # Job ID
    # SSH Keys/secrets


    registry = RecognizerRegistry() # intialize the registry

    # Loads all the predefined recognizers (Credit card, phone number etc.)
    # registry.load_predefined_recognizers()  


    # adding the user recognizer (SUCCESS)
    registry.add_recognizers_from_yaml("yaml_files/user_recognizer.yaml")


    # adding email recognizer (SUCCESS)
    registry.add_recognizers_from_yaml("yaml_files/email_recognizer.yaml")


    # adding group names (check)
    registry.add_recognizers_from_yaml("yaml_files/groupnames_recognizer.yaml")


    # adding directory/ file paths
    registry.add_recognizers_from_yaml("yaml_files/dir_recognizer.yaml")


    # adding ip address (SUCCESS)
    ip_recog = IpRecognizer()
    registry.add_recognizer(ip_recog)  


    # adding hostname (check)


    # adding job id


    # adding ssh keys
    registry.add_recognizers_from_yaml("yaml_files/ssh_recognizer.yaml")


    # adding the xid and uid recognizer
    registry.add_recognizers_from_yaml("yaml_files/uid_xid_recognizers.yaml")  


    # returning the entire registry
    return registry  





def main():

    # get_group_names("/home/jain467/Desktop/Anonymization of Syslogs/MS-Presidio-RCAC-Implementation/user_list/groupnames.txt")

    parser = argparse.ArgumentParser(description="input output file names")

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

    print(analyzer.get_recognizers(language='en')) # print list of all recognizers

    results = analyzer.analyze(text=content, language="en") # run analyzer

    # output result message
    # with open("output.txt", 'w') as file:
    #         for item in results:
    #             file.write(str(item) + '\n')


    #intializing the engine
    anonymizer = AnonymizerEngine();

    #anonymized result
    an_output = anonymizer.anonymize(text=content, analyzer_results=results)

    # output anonymized message
    with open(output_file, 'w') as file:
        file.write(str(an_output))    
    




# run main()
main() 