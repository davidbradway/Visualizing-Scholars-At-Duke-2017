# Credit: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

import pandas as pd
import scipy.io as sio
import pickle
import os
import random

author = pd.read_csv('../author.txt', encoding='cp1252', sep=";")
# print(author.head())

# Load from file if possible
fname = '../coauthorgraph.pkl'
if os.path.isfile(fname):
    pkl_file = open(fname, 'rb')
    coauthorgraph = pickle.load(pkl_file)
    pkl_file.close()
else:
    mat_contents = sio.loadmat('../coauthornet.mat')
    coauthornet = mat_contents['coauthornet']
    # NdArray

    coauthor = pd.DataFrame(coauthornet,  # values
                            index=author['row index'],
                            columns=author['row index'])
    # print(coauthor.head())

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


def bfs_paths(graph, start, goal):
    # The queue contains a list of current nodes and the path to each of those nodes
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)  # pop it from the bottom of the stack, not the last-in
        # check all nodes before going to next depth
        # do not recheck any nodes already visited in the path
        for nextNode in graph[vertex] - set(path):
            if nextNode == goal:
                # Found the goal! Return the path with the nextNode (goal) at the end
                yield path + [nextNode]
            else:
                # Did not find the goal, add the nextNode to the queue for visiting later
                queue.append((nextNode, path + [nextNode]))


def shortest_bfs_path(graph, start, goal):
    # check for trivial case
    if start == goal:
        return [start]

    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return []


def test_graph():
    mygraph = {'A': {'B', 'C'},
               'B': {'A', 'D', 'E'},
               'C': {'A', 'F'},
               'D': {'B'},
               'E': {'B', 'F'},
               'F': {'C', 'E'}}
    found_path1 = shortest_bfs_path(mygraph, 'A', 'F')
    print(found_path1)
    # ['A', 'C', 'F']


def find_bacon(faculty1 = 11, faculty2 = 286):
    try:
        found_path = shortest_bfs_path(coauthorgraph, faculty1, faculty2)
        # print(found_path)
        return found_path
    except KeyError:
        found_path = []
        return found_path


def print_path(found_path):
    if found_path:
        for link in found_path:
            print(link, author.loc[link - 1]['author name'])


def loop_across(threshold = 8):
    longest_short_path = []

    lis1 = list(range(len(author)))
    random.shuffle(lis1)
    lis2 = list(range(len(author)))
    random.shuffle(lis2)

    for faculty1 in lis1:
        print(author.loc[faculty1]['author name'])

        for faculty2 in lis2:
            current_path = find_bacon(faculty1 + 1, faculty2 + 1)

            if len(current_path) > 1:
                if len(current_path) > len(longest_short_path):
                    longest_short_path = current_path
                    print_path(longest_short_path)
                    print(" ")
            if len(longest_short_path) > threshold:
                return longest_short_path

if __name__ == '__main__':
    # longest_short_path = find_bacon(11, 284)
    # print_path(longest_short_path)

    path = loop_across(8)
