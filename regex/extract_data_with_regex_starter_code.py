import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
#phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")

example = "The number is 123-456-7890."

result = phoneNumRegex.search(example)

if result:
    print("Phone number found:", result.group())
    print("Area code:", result.group()[0:3])