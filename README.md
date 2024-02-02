# Project Name: Data Enrichment

## Overview

This project enriches a given dataset by fetching additional information from an external API based on LEI (Legal Entity
Identifier) values.

## Requirements

- Python 3.9.6
- Pandas
- Requests

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/diegosreis/data_enrichment.git
    ```
   or
   ```bash
   git clone git@github.com:diegosreis/data_enrichment.git
   ```

2. Navigate to the project directory:

    ```bash
    cd data_enrichment
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script by providing the path to your CSV file and specifying the output mode (screen or file).

It is recommended to place the dataset inside the project's dataset folder, to avoid problems with read permission.

Example:

```bash
python main.py path/to/your/file.csv --output file
```

or

```bash
python main.py datasets/file.csv --output screen
```

### Arguments

- `file_path`: Path to the CSV file containing the dataset.
- `--output`: Display the result on the screen (`screen`) or save it to a file (`file`).

## Result

The enriched dataset will be displayed on the screen or saved to the `output` directory, depending on the specified
output directory.

## Notes

- If the file is not found or is empty, an error message will be displayed.
- The project uses a virtual environment for dependency management. Activate it before running the script.
- Ensure that Python 3.9 is installed on your system.

