str = input().upper()

strList = list(set(str))

wordList = []

for i in strList:
  count = str.count
  wordList.append(count(i))

if wordList.count(max(wordList)) > 1: 
  print("?")
else:
  print(strList[wordList.index(max(wordList))])