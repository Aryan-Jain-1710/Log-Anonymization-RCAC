# Identification and Anonymization of System Logs

In this project, we implemented a framework in Python using Microsoft Presidio that allows the user to anonymize the system logs by creating various recognizers that are used for identifying sensitive information.

---

<br/>

# Framework Goals
- Identify the sensitive data in the system log
- Anonymize the sensitive data in the system log without loss of semantic

---

<br/>


# Implementation


### Project Structure:

- **main_implementation.py**: the main file of the framework that creates instances of all the yaml file recognizers and uses them to generate an anonymized system log files.
- **operator_typehash.py**: created a new operator class that can be added to the existing list of anonymizing operators and be used to anonymize the analyzed content.
- **yaml_files/email_recognizer.yaml**: list of all emails that should be anonymized, the user must provide a list according to the template provided in the file.
- **yaml_files/user_recognizer.yaml**: list of all user names that should be anonymized, the user must provide a list according to the template provided in the file.
- **yaml_files/groupnames_recognizer.yaml**: list of all group names that should be anonymized, the user must provide a list according to the template provided in the file.

- **yaml_files/ssh_recognizer.yaml**: regex and context words to identify ssh keys in the logs.
- **yaml_files/dir_recognizer.yaml**: regex and context words to identify directory paths in the logs.
- **yaml_files/uid_xid_recognizer.yaml**: regex and context words to identify uid and xid in the logs.

---

### Procedure:

1. Creating an instance of a recognizer registry that contains all the custom recognizers created.
2. Instantiating the analyzer that identifies all the sensitive data.
3. Reading the log file and calling on the analyzer to identify the sensitive data.
4. Instantiating the anonymizer and using it to replace the sensitive data with sensitive data attribute name and hashed value.

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
    python Log-Anonymization-RCAC-share/presidio/main_implementation.py -i <input_sys_log_name> -o <output_file_name>
    ```


---
### References

-  [https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples](https://microsoft.github.io/presidio/)
   - for Microsoft Presidio Usage
---
