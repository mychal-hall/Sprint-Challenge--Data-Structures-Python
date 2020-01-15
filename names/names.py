# It feels like maybe we could speed it up quite a bit by implementing a cache. I'll try that first.
# #$%#$ It worked!
# Initial code ran at 11s. Optimized to 0.009s just by using a cache.

import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

store = {}  # cache
duplicates = []
for name_1 in names_1:
    store[name_1] = name_1
for name_2 in names_2:
    if name_1 in store == name_2:
        duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
