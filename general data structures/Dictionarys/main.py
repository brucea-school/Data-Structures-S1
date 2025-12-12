print("Enter the name of a .txt file:")
intake = input()
# sampleText.txt
f = open(intake, "r")
t = f.read()
t = t.split()
print(t)
wordCount = {}

for i in t:
    if i in wordCount:
        wordCount[i] += 1
    else:
        wordCount[i] = 1

print(wordCount)

for i in wordCount:
    if wordCount[i] >= 2:
        print(i + ":" + str(wordCount[i]))



