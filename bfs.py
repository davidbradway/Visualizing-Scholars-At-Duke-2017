# Credit: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

import pandas as pd
import scipy.io as sio
import pickle
import os


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)  # pop it from the bottom of the stack, not the last-in
        for nextNode in graph[vertex] - set(path):
            if nextNode == goal:
                yield path + [nextNode]
            else:
                queue.append((nextNode, path + [nextNode]))


def shortest_bfs_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


if __name__ == '__main__':
    """
    mygraph = {'A': {'B', 'C'},
           'B': {'A', 'D', 'E'},
           'C': {'A', 'F'},
           'D': {'B'},
           'E': {'B', 'F'},
           'F': {'C', 'E'}}
    found_path = shortest_bfs_path(mygraph, 'A', 'F')  # ['A', 'C', 'F']
    print(found_path)
    """

    author = pd.read_csv('../author.txt', encoding='cp1252', sep=";")
    # print(author.head())

    mat_contents = sio.loadmat('../coauthornet.mat')
    coauthornet = mat_contents['coauthornet']
    # NdArray

    coauthor = pd.DataFrame(coauthornet,    # values
                            index=author['row index'],    # Names as index
                            columns=author['row index'])  # Names as column names
    # print(coauthor.head())

    # Load from file if possible
    fname = '../coauthorgraph.pkl'
    if os.path.isfile(fname):
        pkl_file = open(fname, 'rb')
        coauthorgraph = pickle.load(pkl_file)
        pkl_file.close()
    else:
        # Adjacency list (for sparse graphs)
        coauthorgraph = {}
        for index, row in coauthor.iterrows():
            myset = set()
            for colindex, col in row.iteritems():
                if col > 0 and index != colindex:
                    # print(index, colindex, col)
                    myset |= {colindex}
            if myset:
                coauthorgraph[index] = myset

        pkl_file = open(fname, 'wb')
        pickle.dump(coauthorgraph, pkl_file)
        pkl_file.close()

    found_path = shortest_bfs_path(coauthorgraph, 11, 286)
    # print(found_path)

    if found_path:
        for link in found_path:
            print(author.loc[link - 1]['author name'])
