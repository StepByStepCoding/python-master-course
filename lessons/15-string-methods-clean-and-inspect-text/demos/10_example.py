raw = "     "
words = raw.split()
normalized = " ".join(words).lower()
print(normalized)
print(f"Words: {len(words)}")
print(normalized.startswith("python"))
