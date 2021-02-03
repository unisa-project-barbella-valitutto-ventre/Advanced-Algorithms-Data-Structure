from graphs.dfs_iterative import DFS_complete_iterative
from graphs.dfs import DFS_complete
from script_test.generate_graphs import generate_graph

if __name__ == '__main__':

    g = generate_graph(10)
    g.print_graph()

    print("*****DEVELOPED ITERATIVE VERSION*****")
    forest_iterative = DFS_complete_iterative(g)
    for key, value in zip(forest_iterative.keys(), forest_iterative.values()):
        print(str(key) + " " + str(value))

    print("*****RECURSIVE VERSION (FROM THE LIBREARY TDP_COLLECTION) FOR TESTING*****")
    forest = DFS_complete(g)
    for key, value in zip(forest.keys(), forest.values()):
        print(str(key) + " " + str(value))


