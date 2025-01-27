import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self):
        self.functions = {
            "y=x": lambda x: x,
            "y=x^2": lambda x: x**2,
            "y=sin(x)": np.sin,
            "y=cos(x)": np.cos
        }

    def plot(self, function_name, x_min, x_max):
        if function_name not in self.functions:
            raise ValueError(f"Unsupported function: {function_name}")

        x = np.linspace(x_min, x_max, 500)
        y = self.functions[function_name](x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=function_name)
        plt.title(f"Plot of {function_name}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()