"""
Write a Python program that demonstrates manual garbage collection using the gc module. This
program will create some objects, manually collect garbage, and show the differences in memory usage
before and after garbage collection.
"""
import gc
import sys

# 1. Print initial garbage collection thresholds
print("Initial GC Thresholds:", gc.get_threshold())

# 2. Function to create reference cycles
def create_cycle(iteration):
    # Creating a cyclic reference (dictionary referencing itself)
    x = {}
    x[iteration] = x

print("\n--- Initial State ---")
initial_collected = gc.collect()
print(f"Garbage collector initial collection: {initial_collected} objects.")

print("\nCreating cyclic reference objects...")
for i in range(1, 11):
    create_cycle(i)

print("\n--- Manual Garbage Collection ---")
# Manually run full garbage collection (Generation 2)
collected_count = gc.collect()

print(f"Garbage collector manually collected: {collected_count} objects.")

# 3. Enable debug flags to show GC activity details (Optional demonstration)
print("\n--- GC Stats ---")
print("Objects currently tracked by GC:", len(gc.get_objects()))
print("Current GC count per generation:", gc.get_count())
"""
--> Output
Initial GC Thresholds: (2000, 10, 0)

--- Initial State ---
Garbage collector initial collection: 22 objects.

Creating cyclic reference objects...

--- Manual Garbage Collection ---
Garbage collector manually collected: 10 objects.

--- GC Stats ---
Objects currently tracked by GC: 5423
Current GC count per generation: (0, 0, 0)
"""