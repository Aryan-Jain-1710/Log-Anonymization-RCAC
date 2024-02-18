# How to Run

- Create recognizers using yaml_files as per your need and put all the YAML recognizers in one directory and mention the path of that directory in the `-y` flag when running the code.
    - For example, all the sample YAML recognizer files are in the `template_yaml_files` directory.
    - `template_yaml_files` directory contains multiple YAML files mentioning how to format them.
    - Learn more about how to create different recognizers
        - https://microsoft.github.io/presidio/analyzer/adding_recognizers/ 

-  Enter the names of all the entity types in the `config.yaml` file



---

# FAQs

- If on running main python file, it mentions "No module named 'presidio analyzer'", then make sure to "module load python"
