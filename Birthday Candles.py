n = int(input())
l = []
k = 0
l = []

for i in range(0,n):
    l.append(float(input()))

for i in range(len(l)):
    if (l[i]>k):
        k = l[i]

c = 0

for j in range (len(l)):
    if l[j] == k:
        c = c+1

print(c)
