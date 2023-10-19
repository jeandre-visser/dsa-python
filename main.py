nemo = ['nemo']

def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found Nemo!')
            break
        
find_nemo(nemo) # O(n) --> Linear Time
