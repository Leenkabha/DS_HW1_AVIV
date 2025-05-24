import os
import argparse





class DSpotifyEmulator:
    def __init__(self):
        self.playlists = {}
        self.songs = {}

    def add_playlist(self, pid):
        if pid <= 0:
            return "INVALID_INPUT"
        if pid in self.playlists:
            return "FAILURE"
        self.playlists[pid] = set()
        return "SUCCESS"

    def delete_playlist(self, pid):
        if pid <= 0:
            return "INVALID_INPUT"
        if pid not in self.playlists:
            return "FAILURE"
        if self.playlists[pid]:  
            return "FAILURE"
        del self.playlists[pid]
        return "SUCCESS"

    def add_song(self, sid, plays):
        if sid <= 0 or plays < 0:
            return "INVALID_INPUT"
        if sid in self.songs:
            return "FAILURE"
        self.songs[sid] = plays
        return "SUCCESS"

    def add_to_playlist(self, pid, sid):
        if pid <= 0 or sid <= 0:
            return "INVALID_INPUT"
        if pid not in self.playlists or sid not in self.songs:
            return "FAILURE"
        if sid in self.playlists[pid]:
            return "FAILURE"
        self.playlists[pid].add(sid)
        return "SUCCESS"

    def delete_song(self, sid):
        if sid <= 0:
            return "INVALID_INPUT"
        if sid not in self.songs:
            return "FAILURE"
        for songset in self.playlists.values():
            if sid in songset:
                return "FAILURE"
        del self.songs[sid]
        return "SUCCESS"

    def remove_from_playlist(self, pid, sid):
        if pid <= 0 or sid <= 0:
            return "INVALID_INPUT"
        if pid not in self.playlists or sid not in self.playlists[pid]:
            return "FAILURE"
        self.playlists[pid].remove(sid)
        return "SUCCESS"

    def get_plays(self, sid):
        if sid <= 0:
            return "INVALID_INPUT"
        if sid not in self.songs:
            return "FAILURE"
        return f"SUCCESS, {self.songs[sid]}"

    def get_num_songs(self, pid):
        if pid <= 0:
            return "INVALID_INPUT"
        if pid not in self.playlists:
            return "FAILURE"
        return f"SUCCESS, {len(self.playlists[pid])}"

    def get_by_plays(self, pid, plays):
        if pid <= 0 or plays < 0:
            return "INVALID_INPUT"
        if pid not in self.playlists:
            return "FAILURE"
        exact = [sid for sid in self.playlists[pid] if self.songs.get(sid) == plays]
        if exact:
            return f"SUCCESS, {min(exact)}"
        greater = [(sid, self.songs[sid]) for sid in self.playlists[pid] if self.songs.get(sid, -1) > plays]
        if not greater:
            return "FAILURE"
        min_diff = min(greater, key=lambda x: (x[1] - plays, x[0]))
        return f"SUCCESS, {min_diff[0]}"

    def unite_playlists(self, pid1, pid2):
        # Check for invalid inputs (non-positive IDs or same IDs)
        if pid1 <= 0 or pid2 <= 0 or pid1 == pid2:
            return "INVALID_INPUT"

        # Check if both playlists exist
        if pid1 not in self.playlists or pid2 not in self.playlists:
            return "FAILURE"

        # Merge pid2 into pid1 (automatically handles duplicates if using sets)
        self.playlists[pid1].update(self.playlists[pid2])
        del self.playlists[pid2]  # Remove pid2 after merging
        return "SUCCESS"
def run_test_on_emulator(input_lines):
    emulator = DSpotifyEmulator()
    results = []
    for line in input_lines:
        parts = line.strip().split()
        if not parts:
            continue
        cmd = parts[0]
        try:
            args = list(map(int, parts[1:]))
        except:
            results.append(f"{cmd}: INVALID_INPUT")
            continue

        try:
            if cmd == "add_playlist" and len(args) == 1:
                res = emulator.add_playlist(*args)
            elif cmd == "delete_playlist" and len(args) == 1:
                res = emulator.delete_playlist(*args)
            elif cmd == "add_song" and len(args) == 2:
                res = emulator.add_song(*args)
            elif cmd == "delete_song" and len(args) == 1:
                res = emulator.delete_song(*args)
            elif cmd == "add_to_playlist" and len(args) == 2:
                res = emulator.add_to_playlist(*args)
            elif cmd == "remove_from_playlist" and len(args) == 2:
                res = emulator.remove_from_playlist(*args)
            elif cmd == "get_plays" and len(args) == 1:
                res = emulator.get_plays(*args)
            elif cmd == "get_num_songs" and len(args) == 1:
                res = emulator.get_num_songs(*args)
            elif cmd == "get_by_plays" and len(args) == 2:
                res = emulator.get_by_plays(*args)
            elif cmd == "unite_playlists" and len(args) == 2:
                res = emulator.unite_playlists(*args)
            else:
                res = "INVALID_INPUT"
        except:
            res = "INVALID_INPUT"

        results.append(f"{cmd}: {res}")
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for fname in os.listdir(args.input_dir):
        if not fname.endswith(".in"):
            continue
        with open(os.path.join(args.input_dir, fname)) as f:
            lines = f.readlines()
        output = run_test_on_emulator(lines)
        out_fname = fname.replace(".in", ".out")
        with open(os.path.join(args.output_dir, out_fname), "w") as fout:
            fout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()
