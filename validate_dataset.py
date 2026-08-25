import csv

FILE_NAME = "chemistry_questions_cv.csv"

REQUIRED_COLUMNS = [
    "Question",
    "Answer",
    "Topic",
    "Difficulty"
]

VALID_DIFFICULTIES = [
    "Beginner",
    "Intermediate",
    "Advanced"
]


def validate_dataset():
    errors = []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Check required columns
        for column in REQUIRED_COLUMNS:
            if column not in reader.fieldnames:
                errors.append(f"Missing column: {column}")

        # Stop if required columns are missing
        if errors:
            print("Dataset validation failed.")
            for error in errors:
                print("-", error)
            return

        # Check each record
        for row_number, row in enumerate(reader, start=2):

            for column in REQUIRED_COLUMNS:
                if not row[column].strip():
                    errors.append(
                        f"Row {row_number}: {column} is empty"
                    )

            if row["Difficulty"] not in VALID_DIFFICULTIES:
                errors.append(
                    f"Row {row_number}: Invalid difficulty level"
                )

    if errors:
        print("Dataset validation failed.")
        for error in errors:
            print("-", error)
    else:
        print("Dataset validation successful!")
        print("All required fields are present.")
        print("All records passed the basic quality checks.")


if __name__ == "__main__":
    validate_dataset()
