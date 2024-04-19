from mpi4py import MPI
import numpy as np

def approximate_pi(N):
    # Rank
    r = MPI.COMM_WORLD.Get_rank()
    # Size
    size = MPI.COMM_WORLD.Get_size()
    # Elements in each
    m = N // size
    dx = 1/N
    startArray = np.arange(r*m, (r+1)*m)
    xi = startArray * dx
    operation = dx * ((1 - xi**2) ** (1/2))
    locsum = np.sum(operation)
    rcvBuf = np.array(0.0, "d")

    MPI.COMM_WORLD.Allreduce([locsum, MPI.DOUBLE], [rcvBuf, MPI.DOUBLE], op = MPI.SUM)
    return rcvBuf

s = approximate_pi(100000000) * 4

if MPI.COMM_WORLD.Get_rank() == 0:
    print("pi =", s)