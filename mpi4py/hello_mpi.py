from mpi4py import MPI
from mpi4py.futures import MPICommExecutor
import sys
import time
import os

def print_hello(rank, size, name):
    msg = "Hello Aoife! I am rank {0} of size {1}. You can find me on node {2}."
    print(msg.format(rank, size, name))
    return msg

def naptime():
    time.sleep(5)

comm_size = MPI.COMM_WORLD.Get_size()
comm_rank = MPI.COMM_WORLD.Get_rank()
node_name = MPI.Get_processor_name()

# outside of MPICommPool, all workers return a value
print_hello(comm_rank, comm_size, node_name)

with MPICommExecutor(MPI.COMM_WORLD, root=0) as executor:
    if executor is not None:
        executor.max_workers = comm_size

        # Each worker runs print_hello() and then sleeps
        executor.submit(
            print_hello(comm_rank, comm_size, node_name)
        )
        executor.submit(
            naptime()
        )

        # inside of MPICommPool, all workers return a value only the root process (0) will return a value
        future = executor.submit(abs, -42)
        assert future.result() == 42
        answer = set(executor.map(abs, [-42, 42]))
        assert answer == {42}
        msg = "\tThe meaning of life is {0}!\n".format(answer)
        print(msg)