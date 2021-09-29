# Syncrhonous

from find_fibonacci import find_fibonacci
import time

start = time.perf_counter()

for i in range(100):
  find_fibonacci(i)

finish = time.perf_counter()

executed_time = round(finish - start, 6)
print(f"Finished in {executed_time} second(s)")

# Multithreading

from find_fibonacci import find_fibonacci
import time
import threading

start = time.perf_counter()
#start = 1.5
threads = []
for num in range(100):
  t = threading.Thread(target=find_fibonacci, args=[num])
  t.start()
  threads.append(t)

for thread in threads:
  thread.join()

finish = time.perf_counter()

executed_time = round(finish - start, 6)
print(f"Finished in {executed_time} second(s)")

# Multiprocessing

import multiprocessing
import time
from find_fibonacci import find_fibonacci

start = time.perf_counter()

processes = []
for num in range(10):
  p = multiprocessing.Process(target=find_fibonacci, args=[num])
  p.start()

  processes.append(p)

for process in processes:
  process.join()

finish = time.perf_counter()

executed_time = round(finish - start, 6)
print(f"Finished in {executed_time} second(s)")