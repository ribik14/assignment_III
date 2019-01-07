ffile=open("shakespeare.txt","r")
count = dict()
for line in ffile:
    for word in line.split():
        if len(word) < 2 and (word.lower() < 'a' or word.lower() > 'z'):
            continue
        count[word] = count.get(word, 0) + 1

number = 0
for x in count.keys():
    if len(x) == 3:
        number = number + count[x]
print("The total number of three lettered words is: ", number)


lar_word = sorted(count, key=count.get, reverse=True)[:20]
small_word = sorted(count, key=count.get, reverse=False)[:20]

print("The 20 most frequent words are: ", lar_word)
print("The 20 least frequent words are: ", small_word)
ffile.close()