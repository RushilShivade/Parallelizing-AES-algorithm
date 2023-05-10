# Parallelizing-AES-algorithm
Parallelizing AES algorithm in Python using MPI (mpi4py)

AES (Advanced Encryption Standard) is a widely used encryption algorithm. is a symmetrical block cipher algorithm that takes plain text in blocks of 128 bits and converts them to ciphertext using keys of 128, 192, and 256 bits. 

Serial approach of AES when concerned with a huge amount of data can be time consuming and inefficient as the mechanism consists of many rounds. Parallelizing this algorithm with a famous concept of Parallel Processing , MPI (Message Passing Interface) can reduce the time complexity of the execution and as results show, it takes even less than half of the execution time of naive approach. 

Here, MPI is used to distribute the workload to different processes and then combined to generate a single output thereby enabling multiple processes to run simultaneously. This mini project is done for my 6th Semester Parallel Computing subject.

Serial Approach
![image](https://github.com/RushilShivade/Parallelizing-AES-algorithm/assets/116446026/f71def95-3f99-42e7-9f2d-139b1e155a1e)

Parallel Approach
![image](https://github.com/RushilShivade/Parallelizing-AES-algorithm/assets/116446026/017c72c0-7e68-45c5-b1c1-454207d102cf)
