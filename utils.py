import json


def save_data_as_json_file(file_name, payload):
    with open(f'{file_name}.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(payload, ensure_ascii=False, indent=4))
