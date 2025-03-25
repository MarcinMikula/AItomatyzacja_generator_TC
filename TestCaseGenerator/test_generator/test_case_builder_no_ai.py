# TestCaseGenerator/test_generator/test_case_builder_no_ai.py
import pandas as pd
from TestCaseGenerator.database.db_operations import add_test_case

class TestCaseBuilderNoAI:
    def __init__(self, requirements_file):
        self.requirements_file = requirements_file

    def simulate_ai_response(self, description, test_type):
        """
        Symuluje odpowiedź AI na podstawie typu testu i opisu wymagania.
        Wersja bez integracji z OpenAI.
        """
        if "dodaj nowy kontakt" in description.lower():
            if test_type == "Pozytywny":
                return {
                    "name": "Dodanie kontaktu z poprawnymi danymi",
                    "prerequisites": "Użytkownik jest zalogowany i ma uprawnienia do dodawania kontaktów.",
                    "steps": "1. Przejdź do sekcji 'Kontakty'.\n2. Kliknij 'Dodaj nowy kontakt'.\n3. Wypełnij pola: Imię='Jan', Nazwisko='Kowalski', Email='jan.kowalski@example.com'.\n4. Kliknij 'Zapisz'.",
                    "end_conditions": "Kontakt jest widoczny na liście kontaktów."
                }
            elif test_type == "Negatywny":
                return {
                    "name": "Próba dodania kontaktu bez wymaganych pól",
                    "prerequisites": "Użytkownik jest zalogowany i ma uprawnienia do dodawania kontaktów.",
                    "steps": "1. Przejdź do sekcji 'Kontakty'.\n2. Kliknij 'Dodaj nowy kontakt'.\n3. Pozostaw pole 'Email' puste.\n4. Kliknij 'Zapisz'.",
                    "end_conditions": "System wyświetla komunikat o błędzie: 'Pole Email jest wymagane'."
                }
            elif test_type == "Graniczny":
                return {
                    "name": "Dodanie kontaktu z maksymalną długością imienia",
                    "prerequisites": "Użytkownik jest zalogowany i ma uprawnienia do dodawania kontaktów.",
                    "steps": "1. Przejdź do sekcji 'Kontakty'.\n2. Kliknij 'Dodaj nowy kontakt'.\n3. Wypełnij pole Imię ciągiem 255 znaków (np. 'A' x 255), Nazwisko='Kowalski', Email='jan.kowalski@example.com'.\n4. Kliknij 'Zapisz'.",
                    "end_conditions": "Kontakt jest widoczny na liście kontaktów lub system wyświetla komunikat o błędzie, jeśli limit został przekroczony."
                }

        elif "weryfikuje poprawność adresu email" in description.lower():
            if test_type == "Pozytywny":
                return {
                    "name": "Wprowadzenie poprawnego adresu email",
                    "prerequisites": "Użytkownik jest zalogowany i edytuje dane kontaktu.",
                    "steps": "1. Przejdź do sekcji 'Kontakty'.\n2. Wybierz kontakt do edycji.\n3. Wprowadź email: 'user@example.com'.\n4. Kliknij 'Zapisz'.",
                    "end_conditions": "Dane kontaktu są zapisane, email jest poprawny."
                }
            elif test_type == "Negatywny":
                return {
                    "name": "Wprowadzenie niepoprawnego adresu email",
                    "prerequisites": "Użytkownik jest zalogowany i edytuje dane kontaktu.",
                    "steps": "1. Przejdź do sekcji 'Kontakty'.\n2. Wybierz kontakt do edycji.\n3. Wprowadź email: 'user@'.\n4. Kliknij 'Zapisz'.",
                    "end_conditions": "System wyświetla komunikat o błędzie: 'Niepoprawny format adresu email'."
                }
            elif test_type == "Graniczny":
                return {
                    "name": "Wprowadzenie adresu email o maksymalnej długości",
                    "prerequisites": "Użytkownik jest zalogowany i edytuje dane kontaktu.",
                    "steps": "1. Przejdź do sekcji 'Kontakty'.\n2. Wybierz kontakt do edycji.\n3. Wprowadź email o długości 320 znaków (np. 'a' x 253 + '@example.com').\n4. Kliknij 'Zapisz'.",
                    "end_conditions": "Dane kontaktu są zapisane lub system wyświetla komunikat o błędzie, jeśli limit został przekroczony."
                }

        return {
            "name": f"Test {test_type} dla wymagania",
            "prerequisites": "Brak",
            "steps": "Brak",
            "end_conditions": "Brak"
        }

    def analyze_requirement(self, req_id, description):
        test_cases = []

        # Test pozytywny
        response = self.simulate_ai_response(description, "Pozytywny")
        test_cases.append({
            "requirement_id": req_id,
            "name": response["name"],
            "prerequisites": response["prerequisites"],
            "steps": response["steps"],
            "end_conditions": response["end_conditions"],
            "test_type": "Pozytywny"
        })
        add_test_case(req_id, response["name"], response["prerequisites"], response["steps"], response["end_conditions"], "Pozytywny")

        # Test negatywny
        response = self.simulate_ai_response(description, "Negatywny")
        test_cases.append({
            "requirement_id": req_id,
            "name": response["name"],
            "prerequisites": response["prerequisites"],
            "steps": response["steps"],
            "end_conditions": response["end_conditions"],
            "test_type": "Negatywny"
        })
        add_test_case(req_id, response["name"], response["prerequisites"], response["steps"], response["end_conditions"], "Negatywny")

        # Test graniczny
        response = self.simulate_ai_response(description, "Graniczny")
        test_cases.append({
            "requirement_id": req_id,
            "name": response["name"],
            "prerequisites": response["prerequisites"],
            "steps": response["steps"],
            "end_conditions": response["end_conditions"],
            "test_type": "Graniczny"
        })
        add_test_case(req_id, response["name"], response["prerequisites"], response["steps"], response["end_conditions"], "Graniczny")

        return test_cases

    def generate_test_cases(self):
        try:
            requirements = pd.read_csv(self.requirements_file)
        except FileNotFoundError:
            print(f"Plik {self.requirements_file} nie został znaleziony.")
            return []

        test_cases = []
        for _, row in requirements.iterrows():
            req_id = row["ID"]
            description = row["Opis"]
            test_cases.extend(self.analyze_requirement(req_id, description))

        return test_cases

    def save_to_csv(self, test_cases, output_file):
        if not test_cases:
            print("Brak przypadków testowych do zapisania.")
            return

        df = pd.DataFrame(test_cases)
        df.to_csv(output_file, index=False)
        print(f"Przypadki testowe zapisane do {output_file}")