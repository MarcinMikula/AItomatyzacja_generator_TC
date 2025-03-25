# TestCaseGenerator

## Opis projektu

`TestCaseGenerator` to AItomat napisany w Pythonie, który generuje przypadki testowe na podstawie wymagań, architektury aplikacji webowej (w tym przypadku CRM podobnego do Salesforce) oraz wytycznych ISTQB. Projekt ma na celu usprawnienie procesu tworzenia przypadków testowych w fazie testowania zgodnie z cyklem życia oprogramowania (SDLC) opisanym w ISTQB.

### Główne funkcjonalności:
- Generowanie przypadków testowych na podstawie wymagań zapisanych w pliku CSV.
- Przechowywanie wymagań i przypadków testowych w bazie danych SQLite.
- Eksport wygenerowanych przypadków testowych do pliku CSV.
- (Planowane) Integracja z API AI do generowania bardziej zaawansowanych kroków testowych.
- (Planowane) Eksport przypadków testowych do JIRA po przeglądzie przez testera.

Projekt jest modularny i podzielony na kilka kluczowych komponentów:
- `database/`: Obsługa bazy danych (tworzenie tabel, operacje CRUD).
- `test_generator/`: Logika generowania przypadków testowych.
- `api/`: Integracje z zewnętrznymi systemami (JIRA, AI API).
- `sample_data/`: Przykładowe dane (wymagania, architektura).
- `output/`: Wygenerowane przypadki testowe.

---

## Jak korzystać z projektu

Poniżej znajdziesz instrukcję krok po kroku, jak uruchomić projekt na swoim komputerze.

### Wymagania wstępne
1. Zainstalowany Python w wersji 3.8 lub nowszej.
2. Zainstalowany `pip` (menadżer pakietów Pythona).
3. Opcjonalnie: środowisko wirtualne (zalecane).

### Krok 1: Sklonuj repozytorium
Sklonuj projekt na swój komputer:
```bash
git clone <adres_repozytorium>
cd TestCaseGenerator
```
### Krok 2: Utwórz i aktywuj środowisko wirtualne (opcjonalne, ale zalecane)
Utwórz środowisko wirtualne, aby odizolować zależności projektu:
```bash
python -m venv venv
```

### Krok 3: Zainstaluj zależności
Zainstaluj wymagane biblioteki Pythona z pliku requirements.txt:
bash
```bash
pip install -r requirements.txt
```
### Krok 4: Skonfiguruj dane wrażliwe
Edytuj plik config.py, aby dodać swoje dane konfiguracyjne, takie jak:
URL serwera JIRA.

Token i email do JIRA.

Klucz API AI (jeśli używasz).

Ścieżka do bazy danych (domyślnie SQLite: sqlite:///testcase_db.sqlite).

Przykładowa zawartość config.py:
python
```bash
JIRA_SERVER = "https://twoja-instancja.atlassian.net"
JIRA_TOKEN = "twój_token"
JIRA_EMAIL = "twoj_email@example.com"
AI_API_KEY = "klucz_do_api_ai"
DB_CONNECTION_STRING = "sqlite:///testcase_db.sqlite"
```
### Krok 5: Przygotuj dane wejściowe
Upewnij się, że plik sample_data/requirements.csv zawiera wymagania, na podstawie których mają być generowane przypadki testowe. Przykładowa zawartość:
```bash
ID,Opis
1,Użytkownik może dodać nowy kontakt
2,System weryfikuje poprawność adresu email
```
### Krok 6: Utwórz bazę danych
Przed uruchomieniem głównego skryptu musisz utworzyć bazę danych SQLite i tabele (requirements oraz test_cases). Uruchom skrypt database/db_setup.py:
bash
```bash
cd C:\path\to\TC_Creator  # Zmień na odpowiednią ścieżkę
python -m TestCaseGenerator.database.db_setup
```
Po wykonaniu tego kroku zobaczysz komunikat: Baza danych i tabele zostały utworzone.. Baza danych testcase_db.sqlite zostanie utworzona w katalogu TestCaseGenerator.
Uwaga: Ten krok wykonaj tylko raz na początku projektu. Jeśli baza danych już istnieje i chcesz ją odświeżyć, usuń plik testcase_db.sqlite i uruchom powyższe polecenie ponownie.

### Krok 7: Wygeneruj przypadki testowe
Uruchom główny skrypt main.py, który:
Pobierze wymagania z pliku sample_data/requirements.csv.

Wygeneruje przypadki testowe.

Zapisze je do bazy danych.

Wyeksportuje je do pliku output/test_cases.csv.

Wykonaj:
```bash
cd C:\path\to\TC_Creator  # Zmień na odpowiednią ścieżkę
python -m TestCaseGenerator.main
```
### Krok 8: Sprawdź wyniki
Otwórz plik output/test_cases.csv, aby zobaczyć wygenerowane przypadki testowe.

Możesz również sprawdzić bazę danych testcase_db.sqlite (np. za pomocą narzędzia jak DB Browser for SQLite), aby zobaczyć zapisane dane.

