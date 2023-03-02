import csv
from dataclasses import dataclass

from songs.models import Song


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

    def create_songs_from_parsed_data(self, parsed_data):
        for song in parsed_data:
            Song.objects.create(
                name=song["Song Name"],
                album=song["Album"],
                writer=song["Song Writer"],
                rank=song["Rank"],
                year_release=song["Year Released"],
                singer=song["Singer"],
                song_time=song["Song Time"],
                spotify_streams=song["Spotify Streams"],
                rolling_stone_rank=song[
                    "Rolling Stone 100 Greatest Beatles Songs Ranking"
                ],
                NME_rank=song["NME Top 50 Beatles Songs Ranking"],
                UG_views=song["UG Views"],
                UG_favourites=song["UG Favourites"],
            )
        return Song.objects.all()
