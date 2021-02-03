from BaceFook.dp_algorithm import call_func
from Main.testing_graphs import *

if __name__ == '__main__':

    g,v = g4()

    list = call_func(g,v)
    print("THE VERTECES IN WHICH INSTALL THE SOFTWARE ARE: " + str(len(list)) + ":")
    for v in list:
        print(str(v.element()))
