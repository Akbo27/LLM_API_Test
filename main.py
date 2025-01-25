from llminterface import get_graph_details
from plotter import plot_graph

def main():
    print("Welcome to the Graph Plotting App!")
    while True:
        user_input = input("Describe the plot you need (e.g., 'plot sine function from -5 to 5'): ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Thank you for using the Graph Plotting App. Goodbye!")
            break
        
        response = get_graph_details(user_input)
        
        if response.get("function_name") and response.get("x_min") is not None and response.get("x_max") is not None:
            function_name = response["function_name"]
            x_min = response["x_min"]
            x_max = response["x_max"]
            
            # Plot the graph
            plot_graph(function_name, x_min, x_max)
        else:
            print("Please try again.")

if __name__ == "__main__":
    main()