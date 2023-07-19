A=int(input())
B=int(input())
m = 1 << B
print(m)
if A & m:
    print("1")
else:
    print("0")
