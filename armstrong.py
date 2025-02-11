def armstrong(num):
  string=str(num)
  power=len(string)
  sum_num=sum(int(i)**power for i in string)
  return sum_num==num

n=int(input())
if armstrong(n):
  print("Armstrong")
else:
  print("Not an Armstrong")
