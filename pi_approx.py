def approximate_pi(N):
	piover4 = 0
	dx = 1/N
	for i in range(N):
		xi = i * dx
		piover4 += dx * ((1 - xi**2) ** (1/2))
	return piover4 * 4

print(approximate_pi(100000))