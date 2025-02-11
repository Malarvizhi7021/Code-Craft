def ascii_values(s):
  letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  char=[]
  ascii=[]
  for i in s:
    if i in letters:
      char.append(i)
      ascii.append(ord(i))
  return char,ascii

name="@M$AL&A$R"
print(ascii_values(name))
