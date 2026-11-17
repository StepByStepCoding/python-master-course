nested = [[1], [2]]
shallow = nested.copy()
shallow[0].append(3)
print(nested)
print(shallow)
