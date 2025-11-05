# Web & API Test Automation Framework

Ovaj projekat je automatizovani framework za testiranje web aplikacija i API-ja.

## ✅ Korišćene tehnologije
- Python 3.10+
- Pytest
- Selenium WebDriver
- Requests (API testovi)
- Page Object Model (POM)
- ChromeDriver / GeckoDriver

---

## 📁 Struktura projekta

```
project/
│── tests/
│   ├── web/
│   │   └── test_login.py
│   ├── api/
│   │   └── test_users_api.py
│   └── data/
│       └── testdata.json
│
│── pages/
│   └── loginpage.py
│
│── logic/
│   └── models.py
│
│── conftest.py
│── requirements.txt
│── README.md
```

---

## ✅ Instalacija okruženja

### 1. Kloniranje projekta
```bash
git clone <git-repository-url>
cd project
```

### 2. Kreiranje virtualnog okruženja

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalacija dependencija
```bash
pip install -r requirements.txt
```

---

## ▶️ Pokretanje testova

Pokretanje svih testova:
```bash
pytest
```

Pokretanje samo web testova:
```bash
pytest tests/web -v
```

Pokretanje samo API testova:
```bash
pytest tests/api -v
```

Generisanje HTML izveštaja:
```bash
pytest --html=report.html
```

---

## 🔧 Podešavanje WebDriver-a

Preporučeno korišćenje webdriver-manager:

```python
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
```

Ako želiš manuelno preuzimanje drivera:
- ChromeDriver → https://chromedriver.chromium.org/downloads
- GeckoDriver → https://github.com/mozilla/geckodriver/releases

---

## 🧪 Primer — Page Object Model

**pages/loginpage.py**
```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(...).send_keys(username)
        self.driver.find_element(...).send_keys(password)
        self.driver.find_element(...).click()
```

---

## 🧪 Primer — API test

**tests/api/test_users_api.py**
```python
def test_get_users():
    response = requests.get("https://reqres.in/api/users?page=1")
    assert response.status_code == 200
```

---

## ✔️ Autor
Strahinja Milojevic 
QA Automation Engineer
