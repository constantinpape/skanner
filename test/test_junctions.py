import numpy as np
from skan import csr


def test_junctions(unique_junctions=True):
    x = np.zeros((7, 7), dtype='uint8')
    x[3, :] = 1
    x[:, 3] = 1
    print("input image")
    print(x)
    _, coords, _ = csr.skeleton_to_csgraph(x, unique_junctions=unique_junctions)
    print("coord for skel node 3, expected [2., 3.]")
    print(coords[3])


if __name__ == '__main__':
    test_junctions(False)
