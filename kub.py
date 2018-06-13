from random import randint


def cub():
	i = 0
	while True:
		i += 1
		cub1 = randint(1, 6)
		cub2 = randint(1, 6)
		if cub1 + cub2 == 8:
			print(cub1, cub2, i)
			break


cub()

