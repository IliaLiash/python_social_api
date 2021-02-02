from timeit import timeit
import numpy as np
import pandas as pd

if __name__ == '__main__':
    setup_sum = 'data = list(range(10000))'
    setup_np = 'import numpy as np;'
    setup_np += 'data_np = np.array(list(range(10000)))'
    run_sum = 'result = sum(data)'
    run_np = 'result = np.sum(data_np)'

    time_sum = timeit(run_sum, setup=setup_sum, number=10000)
    time_np = timeit(run_np, setup=setup_np, number=10000)

    print('Время sum: ', time_sum)  #36.1823132 - 100000
    print('Время np.sum: ', time_np)    #0.7694703000000018 - 100000

'''
if __name__ == '__main__' означает что если файл импортирован как модуль то код после этих строк исполнен не будет,
а если запущен как самостоятельный файл то код после этих строк будет исполнен.
'''

data = {'user_id': [1, 2, 3, 4], 'возраст': [25, 35, 31, 19]}
frame = pd.DataFrame(data, columns=['user_id', 'возраст'])
print(frame.head())
frame['больше 30'] = frame['возраст'] > 30
print(frame.head())
frame['love python'] = pd.Series([True, False, True, True], index=frame.index)
print(frame.head())
print(frame.describe())