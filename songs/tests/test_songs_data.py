from songs.models import Song


class TestSongsData:
    def test_song_can_store_name(self):
        song = Song(name="Test Song")
        
        assert song.name == "Test Song"

    def test_song_can_store_album(self):
        song = Song(album="Test Album")

        assert song.album == "Test Album"

    def test_song_can_store_writer(self):
        song = Song(writer="Test Writer")

        assert song.writer == "Test Writer"

    def test_song_can_store_rank(self):
        song = Song(rank=1)

        assert song.rank == 1

    def test_song_can_store_year_release(self):
        song = Song(year_release=2023)

        assert song.year_release == 2023

    def test_song_can_store_singer(self):
        song = Song(singer="Test Singer")

        assert song.singer == "Test Singer"

    def test_song_can_store_song_time(self):
        song = Song(song_time="02:32")

        assert song.song_time == "02:32"

    def test_song_can_store_spotify_streams(self):
        song = Song(spotify_streams=100000)

        assert song.spotify_streams == 100000

    def test_song_can_store_rolling_stone_rank(self):
        song = Song(rolling_stone_rank=1)

        assert song.rolling_stone_rank == 1

    def test_song_can_store_NME_rank(self):
        song = Song(NME_rank=1)

        assert song.NME_rank == 1

    def test_song_can_store_UG_views(self):
        song = Song(UG_views=100000)

        assert song.UG_views == 100000

    def test_song_can_store_UG_favourites(self):
        song = Song(UG_favourites=100000)

        assert song.UG_favourites == 100000

