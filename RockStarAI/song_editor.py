```python
class SongEditor:
    def __init__(self, user_data, game_data):
        self.user_data = user_data
        self.game_data = game_data
        self.custom_songs = user_data['custom_songs']

    def edit_song(self, song_id, new_song_data):
        for song in self.custom_songs:
            if song['id'] == song_id:
                song['data'] = new_song_data
                return "SongEditSuccess"
        return "SongNotFound"

    def create_song(self, song_data):
        new_song_id = len(self.custom_songs) + 1
        new_song = {
            'id': new_song_id,
            'data': song_data
        }
        self.custom_songs.append(new_song)
        return "SongCreateSuccess"

    def delete_song(self, song_id):
        for song in self.custom_songs:
            if song['id'] == song_id:
                self.custom_songs.remove(song)
                return "SongDeleteSuccess"
        return "SongNotFound"

    def get_song(self, song_id):
        for song in self.custom_songs:
            if song['id'] == song_id:
                return song
        return "SongNotFound"

    def list_songs(self):
        return self.custom_songs
```