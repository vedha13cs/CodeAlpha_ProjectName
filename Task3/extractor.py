import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "extracted_emails.txt"

try:
    # Read file
    with open(INPUT_FILE, "r") as file:
        content = file.read()

    # Extract emails using regex
    emails = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        content
    )

    # Remove duplicates
    unique_emails = sorted(set(emails))

    # Save emails
    with open(OUTPUT_FILE, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print("=" * 50)
    print("EMAIL EXTRACTION REPORT")
    print("=" * 50)

    print(f"Total Emails Found : {len(emails)}")
    print(f"Unique Emails      : {len(unique_emails)}")

    print("\nExtracted Emails:")
    for email in unique_emails:
        print(f"✓ {email}")

    print(f"\nReport saved to '{OUTPUT_FILE}'")

except FileNotFoundError:
    print("Input file not found!")
