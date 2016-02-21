w=input()
n=int(input())
print(w[(n-1)//5]+w[n%5-1 if n%5 else 4])

