# CRUD Server (Flask + JSON Storage)

Ovaj projekat predstavlja jednostavan **CRUD API server** baziran na Flask framework-u.
Podaci se čuvaju u lokalnom JSON fajlu i server omogućava manipulaciju tim podacima kroz REST API.

---

## 🧠 Arhitektura sistema

Aplikacija je organizovana modularno po odgovornostima:

```
CRUD_SERVER_FLASK/
│
├── main.py                # Ulazna tačka aplikacije (pokreće server)
├── requirements.txt       # Python dependencije
├── README.md              # Dokumentacija sistema
└── src/
    ├── app.py             # Flask inicijalizacija + registracija ruta
    │
    ├── models/
    │   └── models.py      # Funkcije za rad sa JSON fajlom (load/save)
    │
    ├── routes/
    │   └── routes1.py     # Definicija CRUD API ruta (POST/GET/PUT/DELETE)
    │
    └── data/
        └── data.json      # JSON storage baza (isključeno iz Gita)
```

---

## 🔁 Tok podataka (kako sistem radi)

1. Korisnik pošalje HTTP zahtev ka API-ju (`POST`, `GET`, `PUT`, `DELETE`)
2. `routes1.py` prima zahtev → validira podatke → poziva `models.py`
3. `models.py`:
   - učitava postojeće podatke iz `data.json`
   - modifikuje ih u memoriji (lista/dict)
   - čuva nove vrednosti u `data.json`
4. API vraća HTTP odgovor u JSON formatu

**Primer toka (POST → CREATE item):**

```
[Klijent] → POST /items → [routes1.py] → [models.py] → data.json → odgovor klijentu
```

---

## 📦 Models (`models/models.py`)

Model je zadužen za rad sa skladištenjem podataka:

- `load_data()` — čita JSON fajl i vraća Python listu
- `save_data(data)` — upisuje Python listu nazad u JSON fajl
- API nikad ne zna gde se podaci nalaze → komunikacija ide isključivo kroz model

Ovaj pristup omogućava kasniji prelazak na bazu (npr. SQLite ili PostgreSQL) **bez menjanja ruta**.

---

## 🌐 API endpointi

| Metoda | Endpoint        | Opis operacije                     |
|--------|----------------|-------------------------------------|
| GET    | `/items`       | Vraća sve item-e                    |
| POST   | `/items`       | Kreira novi item                    |
| GET    | `/items/<id>`  | Vraća item po ID-u                  |
| PUT    | `/items/<id>`  | Ažurira postojeći item              |
| DELETE | `/items/<id>`  | Briše item                           |

**Primer JSON objekta u `data.json`:**

```json
[
  {
    "id": 1,
    "name": "Marko",
    "email": "marko@example.com"
  }
]
```

---

## 🚀 Pokretanje servera

```bash
python main.py
```

Server se pokreće na:

```
http://127.0.0.1:5000
```

---

## ❗ Napomena

📌 `data.json` je izbačen iz Git repozitorijuma jer predstavlja runtime storage.

```
.gitignore → src/data/data.json
```

---

## 📌 Cilj projekta

- Naučiti backend strukturu REST API-ja
- Primeniti modularizaciju projekta (routes / models / app)
- Kreirati server koji radi bez baze (JSON storage)

---

➡ Sistem je spreman za proširenje na pravu bazu (SQL).

