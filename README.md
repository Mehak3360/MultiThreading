# MultiThreading Matrix Multiplication Project

## Objective
To analyze the performance of matrix multiplication using different numbers of threads.  
The project multiplies multiple random matrices with a constant matrix and measures execution time for varying thread counts.



## Problem Statement
- Multiply **500 random matrices** of size **1000 × 1000**
- Each matrix is multiplied with a **constant matrix** of the same size
- Perform the experiment for:
  - **T = 1 to 2 × number of CPU cores**
- Record:
  - Execution time
  - Performance variation
  - CPU usage



## System Configuration
- Logical CPU Cores: **4**
- Threads tested: **1 to 8**
- Language: **Python**
- Environment: **VS Code**



## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- threadpoolctl
- psutil



## Methodology
1. Detect number of CPU cores using `os.cpu_count()`
2. Set maximum threads = `2 × cores`
3. Generate one constant matrix
4. For each thread count:
   - Limit threads using `threadpoolctl`
   - Generate random matrices one by one
   - Perform matrix multiplication
   - Measure execution time
5. Store results in CSV
6. Plot execution time vs threads graph
7. Monitor CPU usage using Task Manager



## Results

### Execution Time vs Threads
![Execution Graph]<img width="604" height="481" alt="image" src="https://github.com/user-attachments/assets/879f705e-e2ef-4959-a135-35003eb2e360" />


### Sample Output Table

| Threads | Time (seconds) |
|--------|---------------|
| 1 | 34 |   22.8166     |
| 2 | 23 |   16.4291     |
| 3 | 54 |   16.5201     |
| 4 | 54 |   15.0950     |
| 5 | 33 |   44.4958     |
| 6 | 28 |   34.7614     |
| 7 | 36 |   101.8462    |
| 8 | 30 |   82.8880     |



## Observations
- Best performance observed at **2 threads**
- Increasing threads beyond optimal leads to:
  - Overhead
  - CPU contention
  - Memory bottlenecks
- Performance does **not scale linearly** with threads



## Challenges Faced
- Handling large matrix sizes (memory constraints)
- Managing CPU utilization visibility
- Thread overhead affecting performance



## Conclusion
- Multithreading improves performance only up to an optimal point
- Excess threads can degrade performance due to system limitations
- Efficient thread management is crucial for high-performance computing



## Future Scope
- Use **multiprocessing** instead of threading
- Test with larger matrices (e.g., 5000 × 5000)
- Compare with GPU-based computation
- Analyze memory usage alongside CPU usage



