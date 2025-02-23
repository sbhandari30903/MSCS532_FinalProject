import timeit
import numpy as np
import matplotlib.pyplot as plt

# Linked List Implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    
    def sum_values(self):
        total = 0
        current = self.head
        while current:
            total += current.value
            current = current.next
        return total

# Array Implementation
def sum_array(arr):
    return np.sum(arr)

# Data Preparation
sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 100000]
times_linked_list = []
times_array = []

for size in sizes:
    # Create data structures
    linked_list = LinkedList()
    for i in range(size):
        linked_list.append(i)
    array = np.array(range(size))

    # Benchmarking
    linked_list_time = timeit.timeit(lambda: linked_list.sum_values(), number=10)
    array_time = timeit.timeit(lambda: sum_array(array), number=10)
    times_linked_list.append(linked_list_time)
    times_array.append(array_time)

    print(f"\nSize: {size}")
    print(f"Linked List Sum Time: {linked_list_time:.6f} seconds")
    print(f"Array Sum Time: {array_time:.6f} seconds")

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(sizes, times_linked_list, label='Linked List', marker='o')
plt.plot(sizes, times_array, label='Array', marker='o')
plt.xlabel('Size')
plt.ylabel('Time (seconds)')
plt.title('Sum Performance Comparison')
plt.legend()
plt.savefig('performance_comparison.png')


