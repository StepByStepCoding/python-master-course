# wrong threshold order
# INTENTIONAL LOGIC MISTAKE: 95 prints Pass because the first matching branch wins.
score = 95

if score >= 70:
    print("Pass")
elif score >= 90:
    print("Excellent")
else:
    print("Keep practicing")
