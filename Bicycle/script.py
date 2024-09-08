import pandas as pd
import itertools
import json


def load_designator_sheets(xls):
    designator_sheets = {}
    for sheet in xls.sheet_names[2:]:
        designator_sheets[sheet] = pd.read_excel(xls, sheet)
    return designator_sheets

def generate_ids(id_data):
    designator_values = [id_data[col].dropna().astype(str).tolist() for col in id_data.columns]
    return list(itertools.product(*designator_values))


def get_specific_fields(designator_sheets, designators, designator_mapping):
    specific_fields = {}
    for sheet_number, designator_name in designator_mapping.items():
        sheet_data = designator_sheets[sheet_number]
        if designator_name in designators:
            designator_value = designators[designator_name]
            matching_rows = sheet_data[sheet_data[designator_name] == designator_value]
            if not matching_rows.empty:
                matching_row = matching_rows.iloc[0, 1:]
                specific_fields.update(matching_row.to_dict())
    return specific_fields

def generate_bicycle_json(id_data, general_data, designator_sheets, designator_mapping):
    ids = generate_ids(id_data)
    result = []
    
    for id_tuple in ids:
        designators = dict(zip(id_data.columns, id_tuple))
        bicycle = {"ID": "-".join(id_tuple)}
        bicycle.update(general_data.iloc[0].to_dict())
        specific_fields = get_specific_fields(designator_sheets, designators, designator_mapping)
        bicycle.update(specific_fields)
        result.append(bicycle)
    
    return json.dumps(result, indent=4)

# Main function to load the Excel file and generate JSON
def bicycle_generator(file_path):
    xls = pd.ExcelFile(file_path)
   
    id_data = pd.read_excel(xls, 'ID')
    general_data = pd.read_excel(xls, 'GENERAL')
    designator_sheets = load_designator_sheets(xls)
    
   
    designator_mapping = {
        '1': 'Brakes',
        '2': 'Wheels',
        '3': 'Frame size',
        '4': 'Groupset',
        '5': 'Suspension',
        '6': 'Color'
    }
   
    return generate_bicycle_json(id_data, general_data, designator_sheets, designator_mapping)

# Example usage:
file_path = 'Bicycle.xlsx' 
bicycle_json = bicycle_generator(file_path)

with open('bicycle_output.json', 'w') as f:
    f.write(bicycle_json)

print("Bicycle JSON generated successfully.")
