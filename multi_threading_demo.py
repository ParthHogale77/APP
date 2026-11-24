"""
Write a program that demonstrates threading by performing three tasks: counting numbers,
calculating the square of numbers, and calculating the cube of numbers.
"""
import threading
import time

# 1. Function to Count Numbers
def count_numbers(limit=5):
    print("Task 1: Starting number counting...")
    for i in range(1, limit + 1):
        print(f"[Count]: {i}")
        time.sleep(0.5)  # Simulate delay
    print("Task 1: Counting finished.")

# 2. Function to calculate squares
def calculate_squares(numbers):
    print("Task 2: Starting square calculation...")
    for num in numbers:
        print(f"[Square]: {num}^2 = {num ** 2}")
        time.sleep(0.7)  # Simulate delay
    print("Task 2: Squares finished.")

# 3. Function to calculate cubes
def calculate_cubes(numbers):
    print("Task 3: Starting cube calculation...")
    for num in numbers:
        print(f"[Cube]: {num}^3 = {num ** 3}")
        time.sleep(0.6)  # Simulate delay
    print("Task 3: Cubes finished.")

# Main execution section
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    # Create threads for each task
    thread1 = threading.Thread(target=count_numbers, args=(5,))
    thread2 = threading.Thread(target=calculate_squares, args=(data,))
    thread3 = threading.Thread(target=calculate_cubes, args=(data,))

    print("--- Starting All Threads ---")
    
    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

    print("--- All tasks executed concurrently and finished! ---")

"""
--> Output
--- Starting All Threads ---
Task 1: Starting number counting...
[Count]: 1
Task 2: Starting square calculation...
[Square]: 1^2 = 1
Task 3: Starting cube calculation...
[Cube]: 1^3 = 1
[Count]: 2
[Cube]: 2^3 = 8
[Square]: 2^2 = 4
[Count]: 3
[Cube]: 3^3 = 27
[Square]: 3^2 = 9
[Count]: 4
[Cube]: 4^3 = 64
[Count]: 5
[Square]: 4^2 = 16
[Cube]: 5^3 = 125
Task 1: Counting finished.
[Square]: 5^2 = 25
Task 3: Cubes finished.
Task 2: Squares finished.
--- All tasks executed concurrently and finished! --- 
"""