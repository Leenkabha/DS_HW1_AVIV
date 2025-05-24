import os
import random

os.makedirs("dspotify_generated", exist_ok=True)

playlist_ids = [random.randint(1, 9999) for _ in range(100)]
song_ids = [random.randint(1, 999999) for _ in range(200)]
plays_values = [random.randint(1, 1000) for _ in range(200)]

commands = [
    "add_playlist", "delete_playlist", "add_song", "delete_song",
    "add_to_playlist", "remove_from_playlist", "get_plays",
    "get_num_songs", "get_by_plays", "unite_playlists"
]

for test in range(41, 100):
    with open(f'dspotify_generated/test{test}.in', 'w') as f:
        for _ in range(1000):  # up to 1000 commands per test
            cmd = random.choice(commands)
            pid1 = random.choice(playlist_ids)
            pid2 = random.choice(playlist_ids)
            sid1 = random.choice(song_ids)
            sid2 = random.choice(song_ids)
            plays = random.choice(plays_values)

            if cmd == "add_playlist":
                f.write(f"{cmd} {pid1}\n")
            elif cmd == "delete_playlist":
                f.write(f"{cmd} {pid1}\n")
            elif cmd == "add_song":
                f.write(f"{cmd} {sid1} {plays}\n")
            elif cmd == "delete_song":
                f.write(f"{cmd} {sid1}\n")
            elif cmd == "add_to_playlist":
                f.write(f"{cmd} {pid1} {sid1}\n")
            elif cmd == "remove_from_playlist":
                f.write(f"{cmd} {pid1} {sid1}\n")
            elif cmd == "get_plays":
                f.write(f"{cmd} {sid1}\n")
            elif cmd == "get_num_songs":
                f.write(f"{cmd} {pid1}\n")
            elif cmd == "get_by_plays":
                f.write(f"{cmd} {pid1} {plays}\n")
            elif cmd == "unite_playlists":
                f.write(f"{cmd} {pid1} {pid2}\n")
