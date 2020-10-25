import csv
import glob
import json
from pathlib import Path

from main.base import LastPassRow


def getLastPassHeaders(lastpass_json_rows: []) -> []:
    return list(lastpass_json_rows[0].keys())


def getLastPassRows(enpass_rows_json_array) -> []:
    lastpass_rows = []
    for enpass_row_json in enpass_rows_json_array:
        lastpass_rows.append(LastPassRow.parse(enpass_row_json))

    return lastpass_rows


def getLastPassCSVRows(lastpass_json_rows) -> []:
    lastpass_csv_rows = []
    if len(lastpass_json_rows) > 0:
        lastpass_csv_rows.append(getLastPassHeaders(lastpass_json_rows))
    for lastpass_json_row in lastpass_json_rows:
        lastpass_csv_rows.append(list(lastpass_json_row.values()))

    return lastpass_csv_rows


def generateCSV(lastpass_csv_rows):
    script_location = Path(__file__).absolute().parent
    print(script_location)
    existing_export_files_len = len(glob.glob1(f"{script_location}/output", f"lastpass-*.csv"))
    with open(f'{script_location}/output/lastpass-{existing_export_files_len}.csv', 'w', newline='') as export_file:
        writer = csv.writer(export_file)
        writer.writerows(lastpass_csv_rows)
    print(f"find lastpass-{existing_export_files_len}.csv in output directory")


def generateLastPassCSV(file_path: str):
    enpass_json = json.load(open(file_path, 'r'))
    print(f"enpass json has {len(enpass_json['items'])} entries")

    enpass_rows_json_array = enpass_json['items']
    lastpass_json_rows = getLastPassRows(enpass_rows_json_array)

    lastpass_csv_rows = getLastPassCSVRows(lastpass_json_rows)

    generateCSV(lastpass_csv_rows)


if __name__ == '__main__':
    generateLastPassCSV("")
