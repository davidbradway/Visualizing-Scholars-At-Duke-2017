# Credit: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

import pandas as pd
import scipy.io as sio
import pickle
import os
import random
import argparse

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
    visited = []
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)  # pop it from the bottom of the stack, not the last-in
        # do not recheck any nodes already visited in the path
        if vertex not in visited:
            visited.append(vertex)
            # print(len(visited))

            # check all nodes before going to next depth
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


def find_bacon(faculty1=11, faculty2=286):
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


def fprint_path(found_path, fid):
    if found_path:
        for link in found_path:
            fid.write(str(link) + ', ' + author.loc[link - 1]['author name'] + '\n')


def loop_across(threshold):
    longest_short_path = []

    lis1 = list(range(len(author)))
    lis2 = list(range(len(author)))

    for faculty1 in lis1:
        # print(author.loc[faculty1]['author name'])

        for faculty2 in lis2:
            current_path = find_bacon(faculty1 + 1, faculty2 + 1)

            if len(current_path) > 1:

                if len(current_path) > len(longest_short_path):
                    print(len(current_path))
                    longest_short_path = current_path
                    print_path(longest_short_path)
                    print(" ")

                    f = open('../' + str(faculty1) + '_' + str(faculty2) + '_' + str(
                        len(longest_short_path)) + '.txt', 'w')
                    fprint_path(longest_short_path, f)
                    f.close()

                    # if len(longest_short_path) > threshold:
                    #    return longest_short_path
    print('done')


if __name__ == '__main__':
    path = loop_across(27)
    f = open('../result.txt', 'w')
    fprint_path(path, f)
    f.close()

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("faculty1", help="enter the ID of the first faculty", type=int)
    parser.add_argument("faculty2", help="enter the ID of the second faculty", type=int)
    args = parser.parse_args()

    longest_short_path = find_bacon(args.faculty1, args.faculty2)
    print_path(longest_short_path)

    f = open('../' + str(args.faculty1) + '_' + str(args.faculty2) + '_' + str(len(longest_short_path)) + '.txt', 'w')
    fprint_path(longest_short_path, f)
    f.close()
    """
