import matplotlib.pyplot as plt
import numpy as np

def plot_graph(function_name, x_min, x_max):
    try:
        x = np.linspace(x_min, x_max, 500)

        if function_name == "y=x":
            y = x
        elif function_name == "y=x^2":
            y = x ** 2
        elif function_name == "y=sin(x)":
            y = np.sin(x)
        elif function_name == "y=cos(x)":
            y = np.cos(x)
        else:
            print("Unsupported function.")
            return

        plt.plot(x, y)
        plt.title(f"Graph of {function_name}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.show()
        
    except Exception as e:
        print(f"Error plotting the graph: {e}")