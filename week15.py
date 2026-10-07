# regex week15

import re

"""text = "my phone number is 08012345678"
match = re.search(r"\d+", text)
print(match.group())   # 08012345678"""

# cheacking for digit in password

"""import re
has_digit = bool(re.search(r"\d", password))"""

# re.findall() — get every match, not just the first
"""text = "call me at 0801234567 or 0909876543"
numbers = re.findall(r"\d+", text)
print(numbers)   # ['0801234567', '0909876543']"""

# re.sub() — find and replace using a pattern
"""text = "my number is 0801234567"
censored = re.sub(r"\d", "*", text)
print(censored)   # my number is **********"""

# Groups — capturing specific parts of a match
# # text = "Dominion is 21 years old"
# match = re.search(r"(\w+) is (\d+) years old", text)
# print(match.group(1))   # Dominion
# print(match.group(2))   # 21
