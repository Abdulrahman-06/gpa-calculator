import sys

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
    Raises ValueError if parsing fails.
    """
    s = input_str.strip().upper()
    if s in LETTER_TO_PERCENT:
        return float(LETTER_TO_PERCENT[s])
    try: 
        val = float(s)
        if val > 100 or val < 0:
            raise ValueError("Grade percentage must be between 0 and 100")
        return val
    except ValueError:
        raise ValueError(f"Unable to parse grade '{input_str}'")
    
    def prompt_course() -> dict:
        name = input("Enter course name (or 'done' to finish): ").strip()
        if name.lower() == "done" or name.lower() == "":
            return None

