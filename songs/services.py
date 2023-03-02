import csv
from dataclasses import dataclass


@dataclass
class ParseCSVDataHandler:
    file_path: str

    def parse(self):
        data = []
        with open(self.file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append({header: row[header] for header in reader.fieldnames})
        return data
