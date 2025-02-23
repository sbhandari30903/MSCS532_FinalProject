# MSCS532_FinalProject
# Data Structure Performance Comparison

This project compares the performance of summing elements in two different data structures: Linked Lists and NumPy Arrays. It demonstrates the efficiency differences between these implementations and visualizes the results.

## Overview

The program implements and compares:
- A custom Linked List implementation
- NumPy array operations
- Performance benchmarking using `timeit`
- Visualization of results using matplotlib

## Requirements

- Python 3.x
- NumPy
- Matplotlib

You can install the required packages using:
```bash
pip install numpy matplotlib
```

## Implementation Details

### Data Structures
1. **Linked List**
   - Custom implementation with `Node` and `LinkedList` classes
   - Includes methods for appending values and computing sums

2. **NumPy Array**
   - Uses NumPy's built-in array implementation
   - Leverages NumPy's optimized `sum()` function

### Benchmarking
- Tests performed on different data sizes: 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 100000 elements
- Each test runs 10 iterations to ensure reliable timing
- Results are plotted for visual comparison

## Output

The program generates:
1. Console output showing timing results for each data size
2. A plot saved as 'performance_comparison.png' comparing the performance of both implementations

## Results

The visualization demonstrates the performance differences between linked lists and arrays when performing sum operations. Generally, NumPy arrays show superior performance due to:
- Contiguous memory allocation
- Optimized C-level implementations
- Better cache utilization

## Usage

To run the program, use:

```bash
python HPC.py
```

The program will:
1. Run the performance tests
2. Print timing results to the console
3. Generate and save the performance comparison plot
