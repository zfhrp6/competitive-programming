n = int(input())
mins = [(int(input()),idx) for idx in range(5)]
if min(mins)[0] > n:
    print(5)
else:
    ans = n // min(mins)[0] + 1 * ((n%(min(mins)[0]))>0)
    print(ans+4)
