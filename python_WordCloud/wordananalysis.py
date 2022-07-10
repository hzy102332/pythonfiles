import numpy as np
import matplotlib.pyplot as plt

#data processing
#Calculate the frequency of each word
infile = open('word.txt','r')
dic_word = {}
for line in infile.readlines():
    line = line.replace("\n","")
    if not line.isdigit() and line != "&" and line != "":
        if line in dic_word:
            dic_word[line] = dic_word[line] + 1
        else:
            dic_word[line] = 1

#Remove words that don't mean anything
del dic_word["and"]
del dic_word["in"]
del dic_word["for"]
del dic_word["the"]
del dic_word["The"]
del dic_word["to"]
del dic_word["Big"]
del dic_word["a"]
del dic_word["of"]
del dic_word['Marketing']

print(sorted(dic_word.items(), key = lambda kv:(kv[1], kv[0])))
items = np.array(sorted(dic_word.items(), key = lambda kv:(kv[1], kv[0])))
for item in items:
    print(item)

#draw the bar chart
plt.figure(figsize=(10,10))
for item in dic_word.keys():
    if dic_word[item] >= 5:
        plt.bar(item,dic_word[item],0.5,color = "Blue")

plt.xlabel("Frequency")
plt.ylabel("Word")
plt.xticks(rotation=60)
# plt.savefig("words.jpeg")
plt.show()
