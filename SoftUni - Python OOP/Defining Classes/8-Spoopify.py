class Song:
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return f"Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        filtered_songs = [song for song in self.songs if song.name == song_name]
        current_song = filtered_songs[0]
        if self.published:
            return f"Cannot remove songs. Album is published."
        elif current_song.name == song_name:
            self.songs.remove(current_song)
            return f"Removed song {song_name} from album {self.name}."
        elif song_name not in self.songs:
            return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        res = f"Album {self.name}\n"
        for song in self.songs:
            res += f"== {song.get_info()}\n"
        return res


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        filtered_albums = [al for al in self.albums if al.name == album_name]
        current_album = filtered_albums[0]
        if current_album.name == album_name and not current_album.published:
            self.albums.remove(current_album)
            return f"Album {album_name} has been removed."
        elif current_album.published:
            return f"Album has been published. It cannot be removed."
        elif current_album not in self.albums:
            return f"Album {album_name} is not found."

    @property
    def details(self):
        res = f"Band {self.name}\n"
        for al in self.albums:
            res += f"{al.details()}"
        return str(res)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details)
