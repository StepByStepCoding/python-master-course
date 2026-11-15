# Worked answer: Python lists
topics = ["Python basics", "Strings", "Numbers"]

topics.append("Lists")
topics[0] = "Python foundations"
removed = topics.pop()

print(topics)
print(len(topics))
print(f"Removed: {removed}")
