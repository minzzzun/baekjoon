str = input()
str_list = list(str)
str_list.reverse()
r_str = "".join(str_list)

if str == r_str:
  print(1)
else:
  print(0)