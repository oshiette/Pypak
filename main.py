n = int(input('Введите длину ряда: '))
f1 = f2 = 1

i = 2
while i < n:
	f1, f2 = f2, f1 + f2
	print(f2, end=' ')
	i += 1
print()
