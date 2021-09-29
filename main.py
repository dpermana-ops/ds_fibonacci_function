from find_fibonacci import find_fibonacci
import time

start = time.perf_counter()

for i in range(100):
  find_fibonacci(i)

finish = time.perf_counter()

executed_time = round(finish - start, 6)
print(f"Finished in {executed_time} second(s)")