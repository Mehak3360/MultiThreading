import numpy as np
import time
import os
import pandas as pd
import matplotlib.pyplot as plt
from threadpoolctl import threadpool_limits

MATRIX_SIZE = 1000
NUM_MATRICES = 500

def run_experiment(num_threads):
    constant_matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)

    start = time.time()

    with threadpool_limits(limits=num_threads):
        for i in range(NUM_MATRICES):
            random_matrix = np.random.rand(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
            result = np.matmul(random_matrix, constant_matrix)
            _ = result[0][0]

            if (i + 1) % 50 == 0:
                print(f"Thread {num_threads}: completed {i+1}/{NUM_MATRICES}")

    end = time.time()
    return end - start

def main():
    cores = os.cpu_count()
    max_threads = 2 * cores

    print(f"Testing from 1 to {max_threads} threads\n")

    results = []

    for t in range(1, max_threads + 1):
        print(f"\nRunning with {t} thread(s)...")
        time_taken = run_experiment(t)
        print(f"Time: {time_taken:.4f} seconds\n")

        results.append({
            "Threads": t,
            "Time_seconds": time_taken
        })

    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)

    plt.figure()
    plt.plot(df["Threads"], df["Time_seconds"], marker='o')
    plt.title("Execution Time vs Threads")
    plt.xlabel("Threads")
    plt.ylabel("Time (seconds)")
    plt.grid()
    plt.savefig("graph.png")
    plt.show()

    print("Results saved in results.csv")
    print("Graph saved as graph.png")

if __name__ == "__main__":
    main()