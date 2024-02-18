# How to Run

- Create recognizers using yaml_files as per your need and put all the YAML recognizers in one directory and mention the path of that directory in the `-y` flag when running the code.
    - For example, all the sample YAML recognizer files are in the `template_yaml_files` directory.
    - `template_yaml_files` directory contains multiple YAML files mentioning how to format them.
    - The `template_yaml_files` contains the following files:
        - `yaml_files/email_recognizer.yaml`: list of all emails that should be anonymized, the user must provide a list according to the template provided in the file.
        - `yaml_files/user_recognizer.yaml`: list of all user names that should be anonymized, the user must provide a list according to the template provided in the file.
        - `yaml_files/groupnames_recognizer.yaml`: list of all group names that should be anonymized, the user must provide a list according to the template provided in the file.
        - `yaml_files/ssh_recognizer.yaml`: regex and context words to identify ssh keys in the logs.
        - `yaml_files/dir_recognizer.yaml`: regex and context words to identify directory paths in the logs.
        - `yaml_files/uid_xid_recognizer.yaml`: regex and context words to identify uid and xid in the logs.

    - Learn more about how to create different recognizers
        - https://microsoft.github.io/presidio/analyzer/adding_recognizers/ 

-  Enter the names of all the entity types in the `config.yaml` file



---

# FAQs

- If on running main python file, it mentions "No module named 'presidio analyzer'", then make sure to "module load python"
