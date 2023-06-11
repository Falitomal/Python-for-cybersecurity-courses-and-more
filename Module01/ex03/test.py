from generator import generator


print("\nTest 1:\n Shuffled words:")
text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print("\nTest 2:\n Ordered words:")
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print("\nTest 3:\n Unique words:")
text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
print("\nTest 4:\n Error:")
text = 1.0
for word in generator(text, sep="."):
    print(word)