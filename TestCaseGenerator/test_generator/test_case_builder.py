import pandas as pd
from TestCaseGenerator.database.db_operations import add_test_case
from openai import OpenAI
from TestCaseGenerator.config import AI_API_KEY

class TestCaseBuilder:
    def __init__(self, requirements_file):
        self.requirements_file = requirements_file
        self.client = OpenAI(api_key=AI_API_KEY)  # Inicjalizacja klienta OpenAI

    def simulate_ai_response(self, description, test_type):
        # Tworzenie promptu dla OpenAI
        prompt = (
            f"Generate a test case for the following requirement: '{description}'. "
            f"The test case should be of type '{test_type}' (e.g., Positive, Negative, Boundary). "
            "Provide the following details in a structured format:\n"
            "- Prerequisites: What needs to be set up before the test.\n"
            "- Steps: Step-by-step instructions to perform the test.\n"
            "- End Conditions: Expected outcome after performing the test.\n"
            "Return the response in a clear, concise format."
        )

        try:
            # Wywołanie OpenAI API
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a software testing assistant specializing in generating test cases."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )

            # Pobranie wygenerowanej odpowiedzi
            generated_text = response.choices[0].message.content.strip()

            # Parsowanie odpowiedzi
            lines = generated_text.split("\n")
            prerequisites = "Brak"
            steps = "Brak"
            end_conditions = "Brak"

            for line in lines:
                if line.startswith("Prerequisites:"):
                    prerequisites = line.replace("Prerequisites:", "").strip()
                elif line.startswith("Steps:"):
                    steps = line.replace("Steps:", "").strip()
                elif line.startswith("End Conditions:"):
                    end_conditions = line.replace("End Conditions:", "").strip()

            return prerequisites, steps, end_conditions

        except Exception as e:
            print(f"Błąd podczas wywołania OpenAI API: {e}")
            return "Brak", "Brak", "Brak"

    def analyze_requirement(self, req_id, description):
        test_cases = []

        # Test pozytywny
        prerequisites, steps, end_conditions = self.simulate_ai_response(description, "Positive")
        test_cases.append({
            "requirement_id": req_id,
            "name": f"Test Pozytywny dla wymagania",
            "prerequisites": prerequisites,
            "steps": steps,
            "end_conditions": end_conditions,
            "test_type": "Pozytywny"
        })
        add_test_case(req_id, f"Test Pozytywny dla wymagania", prerequisites, steps, end_conditions, "Pozytywny")

        # Test negatywny
        prerequisites, steps, end_conditions = self.simulate_ai_response(description, "Negative")
        test_cases.append({
            "requirement_id": req_id,
            "name": f"Test Negatywny dla wymagania",
            "prerequisites": prerequisites,
            "steps": steps,
            "end_conditions": end_conditions,
            "test_type": "Negatywny"
        })
        add_test_case(req_id, f"Test Negatywny dla wymagania", prerequisites, steps, end_conditions, "Negatywny")

        # Test graniczny
        prerequisites, steps, end_conditions = self.simulate_ai_response(description, "Boundary")
        test_cases.append({
            "requirement_id": req_id,
            "name": f"Test Graniczny dla wymagania",
            "prerequisites": prerequisites,
            "steps": steps,
            "end_conditions": end_conditions,
            "test_type": "Graniczny"
        })
        add_test_case(req_id, f"Test Graniczny dla wymagania", prerequisites, steps, end_conditions, "Graniczny")

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