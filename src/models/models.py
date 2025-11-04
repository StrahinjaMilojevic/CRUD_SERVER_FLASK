import json
import os

DATA_FILE = "data.json"


def load_data():
    """Učitava podatke iz JSON fajla."""
    if not os.path.exists(DATA_FILE):
        return []  # Ako fajl ne postoji, vrati praznu listu

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """Čuva podatke u JSON fajl."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_all():
    """Vraća sve zapise iz baze."""
    return load_data()


def get_by_id(record_id):
    """Vraća zapis po ID-u."""
    data = load_data()
    for item in data:
        if item["id"] == record_id:
            return item
    return None


def create(record):
    """Kreira novi zapis i automatski dodeljuje ID."""
    data = load_data()

    # Automatski ID
    if data:
        record["id"] = max(item["id"] for item in data) + 1
    else:
        record["id"] = 1

    data.append(record)
    save_data(data)
    return record


def update(record_id, updated_record):
    """Ažurira zapis po ID-u."""
    data = load_data()

    for index, item in enumerate(data):
        if item["id"] == record_id:
            updated_record["id"] = record_id  # osiguravamo da ID ostane isti
            data[index] = updated_record
            save_data(data)
            return updated_record

    return None


def delete(record_id):
    """Briše zapis po ID-u."""
    data = load_data()

    for index, item in enumerate(data):
        if item["id"] == record_id:
            removed = data.pop(index)
            save_data(data)
            return removed

    return None
