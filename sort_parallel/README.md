# Sort Parallel

Task: Write an algorithm which sorts a list of numbers using parallel processing.

## Timings

Here are some timings for a sample machine (AMD fx8250, 8 cores)

### Timing list generation

```
python3 generate_list.py

   0.0092s, N=    10000,    0.0092s per 10k. generate unsorted list of random numbers
   0.0062s, N=    10000,    0.0062s per 10k. write unsorted list to file
   0.0013s, N=    10000,    0.0013s per 10k. sort list
   0.0062s, N=    10000,    0.0062s per 10k. write sorted list to file

   0.0934s, N=   100000,    0.0093s per 10k. generate unsorted list of random numbers
   0.0654s, N=   100000,    0.0065s per 10k. write unsorted list to file
   0.0191s, N=   100000,    0.0019s per 10k. sort list
   0.0680s, N=   100000,    0.0068s per 10k. write sorted list to file

   0.8854s, N=  1000000,    0.0089s per 10k. generate unsorted list of random numbers
   0.6801s, N=  1000000,    0.0068s per 10k. write unsorted list to file
   0.3356s, N=  1000000,    0.0034s per 10k. sort list
   0.7581s, N=  1000000,    0.0076s per 10k. write sorted list to file

   8.4536s, N= 10000000,    0.0085s per 10k. generate unsorted list of random numbers
   6.8888s, N= 10000000,    0.0069s per 10k. write unsorted list to file
   4.9341s, N= 10000000,    0.0049s per 10k. sort list
   7.8593s, N= 10000000,    0.0079s per 10k. write sorted list to file

  98.0245s, N=100000000,    0.0098s per 10k. generate unsorted list of random numbers
  67.3814s, N=100000000,    0.0067s per 10k. write unsorted list to file
 106.6602s, N=100000000,    0.0107s per 10k. sort list
  81.4213s, N=100000000,    0.0081s per 10k. write sorted list to file
```

### Timing just the sort

```
python3 time_sort_parallel.py

   0.0014s, N=    10000,    0.0014s per 10k. Sort internal
   0.0521s, N=    10000,    0.0521s per 10k. Sort parallel

   0.0191s, N=   100000,    0.0019s per 10k. Sort internal
   0.1437s, N=   100000,    0.0144s per 10k. Sort parallel

   0.3425s, N=  1000000,    0.0034s per 10k. Sort internal
   1.1811s, N=  1000000,    0.0118s per 10k. Sort parallel

   5.1535s, N= 10000000,    0.0052s per 10k. Sort internal
  12.1837s, N= 10000000,    0.0122s per 10k. Sort parallel

 108.7289s, N=100000000,    0.0109s per 10k. Sort internal
 170.4060s, N=100000000,    0.0170s per 10k. Sort parallel
```
