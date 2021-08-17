import os
import json
import dataclasses
from google.cloud import bigquery


@dataclasses.dataclass
class Font_Data:
    font_id: str
    language: str
    name: str
    version: str
    preferences: str
    main: str
    about: str
    start: str


credentials_path = 'Resource/bigquery_private_key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'ability-stone-simulator.resource.font_table'

row = [{
    "font_id": "FP01",
    "language": "English",
    "name": "English Font Pack",
    "version": "1.0.0.0",
    "main": {
        "AccentButton": "Poppins, 14, bold",
        "ToggleButton": "Poppins, 9",
        "Switch": "Poppins, 12",
        "TCheckbutton": "Poppins, 11",
        "TCombobox": "Noto Sans CJK KR Medium (TTF), 12",
        "menu": "Poppins, 12",
        "user_id_label": "Poppins, 12",
        "start_label": "Poppins, 16, bold",
        "microphone_label": "Poppins, 16",
        "input_device_combo": "Noto Sans CJK KR Medium (TTF), 12",
        "speaker_label": "Poppins, 16",
        "output_device_combo": "Noto Sans CJK KR Medium (TTF), 12",
        "license_message": "Poppins, 13",
        "toggle_button": {
            "left_button": "Poppins, 9, bold",
            "right_button": "Poppins, 9, bold"
        }
    },
    "preferences": {
        "title_label": "Poppins, 16, bold",
        "language_label": "Poppins, 14, bold",
        "language_combo": "Noto Sans CJK KR Medium (TTF), 12",
        "advanced_label": "Poppins, 14, bold",
        "notice_label": "Poppins, 10"
    },
    "about": {
        "software_name_label": "Poppins, 16, bold",
        "version_label": "Poppins, 10",
        "build_label": "Poppins, 10",
        "contents_message": "Poppins, 10",
        "copyrights_label": "Poppins, 10"
    },
    "start": {
        "content_message": "Poppins, 10",
        "start_button": "Poppins, 12, bold"
    }
}]

errors = client.insert_rows_json(table_id, font_data)
if not errors:
    print('New rows have been added.')
else:
    print(f'Encountered errors while inserting rows: {errors}')
