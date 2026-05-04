import re

# ===== question 1 =====
text = "Visit https://www.example.com or http://test.org for more info."
output = re.findall(r"https?://[^\s]+", text)
print(output)

# ===== question 2 =====
text = "Some color codes: #FF5733, #123, #1A2B3C, #XYZ123"
output = re.findall(r"#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})", text)
print(output)

# ===== question 3 =====
text = "Look at that cool book and the letter."
output = [
    x
    for x in re.findall(r"\w+", text)
    if re.search(r"(\w)\1", x)
]
print(output)

# ===== question 4 =====
text = 'She said "hello world" and then "goodbye".'
output = re.findall(r'"[^"]*"', text)
print(output)

# ===== question 5 =====
text = "Valid dates: 2023-12-01, 2024-02-30, 2023-00-10, 2023-11-31"

all_date = re.findall(r"(\d{4})-(0[1-9]|1[0-2])-([012][0-9]|3[01])", text)

def is_valid_date(date):
    year, month, day = map(int, date)
    
    if month in [4, 6, 9, 11] and day == 31:
        return False
    
    if month == 2: 
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return day <= (29 if is_leap else 28)
    
    return True

output = [
    f"{x[0]}-{x[1]}-{x[2]}"
    for x in all_date
    if is_valid_date(x)
]

print(output)

# ===== question 6 =====
text = "Anna saw a radar and met Hannah at noon."
output = [
    word
    for word in re.findall(r"[A-Za-z]{2,}", text)
    if word[0].lower() == word[-1].lower()
]
print(output)

# ===== question 7 =====
text = "<div>Hello <b>world</b>!</div>"
output = re.sub(r"<[^>]+>", "", text)
print(output)

# ===== question 8 =====
text = "This is is a test test of regex regex."
output = re.findall(r"\b(\w+) \1\b", text)
print(output)

# ===== question 9 =====
text = "Files: report.txt, data.csv, image.png, notes.log"
output = re.findall(r"\w+\.[A-Za-z]{3}", text)
print(output)

# ===== question 10 =====
text = "'user_1', '1user', 'user-name', 'valid_user123'"
output = re.findall(r"'([A-Za-z][A-Za-z0-9_]{4,14})", text)
print(output)