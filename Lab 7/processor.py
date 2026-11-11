import math


def parse_applicant(text):
    if not isinstance(text, str):
        return None

    try:
        parts = text.split(':')
        if len(parts) != 2:
            return None

        category, marks = parts
        category = category.strip()
        marks = float(marks.strip())

        if not category or not math.isfinite(marks):
            return None

        return category.title(), marks

    except (ValueError, TypeError):
        return None


def marks_average(marks_csv):
    if not isinstance(marks_csv, str):
        return None

    try:
        parts = marks_csv.split(',')
        if not parts or any(not part.strip() for part in parts):
            return None

        values = [int(part.strip()) for part in parts]
        return sum(values) // len(values)

    except (ValueError, TypeError):
        return None


def payable_award(text):
    if not isinstance(text, str):
        return None

    try:
        parts = text.split('|')
        if len(parts) != 2:
            return None

        award, deduction = parts
        award = float(award.strip())
        deduction = float(deduction.strip())

        if not math.isfinite(award) or not math.isfinite(deduction):
            return None

        total = award * 1.18 - deduction
        return max(total, 0)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_applicant ====")
    user_input = input("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    print("Category and Marks:", result)

    print("\n==== Running marks_average ====")
    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    print("Average Marks:", result)

    print("\n==== Running payable_award ====")
    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    print("Payable Award:", result)


if __name__ == "__main__":
    main()
