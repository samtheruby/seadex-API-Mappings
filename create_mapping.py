import json
import os

FILE_PATH = "mapping.json"

def load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"mappings": {}, "settings": {"fallback_to_seadex": True, "priority": "mapping_first"}}

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    data = load_json(FILE_PATH)

    mapping_key = input("Enter mapping key (e.g., attack on titan): ").strip().lower()
    anilist_id = int(input("Enter Anilist ID: ").strip())
    anime_name = input("Enter anime name: ").strip()
    anime_format = input("Enter anime format (e.g., TV, Movie): ").strip()

    also_search_raw = input("Enter search terms (comma separated): ").strip()
    also_search = [term.strip() for term in also_search_raw.split(",") if term.strip()]

    torrents = []
    while True:
        add_torrent = input("Add torrent? (y/n): ").strip().lower()
        if add_torrent != "y":
            break
        nyaa_id = int(input("Enter nyaa_id: ").strip())
        name = input("Enter torrent name: ").strip()
        torrents.append({"nyaa_id": nyaa_id, "name": name})

    data["mappings"][mapping_key] = {
        "anilist_id": anilist_id,
        "anime_name": anime_name,
        "anime_format": anime_format,
        "also_search": also_search,
        "torrents": torrents
    }

    save_json(FILE_PATH, data)
    print(f"Mapping '{mapping_key}' added successfully to {FILE_PATH}")

if __name__ == "__main__":
    main()
