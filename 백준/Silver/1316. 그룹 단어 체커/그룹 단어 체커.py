num = int(input())
group_word = num
for i in range(num):
  word = input()
  for j in range(len(word)-1):
    if word[j] ==  word[j+1]:
      pass
    elif word[j] in word[j+1:]:
      group_word -= 1 
      break

print(group_word)