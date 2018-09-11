'''
# @Time    : 18-9-10 下午11:50
# @Author  : ShengZ
# @FileName: create_data.py
# @Software: PyCharm
# @Github  : https://github.com/ZZshengyeah
'''

import numpy as np
import os
'''
def element_wise_int(matrix):
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            matrix[i][j] = int(matrix[i][j])
    return matrix
'''


def inputs(num_samples):
    man_hand_length = np.random.normal(loc=27, scale=1, size=[num_samples,1])
    man_height = np.random.normal(loc=175, scale=3, size=[num_samples,1])
    man_feet = np.random.normal(loc=42, scale=1, size=[num_samples,1])
    man_skin_color_level = np.random.uniform(-1, 0, size=[num_samples,1])
    man_smooth_level = np.random.uniform(0.5, 2, size=[num_samples,1])

    man_positive_samples = np.concatenate((man_hand_length,
                                           man_height,
                                           man_feet,
                                           man_skin_color_level,
                                           man_smooth_level), axis=1)
    #man_positive_samples = element_wise_int(man_positive_samples)

    woman_hand_length = np.random.normal(loc=25, scale=1, size=[num_samples,1])
    woman_height = np.random.normal(loc=165, scale=3, size=[num_samples,1])
    woman_feet = np.random.normal(loc=38, scale=1, size=[num_samples,1])
    woman_skin_color_level = np.random.uniform(0, 1, size=[num_samples,1])
    woman_smooth_level = np.random.uniform(2, 3, size=[num_samples,1])

    woman_nagetive_samples = np.concatenate((woman_hand_length,
                                             woman_height,
                                             woman_feet,
                                             woman_skin_color_level,
                                             woman_smooth_level), axis=1)
    #woman_nagetive_samples = element_wise_int(woman_nagetive_samples)

    return man_positive_samples, woman_nagetive_samples

def may_write(num_samples):
    if not os.path.exists('./data/positive.txt') or os.path.exists('./data/nagetive.txt'):
        print('creating data...')
        positive, nagetive = inputs(num_samples)
        p_shape = positive.shape
        n_shape = nagetive.shape
        with open('./data/positive.txt','w') as f:
            for i in range(p_shape[0]):
                for j in range(p_shape[1]):
                    f.write(str(int(round(positive[i][j]))))
                    f.write('\t')
                f.write('\n')
        with open('./data/nagetive.txt','w') as f:
            for i in range(n_shape[0]):
                for j in range(n_shape[1]):
                    f.write(str(int(round(nagetive[i][j]))))
                    f.write('\t')
                f.write('\n')

if __name__ == '__main__':
    may_write(1000000)