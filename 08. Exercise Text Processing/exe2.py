w = input().split()
sum = 0

word1 = w[0]
word2 = w[1]

if len(word1) > len(word2):
    for x in range(len(word1)):
        if x < len(word2):
            sum += ord(word1[x]) * ord(word2[x])
        else:
            sum += ord(word1[x])
else:
    for x in range(len(word2)):
        if x < len(word1):
            sum += ord(word1[x]) * ord(word2[x])
        else:
            sum += ord(word2[x])

print(sum)