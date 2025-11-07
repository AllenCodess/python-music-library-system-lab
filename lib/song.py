# lib/song.py

class Song:
    # Class attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        """Increment the total number of songs."""
        Song.count += 1

    def add_to_genres(self):
        """Add the genre to the set of all genres."""
        Song.genres.add(self.genre)

    def add_to_artists(self):
        """Add the artist to the set of all artists."""
        Song.artists.add(self.artist)

    def add_to_genre_count(self):
        """Update the genre count dictionary."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Update the artist count dictionary."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
