student = {
    "name": "Maya",
    "score": 80,
    "passed": True,
}
student["score"] = 65
student["passed"] = student["score"] >= 70
student["topic"] = "Python"
removed = student.pop("topic")
print("Removed:", removed)
print(student)
