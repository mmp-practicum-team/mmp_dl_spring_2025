import glob
import argparse

import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Check answer correctness for matrix multiplication Hadoop Streaming task')
    parser.add_argument('-n', type=int, default=199, required=False)
    parser.add_argument('-m', type=int, default=201, required=False)
    parser.add_argument('-k', type=int, default=203, required=False)
    args = parser.parse_args()

    C_true = np.zeros([args.n, args.k], dtype=np.float32)
    C_predicted = np.zeros([args.n, args.k], dtype=np.float32)
    for filename in glob.glob('./data/output/part-*'):
        with open(filename, 'r') as file:
            lines = map(lambda line: line.strip().split('\t'), file.readlines())
            for key, value in lines:
                idx, jdx = key.split(',')
                C_predicted[int(idx), int(jdx)] = float(value)

    with open('./data/C.txt', 'r') as file:
        lines = map(lambda line: line.strip().split('\t'), file.readlines())
        for key, value in lines:
            idx, jdx = key.split(',')
            C_true[int(idx), int(jdx)] = float(value)

    deltas = np.abs(C_true - C_predicted)
    delta = np.max(deltas)
    max_index = np.unravel_index(np.argmax(deltas), shape=C_true.shape)
    if delta > 1e-4:
        print(f'Result is incorrect: delta = {delta} at position {max_index}')
    else:
        print(f'Success. delta = {delta} < 1e-4')

if __name__ == '__main__':
    main()
