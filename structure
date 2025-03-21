TestCaseGenerator/
│
├── config.py                # Plik konfiguracyjny z danymi wrażliwymi (tokeny, maile, Jira URL itp.)
├── main.py                  # Główny plik uruchamiający automat
├── requirements.txt         # Lista zależności (np. pandas, requests, sqlalchemy)
│
├── api/
│   ├── ai_api.py            # Moduł integracji z API AI (np. do generowania kroków testowych)
│   └── jira_api.py          # Moduł integracji z JIRA (eksport przypadków testowych)
│
├── database/
│   ├── db_setup.py          # Skrypty do tworzenia bazy danych (tabele: wymagania, przypadki testowe itp.)
│   └── db_operations.py     # Operacje na bazie danych (CRUD dla wymagań i testów)
│
├── test_generator/
│   ├── test_case_builder.py # Logika generowania przypadków testowych na podstawie wymagań, architektury i ISTQB
│   └── test_types.py        # Definicje typów testów (funkcjonalne, integracyjne itp.)
│
├── tests/                   # Katalog z podkatalogami dla różnych typów testów
│   ├── functional/          # Testy funkcjonalne (np. dodanie kontaktu)
│   ├── integration/         # Testy integracyjne (np. synchronizacja z zewnętrznym API)
│   ├── performance/         # Testy wydajnościowe (np. czas odpowiedzi serwera)
│   ├── security/            # Testy bezpieczeństwa (np. walidacja uprawnień)
│   └── ui/                  # Testy interfejsu użytkownika (np. poprawność wyświetlania formularzy)
│
├── sample_data/
│   ├── requirements.csv     # Przykładowe wymagania w formacie CSV
│   └── architecture.md      # Opis architektury aplikacji (np. w Markdownie)
│
└── output/
    └── test_cases.csv       # Wygenerowane przypadki testowe w formacie CSV
