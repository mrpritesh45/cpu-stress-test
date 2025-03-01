# CPU Stress Test

A simple Python utility for stress testing CPU performance by maximizing processor utilization across all available cores.

## Overview

This tool creates worker processes equal to the number of available CPU cores on your system, with each process performing computation-intensive operations to generate high CPU load. It's useful for:

- Testing system stability under high CPU load
- Benchmarking cooling solutions
- Evaluating system performance under stress
- Testing power consumption under full load

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library modules)

## Usage

Simply run the script to start the stress test:

```bash
python cpu_stress_test.py
```

The program will:
1. Detect the number of available CPU cores
2. Launch a worker process for each core
3. Run until manually terminated with Ctrl+C

## Code Overview

```python
import multiprocessing
import time

def perform_intensive_calculation():
    """Execute a computation-heavy task that utilizes CPU resources."""
    while True:
        # Perform calculation that demands significant processor resources
        result = [number**2 for number in range(10**6)]

if __name__ == "__main__":
    # Determine available processing cores
    available_cores = multiprocessing.cpu_count()
    print(f"Initiating high CPU load test across {available_cores} cores...")
    
    # Create and launch worker processes
    worker_processes = []
    for i in range(available_cores):
        process = multiprocessing.Process(target=perform_intensive_calculation)
        process.start()
        worker_processes.append(process)
    
    # Main program loop
    try:
        # Keep main thread alive
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        # Handle user termination (Ctrl+C)
        print("CPU stress test terminating...")
        # Clean up all worker processes
        for process in worker_processes:
            process.terminate()
            process.join()
```

## Warning

This tool is designed to push your CPU to maximum utilization. Use with caution:

- Extended use may cause system overheating if cooling is inadequate
- Not recommended for systems with known thermal issues
- Monitor system temperatures when running for extended periods

## License

MIT License
