# 270. Extract emails using re
# Extract email addresses from text using regular expressions

import re

print("=== Basic Email Extraction ===")
# Simple email pattern
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

text = """
Contact us at support@example.com or sales@company.org
For inquiries, email john.doe@email.co.uk
Do not use test@invalid or user@domain
"""

print("Text:")
print(text)

print("\nExtracted emails:")
emails = re.findall(email_pattern, text)
for email in emails:
    print(f"  - {email}")

print("\n=== Email Search ===")
if re.search(email_pattern, "Contact: admin@website.com"):
    print("Email found!")

print("\n=== Email Validation ===")
def is_valid_email(email):
    """Check if email is valid"""
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return re.match(pattern, email) is not None

test_emails = [
    'user@example.com',
    'john.doe@company.co.uk',
    'invalid.email',
    'user@domain',
    'test123@test-site.com'
]

print("Email validation results:")
for email in test_emails:
    valid = is_valid_email(email)
    status = "Valid" if valid else "Invalid"
    print(f"  {email}: {status}")

print("\n=== Extract Email with Finditer ===")
text2 = "Email user1@domain.com or user2@site.org for help. Also try admin@test.net"

print("Text:", text2)
print("\nEmails with positions:")
for match in re.finditer(email_pattern, text2):
    print(f"  Found: {match.group()} at position {match.start()}-{match.end()}")

print("\n=== Extract Email Parts ===")
# Extract different parts of email
email_with_groups = r'([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+)\.([A-Za-z]{2,})'
email_text = "contact@example.com"

match = re.match(email_with_groups, email_text)
if match:
    print(f"Full email: {match.group(0)}")
    print(f"Username: {match.group(1)}")
    print(f"Domain: {match.group(2)}")
    print(f"TLD: {match.group(3)}")

print("\n=== Replace Emails ===")
original = "Contact support@company.com or info@company.com"
redacted = re.sub(email_pattern, '[EMAIL]', original)
print(f"Original: {original}")
print(f"Redacted: {redacted}")
