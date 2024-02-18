# Identification and Anonymization of System Logs

In this project, we implemented a framework in Python using Microsoft Presidio that allows the user to anonymize the system logs by creating various recognizers that are used for identifying sensitive information.

---

<br/>

## Framework Goals
- Identify the sensitive data in the system log
- Anonymize the sensitive data in the system log without loss of semantic

---

<br/>


## Implementation


### Project Structure:

- **presidio/main_implementation.py**: the main file of the framework that creates instances of all the YAML file recognizers and adds them to the recognizer registry to identify sensitive data and then adds a new operator class to anonymize the sensitive data without loss of semantics.
- **presidio/operator_typehash.py**: created a new operator class that can be added to the existing list of anonymizing operators and be used to anonymize the analyzed content.
- **presidio/yaml_files**: the directory contains all the YAML files that are used for recognizers.
- **presidio/config.yaml**: this YAML file contains the names of all the entity types for which the recognizers are implemented.

---

### Procedure:

1. Creating an instance of a recognizer registry that contains all the custom recognizers created.
2. Instantiating the analyzer that identifies all the sensitive data.
3. Reading the log file and calling on the analyzer to identify the sensitive data.
4. Instantiating the anonymizer and adding a new operator class for anonymization
5. Anonymizing the sensitive data recognized without loss of sensitive data by replacing with entity names and hashed value.

---
### Dependencies
- **presidio_analyzer**
- **typing import List**
- **presidio_anonymizer**
- **presidio_anonymizer.entities**
- **presidio_analyzer.predefined_recognizers**
- **argparse**
- **typing**
- **presidio_anonymizer.operators**
- **os**
- **yaml**

---
### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Aryan-Jain-1710/Log-Anonymization-RCAC.git
    cd Log-Anonymization-RCAC
    cd presidio
    ```

2. Install the required dependencies:

   ```
   Refer to the link:
   https://microsoft.github.io/presidio/installation/#using-pip
   ```


---
### How to Run

1. Run the main file:

    ```bash
    python Log-Anonymization-RCAC/presidio/main_implementation.py -i <input_sys_log_name> -o <output_file_name> -y <yaml_files_dir_name> -e <entity_yaml_file_name>
    ```

    Required flags:
    - -i: name of the input system log that need to be anonymized
    - -o: name of the output file that will store the anonymized system log
    - -y: name of the directory that contains all the YAML files which are used as recognizers
    - -e: YAML file that contains the name of all the entity types

---
### References

-  [https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples](https://microsoft.github.io/presidio/)
   - for Microsoft Presidio Usage
---
