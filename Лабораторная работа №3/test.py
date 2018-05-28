A = int(input())
B = int(input())
C = int(input())

count = int((B-A)/C)
if (B-A) % C != 0:
    count += 1
if A % C == 0 or B % C == 0:
    count += 1
print(count)
