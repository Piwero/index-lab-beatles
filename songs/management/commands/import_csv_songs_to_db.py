from django.core.management import BaseCommand

from songs.services import ParseCSVDataHandler


class Command(BaseCommand):
    help = "Imports CSV file data to database"

    def add_arguments(self, parser):
        parser.add_argument("path_file", type=str, help="The path to the CSV file")

    def handle(self, *args, **options):
        path = options["path_file"]
        csv_parser = ParseCSVDataHandler(path)
        parsed_data = csv_parser.parse()
        csv_parser.create_songs_from_parsed_data(parsed_data)

        self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
