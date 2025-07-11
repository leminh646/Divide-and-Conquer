import random
import time
import tracemalloc
import csv
from mergeSort import mergeSort
from quickSort import quickSort

def generate_data(n, order):
    if order == 'random':
        return [random.randint(0, n) for _ in range(n)]
    if order == 'sorted':
        return list(range(n))
    if order == 'reversed':
        return list(range(n, 0, -1))
    raise ValueError(order)

def measure(func, data):
    # Time
    start_time = time.perf_counter()
    # Memory: start tracing
    tracemalloc.start()
    result = func(list(data))   # copy so original isn't modified
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed = time.perf_counter() - start_time
    return elapsed, peak / 1024**2  # seconds, peak MB

def run_trials(alg_name, func, sizes, orders, trials=3):
    rows = []
    for n in sizes:
        for order in orders:
            for t in range(trials):
                data = generate_data(n, order)
                t_sec, mem_mb = measure(func, data)
                rows.append({
                    'algorithm': alg_name,
                    'n': n,
                    'order': order,
                    'time_s': t_sec,
                    'mem_mb': mem_mb
                })
    return rows

def main():
    sizes  = [10_000, 50_000, 100_000]          # adjust as you like
    orders = ['random', 'sorted', 'reversed']
    all_rows = []
    
    all_rows += run_trials('MergeSort', mergeSort, sizes, orders)
    all_rows += run_trials('QuickSort', lambda a: quickSort(a), sizes, orders)
    
    # Write to CSV for later plotting/analysis
    with open('sort_benchmarks.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_rows[0].keys())
        writer.writeheader()
        writer.writerows(all_rows)
    print("Done: wrote sort_benchmarks.csv")

if __name__ == '__main__':
    main()
