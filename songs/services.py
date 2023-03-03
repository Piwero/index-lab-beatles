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
                rank=song["Rank"] or None,
                year_release=song["Year Released"] or None,
                singer=song["Singer"],
                song_time=song["Song Time"],
                spotify_streams=song["Spotify Streams"],
                rolling_stone_rank=song[
                    "Rolling Stone 100 Greatest Beatles Songs Ranking"
                ] or None,
                NME_rank=song["NME Top 50 Beatles Songs Ranking"] or None,
                UG_views=song["UG Views"] or None,
                UG_favourites=song["UG Favourites"] or None,
            )
        return Song.objects.all()
