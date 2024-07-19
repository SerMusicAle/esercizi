from multiprocessing import Process
import time
from random import randint

def bubble_sort():
    
    #arr = [64, 34, 25, 12, 22, 11, 90]
    arr = [randint (0, 10000) for _ in range(50000)]
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array:", arr)

def sleep():
    print(f"Sono nella funzione")
    
    time.sleep(60)
    
    print(f"Sto uscendo dalla funzione")
    
def print_time(tic: float):
    while True:
        time_elapsed = time.time() - tic
        print(f"tempo trascorso: {time_elapsed:.2f} secondi", end='\r')
    
if __name__ == "__main__":
    
    tic: float = time.time()
    
    t1 = Process (target=bubble_sort)
    t2 = Process (target=bubble_sort)
    t3 = Process (target=bubble_sort)
    t4 = Process (target=bubble_sort)
    t5 = Process (target=bubble_sort)


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    t_time = Process(target=print_time, args=(tic,))
    t_time.start()
    
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    t_time.terminate()
    
    toc: float = time.time()
    #time_elapsed: float = time.time()
    time_elapsed: float = toc - tic
    
    print(f"\n{time_elapsed=} secondi")
    
    
    

