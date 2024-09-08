
# Bicycle Generator

This project is a Python module that generates all possible bicycle modifications from an Excel file containing bicycle specifications. The generator outputs the modifications in JSON format, which can be used to track stock and specifications in a bicycle store.

## Features

- Reads an Excel file with multiple sheets of bicycle specifications.
- Generates all possible permutations of bicycle modifications based on provided designators.
- Outputs a JSON file listing all generated bicycle modifications with their specifications.

## File Structure

```
.
├── script.py               # Main script containing the bicycle generator logic
├── Bicycle.xlsx            # Input Excel file containing bicycle specifications
├── bicycle_output.json     # Output JSON file with all bicycle permutations
└── README.md               # This readme file
```

## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python 3.x
- pandas
- openpyxl

You can install the required dependencies by running:

```bash
pip install pandas openpyxl
```

## Excel File Format

The Excel file contains the following sheets:

1. **ID**: Contains designator names and values used to generate all possible bicycle IDs.
2. **GENERAL**: Contains fields that are common across all bicycle modifications.
3. **1 to 6**: Each of these sheets contains fields that are specific to certain designator values.

## How to Use

1. **Clone the repository** or download the script and the Excel file.
2. **Modify the Excel file** (`Bicycle.xlsx`) if necessary to suit your bicycle specifications.
3. **Run the script** to generate the JSON output:

```bash
python script.py
```
