models = ["A", "B", "C", "D", "E"]
models.insert(1, "X")
models.pop()
models.extend(["Y", "Z"])
models.remove("C")
models[0:2] = ["Q"]
print(models)
#["A", "X","B", "C", "D", "E"]
#["A", "X","B", "C", "D"]
#["A", "X","B", "C", "D","Y", "Z"]
#["A", "X","B",  "D","Y", "Z"]
#["Q","B",  "D","Y", "Z"]
#models.insert(1, "X")חשבתי שזה דורס את B