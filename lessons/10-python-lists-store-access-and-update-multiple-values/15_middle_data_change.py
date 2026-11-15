# middle data change
topics = ["Python basics", "Text", "Numbers"]

topics.append("Lists")
topics[0] = "Python foundations"
removed = topics.pop()

print(topics)
print(len(topics))
print(f"Removed: {removed}")
