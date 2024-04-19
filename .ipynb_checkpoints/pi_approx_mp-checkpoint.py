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
    
        for i in range(self.id*m, (self.id+1)*m):
    		xi = i * dx
    		result = dx * ((1 - xi**2) ** (1/2))
		with self.lock:
			self.piover4.value += result

def main(N):
	piover4 = mp.Value("d", lock = True)
	piover4.value = 0
	lock = mp.Lock()

	processes = [Process(i, piover4, lock, N) for i in range(mp.cpu_count())]
	[p.start() for p in processes]
	[p.join() for p in processes]
	result = piover4.value * 4



