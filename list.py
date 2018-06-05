list = [3, 5, 8, 6, 9, 12]
c = list[::2]
sum = 0
for i in c:
	sum = sum + i
a = len(list) - 1
print(sum * list[a])
