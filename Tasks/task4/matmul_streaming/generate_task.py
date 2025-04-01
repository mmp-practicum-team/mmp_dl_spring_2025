import os
import argparse

import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Generate task for matrix multiplication Hadoop Streaming')
    parser.add_argument('-n', type=int, default=199, required=False)
    parser.add_argument('-m', type=int, default=201, required=False)
    parser.add_argument('-k', type=int, default=203, required=False)
    args = parser.parse_args()

    os.makedirs('./data/input', exist_ok=True)

    A = np.random.normal(size=(args.n, args.m))
    B = np.random.normal(size=(args.m, args.k))
    with open('./data/input/A.txt', 'w') as a_file:
        for idx, line in enumerate(A):
            values = ' '.join(['{0:.5f}'.format(value) for value in line])
            print('{0} {1}'.format(idx, values), file=a_file)
    with open('./data/input/B.txt', 'w') as b_file:
        for idx, line in enumerate(B):
            values = ' '.join(['{0:.5f}'.format(value) for value in line])
            print('{0} {1}'.format(idx, values), file=b_file)

    A = np.around(A, decimals=5)
    B = np.around(B, decimals=5)
    C = A @ B
    with open('./data/C.txt', 'w') as c_file:
        for idx in range(args.n):
            for jdx in range(args.k):
                line = '{0},{1}\t{2:.5f}'.format(idx, jdx, C[idx, jdx])
                print(line, file=c_file)

if __name__ == '__main__':
    main()
