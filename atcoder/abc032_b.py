s=input()
k=int(input())
n=set({})
for i in range(len(s)-k+1):
  n.add(s[i:i+k])
print(len(n))
