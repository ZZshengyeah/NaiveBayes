'''
# @Time    : 18-9-11 上午1:10
# @Author  : ShengZ
# @FileName: naivebayes.py
# @Software: PyCharm
# @Github  : https://github.com/ZZshengyeah
'''

from collections import defaultdict, Counter
num_features = 5


def read_data(data):
    feature_value_dic = defaultdict(list)
    num_samples = 0
    with open(data,'r') as f:
        for line in f:
            line = line.strip().split('\t')
            num_samples += 1
            for i in range(num_features):
                feature_value_dic[i].append(line[i])
    return feature_value_dic, num_samples

def compute_possibility(data):
    feature_value_dic, num_samples = read_data(data)
    possibility = defaultdict(list)
    for i in range(num_features):
        count_dic = Counter(feature_value_dic[i])
        for j in count_dic:
            possibility[i].append((j,count_dic[j]/num_samples))
    return possibility

def naivebayes(data, input_data):
    '''

    :param input_data: eg: '27 175 40 -1 1'
    :return: eg: 概率， 标签
    '''
    features = input_data.strip().split()
    conditional_p = compute_possibility(data)
    #print(conditional_p)
    p = 1
    for i in range(num_features):
        try:
            for j in conditional_p[i]:
                if j[0] == features[i]:
                    p = p * j[1]
        except:
            p = p * 0.00001
    return p
if __name__ == '__main__':
    positive_sample = './data/positive.txt'
    nagetive_sample = './data/nagetive.txt'
    #input_data = input('Please input:\n')
    input_data = '24 170 37 0 1'
    p1 = naivebayes(positive_sample, input_data)
    p0 = naivebayes(nagetive_sample, input_data)

    print('p: {}, label: 1'.format(p1))
    print('p: {}, lable: 0'.format(p0))
    if p1 > p0:
        label = 1
    else:
        label = 0
    print('The lable of input is %d' %label)