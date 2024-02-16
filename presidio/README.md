# How to Run

- Create recognizers using yaml_files as per your need.
- Make sure to include the absolute/relative path of the YAML files:
    ```bash
    registry.add_recognizers_from_yaml(<yaml_file_path>)
    ```

---

# FAQs

- If on running main python file, it mentions "No module named 'presidio analyzer'", then make sure to "module load python"
