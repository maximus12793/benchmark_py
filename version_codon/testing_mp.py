import openmp as omp
print(omp.get_num_threads())
omp.set_num_threads(32)