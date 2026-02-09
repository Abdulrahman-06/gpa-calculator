LETTER_TO_PERCENT = {
    "A+": 97, "A": 93, "A-": 90,
    "B+": 87, "B": 83, "B-": 80,
    "C+": 77, "C": 73, "C-": 70,
    "D+": 67, "D": 63, "D-": 60,
    "F": 0
}

def grade_to_gpa(grade_percent: float) -> float:
    """Convert numeric percentage grade to 4.0 GPA scale."""
    if grade_percent >= 90:
        return 4.0
    elif grade_percent >= 80:
        return 3.0
    elif grade_percent >= 70:
        return 2.0
    elif grade_percent >= 60:
        return 1.0
    else:
        return 0.0

def parse_grade(input_str: str) -> float:
    """
    Parse user input for grade. Accepts:
    - numeric percentages (e.g. 92 or 92.5)
    - letter grades (e.g. A, B+, A-)
    Returns a numeric percentage (0-100).
    """
    s = input_str.strip().upper()
    if s in LETTER_TO_PERCENT:
        return float(LETTER_TO_PERCENT[s])

    try:
        val = float(s)
    except ValueError:
        raise ValueError(f"Unable to parse grade '{input_str}'")

    if not (0 <= val <= 100):
        raise ValueError("Grade percentage must be between 0 and 100")
    return val

def prompt_course() -> dict | None:
    name = input("Enter course name (or 'done' to finish): ").strip()
    if name.lower() == "done" or name == "":
        return None

    # Grade
    while True:
        grade_str = input("Enter grade (percent like 92.5 or letter like A-/B+): ").strip()
        try:
            percent = parse_grade(grade_str)
            break
        except ValueError as e:
            print(e)

    # Credits
    while True:
        credits_str = input("Enter credits (e.g. 3): ").strip()
        try:
            credits = float(credits_str)
            if credits <= 0:
                raise ValueError
            break
        except ValueError:
            print("Credits must be a positive number.")

    return {
        "name": name,
        "percent": percent,
        "gpa": grade_to_gpa(percent),
        "credits": credits
    }

def calculate_weighted_gpa(courses: list[dict]) -> float:
    total_points = 0.0
    total_credits = 0.0
    for c in courses:
        total_points += c["gpa"] * c["credits"]
        total_credits += c["credits"]
    return (total_points / total_credits) if total_credits > 0 else 0.0

def main():
    print("GPA Calculator (enter 'done' when finished)\n")

    courses: list[dict] = []
    while True:
        course = prompt_course()
        if course is None:
            break
        courses.append(course)
        print()

    if not courses:
        print("No courses entered.")
        return

    gpa = calculate_weighted_gpa(courses)

    print("\n--- Summary ---")
    for c in courses:
        print(f"{c['name']}: {c['percent']:.1f}% -> {c['gpa']:.1f} GPA  (credits: {c['credits']})")

    print(f"\nWeighted GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
