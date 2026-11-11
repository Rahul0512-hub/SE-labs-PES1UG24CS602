import math


def parse_application(text):
    """Parse visa type and entry count safely."""
    if not isinstance(text, str):
        return "Unknown", 0

    try:
        visa, entries = text.split(":", 1)
        visa = visa.strip()
        entries = int(entries.strip())

        if not visa or entries < 0:
            return "Unknown", 0

        return visa.title(), entries

    except (ValueError, TypeError):
        return "Unknown", 0


def processing_average(days_csv):
    """Calculate the average of valid processing-day values."""
    if not isinstance(days_csv, str):
        return 0

    values = []

    for value in days_csv.split(","):
        try:
            values.append(int(value.strip()))
        except (ValueError, TypeError):
            continue

    if not values:
        return 0

    return sum(values) // len(values)


def payable_fee(text):
    """Calculate payable fee safely."""
    if not isinstance(text, str):
        return 0.0

    try:
        fee, discount = text.split("|", 1)

        fee = float(fee.strip())
        discount = float(discount.strip())

        if not math.isfinite(fee) or not math.isfinite(discount):
            return 0.0

        total = fee * 1.18 - discount
        return max(total, 0.0)

    except (ValueError, TypeError):
        return 0.0


def main():
    print("==== Running parse_application ====")
    user_input = input("Enter visa type:entries (e.g. tourist:2): ")
    result = parse_application(user_input)
    print("Visa Type and Entries:", result)

    print("\n==== Running processing_average ====")
    user_input = input("Enter processing days as CSV (e.g. 5,10,21): ")
    result = processing_average(user_input)
    print("Average Processing Days:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 6000|500): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
