import time


nemo = ['nemo'] * 100

large = ['nemo'] * 10000

def find_nemo(array):
    t0 = time.time()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo!')
    t1 = time.time()
    print(f'Time taken: {t1 - t0} seconds')
        
find_nemo(large) # O(n) --> Linear Time
