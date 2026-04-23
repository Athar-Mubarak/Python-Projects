#Email Slicer
import sys

print("--- Welcome to the Easy Email Slicer ---")
email = input("Please enter your email address: ").strip()
if '@' not in email:
    print("\nError: That doesn't look like a valid email (missing '@').")
else:
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]

    print("\n", "=" * 35)
    print(f"|Slicing Email: {email}")
    print("|" + '-' * 33)
    print(f"| Username:: {username}")
    print(f"| Domain:: {domain}")
    print("=" * 35)
