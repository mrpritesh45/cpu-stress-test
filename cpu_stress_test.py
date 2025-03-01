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
