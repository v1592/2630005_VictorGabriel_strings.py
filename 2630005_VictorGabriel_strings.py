# =============================================================================
# COVER PAGE
# =============================================================================
# Name:      VICTOR GABRIEL HERNANDEZ LUGO
# Student ID: 263005
# Topic:     Strings in Python
# GitHub:    https://github.com/<your-user>/<your-repo>   (replace with your URL)
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY
# =============================================================================
# A string (str) is Python's data type for text: an ordered sequence of
# characters. Strings are immutable, so any "change" (upper(), replace(),
# strip()...) creates a new string and leaves the original untouched.
# Basic operations include concatenation (+), repetition (*), length (len()),
# indexing (text[i]), slicing (text[a:b]), searching (in, find(), count()) and
# replacing (replace()). User text is often messy (extra spaces, mixed case),
# so it must be validated and normalized (strip(), lower()) before comparing
# or storing it. This document contains 6 problems: name formatter, email
# validator, palindrome checker, sentence word stats, password strength
# classifier and product label formatter. Each one documents its inputs,
# outputs, validations and 3 test cases (normal, border, error).

# =============================================================================
# PRINCIPLES AND GOOD PRACTICES
# =============================================================================
# - Strings are immutable: every change produces a new string.
# - Normalize input with strip() and lower() before comparing it.
# - Avoid "magic numbers" in indexes; document what each slice extracts.
# - Use built-in string methods instead of rewriting basic logic.
# - Validate in order: first "not empty", then the format.
# - Write readable code: clear variable names and understandable messages.

import math

# Constants (UPPER_SNAKE_CASE)
MIN_NAME_WORDS = 2
MIN_PALINDROME_LENGTH = 3
MIN_PASSWORD_LENGTH = 8
LABEL_LENGTH = 30
ERROR_MESSAGE = "Error: invalid input"


# =============================================================================
# Problem 1: Full name formatter (name + initials)
# =============================================================================
# Description: Receives a full name in one string, normalizes spaces and case,
#   and shows it in Title Case together with the initials (e.g. V.G.H.L.).
#
# Inputs:
# - full_name (string): may be upper/lower/mixed case with extra spaces.
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - Not empty after strip() (spaces-only strings are rejected).
# - At least two words (name and last name).
#
# Test cases:
# 1) Normal: "  victor gabriel HERNANDEZ LUGO " -> Formatted name:
#            Victor Gabriel Hernandez Lugo, Initials: V.G.H.L.
# 2) Border: "ana lopez" (exactly two words) -> Ana Lopez, A.L.
# 3) Error:  "     " or "madonna" -> Error: invalid input

def format_full_name(full_name):
    """Return (formatted_name, initials) or None if the input is invalid."""
    cleaned_name = full_name.strip()
    if cleaned_name == "":
        return None
    words = cleaned_name.split()  # split() with no args removes extra spaces
    if len(words) < MIN_NAME_WORDS:
        return None
    formatted_name = " ".join(words).title()
    initials = ""
    for word in formatted_name.split():
        initials += word[0] + "."  # word[0] = first letter of each word
    return formatted_name, initials


def run_problem_1(full_name):
    print(f'Input: "{full_name}"')
    result = format_full_name(full_name)
    if result is None:
        print(ERROR_MESSAGE)
    else:
        formatted_name, initials = result
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


# =============================================================================
# Problem 2: Simple email validator (structure + domain)
# =============================================================================
# Description: Checks a basic email format: exactly one '@', at least one '.'
#   after the '@', and no spaces. If valid, it also shows the domain.
#
# Inputs:
# - email_text (string).
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - Not empty after strip().
# - Exactly one '@' (count()).
# - No spaces inside the text.
# - Extra: something must exist before the '@'.
#
# Test cases:
# 1) Normal: "victor@example.com" -> Valid email: true, Domain: example.com
# 2) Border: "a@b.c" (shortest sensible email) -> true, Domain: b.c
# 3) Error:  "user@@mail.com", "user mail@x.com", "user@mail" -> false;
#            "   " -> Error: invalid input

def validate_email(email_text):
    """Return (is_valid, domain). domain is '' when the email is invalid."""
    cleaned_email = email_text.strip()
    if cleaned_email.count("@") != 1:
        return False, ""
    if " " in cleaned_email:
        return False, ""
    at_position = cleaned_email.find("@")
    if at_position == 0:  # nothing before '@'
        return False, ""
    domain_part = cleaned_email[at_position + 1:]  # everything after '@'
    if "." not in domain_part:
        return False, ""
    return True, domain_part


def run_problem_2(email_text):
    print(f'Input: "{email_text}"')
    if email_text.strip() == "":
        print(ERROR_MESSAGE)
        return
    is_valid, domain_part = validate_email(email_text)
    print(f"Valid email: {str(is_valid).lower()}")
    if is_valid:
        print(f"Domain: {domain_part}")


# =============================================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# =============================================================================
# Description: Determines whether a phrase reads the same forwards and
#   backwards, ignoring spaces and upper/lower case.
#
# Inputs:
# - phrase (string).
#
# Outputs:
# - "Normalized: <text>"
# - "Is palindrome: true" or "Is palindrome: false"
#
# Validations:
# - Not empty after strip().
# - At least 3 characters after removing spaces.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> normalized "anitalavalatina", true
# 2) Border: "Aba" (exactly 3 characters) -> true; "Hola mundo" -> false
# 3) Error:  "  " or "a b" (only 2 characters once cleaned) -> Error

def is_palindrome(phrase):
    """Return (normalized_text, result) or None if the input is invalid."""
    normalized_text = phrase.strip().lower().replace(" ", "")
    if phrase.strip() == "" or len(normalized_text) < MIN_PALINDROME_LENGTH:
        return None
    reversed_text = normalized_text[::-1]  # step -1 reverses the string
    return normalized_text, normalized_text == reversed_text


def run_problem_3(phrase):
    print(f'Input: "{phrase}"')
    result = is_palindrome(phrase)
    if result is None:
        print(ERROR_MESSAGE)
    else:
        normalized_text, answer = result
        print(f"Normalized: {normalized_text}")
        print(f"Is palindrome: {str(answer).lower()}")


# =============================================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# =============================================================================
# Description: Splits a sentence into words and reports the number of words,
#   the first and last word, and the shortest and longest word by length.
#
# Inputs:
# - sentence (string).
#
# Outputs:
# - "Word count: <n>", "First word: <...>", "Last word: <...>",
#   "Shortest word: <...>", "Longest word: <...>"
#
# Validations:
# - Not empty after strip().
# - At least one word after split().
#
# Test cases:
# 1) Normal: "  Python makes text processing easy  " -> 5 words, first
#            Python, last easy, shortest text (first of the 4-letter ties), longest processing
# 2) Border: "Hello" (single word) -> all four word fields are Hello, count 1
# 3) Error:  "     " -> Error: invalid input
# Note: on ties, the first word found wins.

def sentence_stats(sentence):
    """Return a dict with the stats or None if the input is invalid."""
    words = sentence.strip().split()
    if len(words) == 0:
        return None
    shortest_word = words[0]
    longest_word = words[0]
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word
    return {
        "count": len(words),
        "first": words[0],
        "last": words[-1],  # -1 = last element
        "shortest": shortest_word,
        "longest": longest_word,
    }


def run_problem_4(sentence):
    print(f'Input: "{sentence}"')
    stats = sentence_stats(sentence)
    if stats is None:
        print(ERROR_MESSAGE)
    else:
        print(f"Word count: {stats['count']}")
        print(f"First word: {stats['first']}")
        print(f"Last word: {stats['last']}")
        print(f"Shortest word: {stats['shortest']}")
        print(f"Longest word: {stats['longest']}")


# =============================================================================
# Problem 5: Password strength classifier
# =============================================================================
# Description: Classifies a password as weak, medium or strong.
# Rules (documented):
# - Weak:   length < 8, or length >= 8 but only one kind of character
#           (e.g. all lowercase letters).
# - Medium: length >= 8 and (has a digit OR has both upper and lower case),
#           but not all four kinds of characters.
# - Strong: length >= 8 and has uppercase, lowercase, digit and a symbol
#           (any character that is not a letter or a digit).
#
# Inputs:
# - password_input (string).
#
# Outputs:
# - "Password strength: weak" / "medium" / "strong"
#
# Validations:
# - Not empty (spaces-only is rejected too).
# - Length checked with len().
#
# Test cases:
# 1) Normal: "Abcdef1!" -> Password strength: strong
# 2) Border: "abcdefgh" (exactly 8, lowercase only) -> weak;
#            "Abcdefg1" (exactly 8, mixed + digit) -> medium
# 3) Error:  "" -> Error: invalid input

def classify_password(password_input):
    """Return 'weak', 'medium', 'strong' or None if the input is invalid."""
    if password_input.strip() == "":
        return None
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True
    if len(password_input) < MIN_PASSWORD_LENGTH:
        return "weak"
    if has_upper and has_lower and has_digit and has_symbol:
        return "strong"
    if has_digit or (has_upper and has_lower):
        return "medium"
    return "weak"


def run_problem_5(password_input):
    print(f'Input: "{password_input}"')
    strength = classify_password(password_input)
    if strength is None:
        print(ERROR_MESSAGE)
    else:
        print(f"Password strength: {strength}")


# =============================================================================
# Problem 6: Product label formatter (fixed-width text)
# =============================================================================
# Description: Builds the line "Product: <NAME> | Price: $<PRICE>" and forces
#   it to exactly 30 characters: shorter labels are padded with spaces on the
#   right, longer ones are cut with slicing.
#
# Inputs:
# - product_name (string).
# - price_value (string or number, must be a positive number).
#
# Outputs:
# - 'Label: "<exactly 30 characters>"' (quotes make the spaces visible)
#
# Validations:
# - product_name not empty after strip().
# - price_value convertible to a positive, finite number.
#
# Test cases:
# 1) Normal: "Pen", 2.5 -> "Product: Pen | Price: $2.50   "
# 2) Border: "Laptop", 2.5 -> label is exactly 30 characters already
#            (nothing to pad or cut); "Laptop", 15999.5 -> cut at 30
# 3) Error:  "Pen", -5 / "Pen", "abc" / "  ", 3 -> Error: invalid input

def build_label(product_name, price_value):
    """Return the 30-character label or None if the input is invalid."""
    cleaned_name = product_name.strip()
    if cleaned_name == "":
        return None
    try:
        price_number = float(price_value)
    except ValueError:
        return None
    if not math.isfinite(price_number) or price_number <= 0:
        return None
    base_label = f"Product: {cleaned_name} | Price: ${price_number:.2f}"
    base_label = base_label[:LABEL_LENGTH]  # cut if longer than 30
    return base_label.ljust(LABEL_LENGTH)   # pad with spaces if shorter


def run_problem_6(product_name, price_value):
    print(f'Input: "{product_name}", {price_value}')
    label = build_label(product_name, price_value)
    if label is None:
        print(ERROR_MESSAGE)
    else:
        print(f'Label: "{label}"')
        print(f"Length: {len(label)}")


# =============================================================================
# TEST RUNNER
# =============================================================================
def print_title(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def main():
    print_title("Problem 1: Full name formatter")
    run_problem_1("  victor gabriel HERNANDEZ LUGO ")   # normal
    run_problem_1("ana lopez")              # border
    run_problem_1("     ")                  # error

    print_title("Problem 2: Simple email validator")
    run_problem_2("victor@example.com")     # normal
    run_problem_2("a@b.c")                  # border
    run_problem_2("user@@mail.com")         # error (two '@')
    run_problem_2("   ")                    # error (empty)

    print_title("Problem 3: Palindrome checker")
    run_problem_3("Anita lava la tina")     # normal
    run_problem_3("Aba")                    # border
    run_problem_3("Hola mundo")             # not a palindrome
    run_problem_3("a b")                    # error (too short)

    print_title("Problem 4: Sentence word stats")
    run_problem_4("  Python makes text processing easy  ")  # normal
    run_problem_4("Hello")                  # border
    run_problem_4("     ")                  # error

    print_title("Problem 5: Password strength classifier")
    run_problem_5("Abcdef1!")               # normal (strong)
    run_problem_5("abcdefgh")               # border (weak)
    run_problem_5("Abcdefg1")               # border (medium)
    run_problem_5("")                       # error

    print_title("Problem 6: Product label formatter")
    run_problem_6("Pen", "2.5")             # normal
    run_problem_6("Laptop", 2.5)            # border (exactly 30)
    run_problem_6("Laptop", 15999.5)        # border (cut at 30)
    run_problem_6("Pen", -5)                # error (negative price)
    run_problem_6("Pen", "abc")             # error (not a number)


if __name__ == "__main__":
    main()


# =============================================================================
# CONCLUSIONS
# =============================================================================
# Handling strings is essential for reading and showing data, because almost
# everything a user types arrives as text. strip() and split() are useful to
# clean spaces and separate words, join() to rebuild text, and lower() or
# upper() whenever two texts must be compared. Normalizing text first avoids
# false differences such as "Hello" vs "hello " that would break a comparison.
# Clear validations (first not empty, then the format) prevent errors and
# garbage data from entering the program. I learned that strings are
# immutable, so every method returns a new string that must be stored in a
# variable, and that slices like text[::-1] or label[:30] solve problems in
# a single line.

# =============================================================================
# REFERENCES
# =============================================================================
# References:
# 1) Python documentation - Built-in Types: Text Sequence Type - str
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python documentation - String Methods
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Tutorial - Strings (section 3.1.3)
#    https://docs.python.org/3/tutorial/introduction.html#strings
# 4) PEP 8 - Style Guide for Python Code (naming conventions)
#    https://peps.python.org/pep-0008/
# 5) Real Python - Python Strings and Character Data
#    https://realpython.com/python-strings/
# 6) Sweigart, A. Automate the Boring Stuff with Python (Manipulating Strings)
