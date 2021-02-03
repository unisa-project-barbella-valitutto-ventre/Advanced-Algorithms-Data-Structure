from graph.read_graph_from_file import read_graph_from_file
from BaceFook.greedy_algorithm import call_func

if __name__ == '__main__':

    for i in range(5):
        g = read_graph_from_file("frb30-15-"+str(i+1)+".txt")
        list = call_func(g)
        print("Selected nodes = " + str(len(list)))
        print("Approximation ratio = " + str(len(list)/420))

    for i in range(5):
        g = read_graph_from_file("frb50-23-"+str(i+1)+".txt")
        list = call_func(g)
        print("Selected nodes = " + str(len(list)))
        print("Approximation ratio = " + str(len(list)/1100))
