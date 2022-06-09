
count = 0
word = " "
maxCount = 0
words = []

file = open("first problem.txt", "r")

for line in file:
    starting = line.lower().replace(',', '').replace('.', '').split(" ")
    for s in starting:
        words.append(s)

for i in range(0, len(words)):
    count = 1
    for j in range(i + 1, len(words)):
        if (words[i] == words[j]):
            count = count + 1

    if (count > maxCount):
        maxCount = count
        word = words[i]

print("word: " + word)
print(f"number of occurences: {maxCount}")
