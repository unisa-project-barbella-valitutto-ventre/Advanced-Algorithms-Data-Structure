from BaceFook.greedy_algorithm import call_func
from graph.generate_graphs import generate_graph
import time

if __name__ == '__main__':

    average_time = 0
    average_selected_nodes = 0
    number_simulations = 100
    number_nodes = 100

    for i in range(number_simulations):
        g = generate_graph(number_nodes)
        start_time = time.time()
        list = call_func(g)
        run_time = time.time() - start_time
        print("The algorithm selected " + str(len(list)) + " in " + str(run_time) + " seconds")
        average_time += run_time
        average_selected_nodes += len(list)

    print("")
    print("The average time is " + str(average_time/number_simulations) + " seconds")
    print("The average number of selected nodes is " + str(average_selected_nodes/number_nodes))
