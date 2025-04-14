import argparse
import random
import time
import matplotlib
matplotlib.use("MacOSX")  # or "TkAgg" if MacOSX gives issues
import matplotlib.pyplot as plt

# Dummy versions of sorting algos (replace with your real ones)
from algorithms.sorting.quicksort import quicksort
from algorithms.sorting.mergesort import mergesort
from algorithms.sorting.heapsort import heapsort
from algorithms.sorting.bubblesort import bubblesort

def benchmark_sort(algo, size):
    arr = [random.randint(1, 10000) for _ in range(size)]
    print(f"Running {algo} on list of size {size}")

    start = time.time()
    if algo == "quicksort":
        sorted_arr = quicksort(arr)
    elif algo == "mergesort":
        sorted_arr = mergesort(arr)
    elif algo == "heapsort":
        sorted_arr = heapsort(arr.copy())
    elif algo == "bubblesort":
        sorted_arr = bubblesort(arr.copy())
    else:
        raise ValueError("Unsupported algorithm")
    end = time.time()

    print(f"✅ Completed in {end - start:.6f} seconds")

def plot_benchmarks():
    import matplotlib.pyplot as plt

    input_sizes = [100, 500, 1000, 2000, 3000]
    algos = {
        "quicksort": lambda a, c: quicksort(a, counter=c),
        "mergesort": lambda a, c: mergesort(a, counter=c),
        "heapsort": lambda a, c: heapsort(a.copy(), counter=c),
        ##"bubblesort": lambda a, c: bubblesort(a.copy(), counter=c)
    }

    results = {name: [] for name in algos}           # runtime
    comparisons = {name: [] for name in algos}       # comparisons

    for size in input_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        for name, func in algos.items():
            input_copy = arr.copy()
            counter = {"comparisons": 0}
            start = time.time()
            func(input_copy, counter)
            end = time.time()

            results[name].append(end - start)
            comparisons[name].append(counter["comparisons"])

    # --- Plot Runtime ---
    plt.figure(figsize=(10, 5))
    for name in results:
        plt.plot(input_sizes, results[name], label=name)
    plt.title("Runtime vs Input Size")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("runtime_plot.png")
    print("📈 Saved runtime_plot.png")

    # --- Plot Comparisons ---
    plt.figure(figsize=(10, 5))
    for name in comparisons:
        plt.plot(input_sizes, comparisons[name], label=name)
    plt.title("Comparisons vs Input Size")
    plt.xlabel("Input Size")
    plt.ylabel("Number of Comparisons")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("comparisons_plot.png")
    print("📊 Saved comparisons_plot.png")
    
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="CodeQuest CLI")
    parser.add_argument("--algo", type=str, help="Sorting algorithm to use")
    parser.add_argument("--size", type=int, default=1000)
    parser.add_argument("--graph", action="store_true", help="Generate runtime graph")
    args = parser.parse_args()

    if args.graph:
        plot_benchmarks()
    elif args.algo:
        benchmark_sort(args.algo.lower(), args.size)
    else:
        print("⚠️  Please specify --algo or --graph")

if __name__ == "__main__":
    main()