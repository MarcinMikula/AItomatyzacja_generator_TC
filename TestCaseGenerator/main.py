# main.py
import os
from TestCaseGenerator.test_generator.test_case_builder import TestCaseBuilder

def main():
    # Poprawiona ścieżka do pliku requirements.csv
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Katalog TestCaseGenerator
    requirements_file = os.path.join(base_dir, "sample_data", "requirements.csv")
    output_file = os.path.join(base_dir, "output", "test_cases.csv")

    # Inicjalizacja generatora przypadków testowych
    builder = TestCaseBuilder(requirements_file)

    # Generowanie przypadków testowych
    test_cases = builder.generate_test_cases()

    # Zapis do CSV
    builder.save_to_csv(test_cases, output_file)

if __name__ == "__main__":
    main()