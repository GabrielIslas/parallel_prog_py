import multiprocessing as mp
import numpy as np

class Process(mp.Process):
	def __init__(self, id, piover4, lock, N):
		super(Process, self).__init__()
		self.id = id
		self.piover4 = piover4
		self.lock = lock
		self.N = N

	def run(self):
		m = self.N // mp.cpu_count()
		dx = 1/self.N
		startArray = np.arange(self.id*m, (self.id+1)*m)
		xi = startArray * dx
		result = dx * ((1 - xi**2) ** (1/2))
		loc_sum = np.sum(result)
		with self.lock:
			self.piover4.value += loc_sum

def main(N):
	piover4 = mp.Value("d", lock = True)
	piover4.value = 0
	lock = mp.Lock()

	processes = [Process(i, piover4, lock, N) for i in range(mp.cpu_count())]
	[p.start() for p in processes]
	[p.join() for p in processes]
	result = piover4.value * 4
	print(result)

if __name__ == '__main__':
	main(100000)



