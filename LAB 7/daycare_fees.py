
import math


def parse_enrolment(text):
    if not isinstance(text, str):
        return None

    parts = text.split(':')
    if len(parts) != 2:
        return None

    age_group = parts[0].strip()
    hours_text = parts[1].strip()

    if not age_group or not hours_text:
        return None

    try:
        hours = float(hours_text)
    except (ValueError, TypeError):
        return None

    if not math.isfinite(hours):
        return None

    return age_group.title(), hours


def hours_average(hours_csv):
    if not isinstance(hours_csv, str):
        return None

    values = hours_csv.split(',')

    if not values or any(not v.strip() for v in values):
        return None

    try:
        numbers = [int(v.strip()) for v in values]
    except (ValueError, TypeError):
        return None

    return sum(numbers) // len(numbers)


def payable_fee(text):
    if not isinstance(text, str):
        return None

    parts = text.split('|')
    if len(parts) != 2:
        return None

    try:
        fee = float(parts[0].strip())
        discount = float(parts[1].strip())
    except (ValueError, TypeError):
        return None

    if not math.isfinite(fee) or not math.isfinite(discount):
        return None

    total = fee * 1.18 - discount

    if not math.isfinite(total):
        return None

    return max(total, 0)


def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    result = parse_enrolment(user_input)
    print("Age Group and Hours:", result)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    result = hours_average(user_input)
    print("Average Hours:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
