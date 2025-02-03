str = input()

check_croatia = ["c=", "c-","dz=","d-","lj","nj","s=","z="]
count = 0 
for i in check_croatia:
  str = str.replace(i,"*")

print(len(str))