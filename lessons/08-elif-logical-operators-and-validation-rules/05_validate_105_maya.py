# validate (105, 'Maya')
name = "Maya"
score = 105

if name == "" or score < 0 or score > 100:
    print("Check the name and score.")
elif score >= 90:
    print("Excellent")
elif score >= 70:
    print("Pass")
else:
    print("Keep practicing")
