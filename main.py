from llminterface import LLMInterface
from plotter import Plotter

def main():
    llm = LLMInterface()
    plotter = Plotter()

    print("Welcome to the Graph Plotting Application!")

    while True:
        user_input = input("What plot do you need? (e.g., 'Plot sine function from -5 to 5')\n")

        if "bye" in user_input.lower():
            print("Thank you for using the application! Goodbye!")
            break

        try:
            llm_response = llm.extract_plot_details(user_input)
            print(f"LLM Response: {llm_response}")

            # Example LLM response parsing: "function_name,x_min,x_max"
            function_name, x_min, x_max = llm_response.split(",")
            function_name = function_name.strip()
            x_min = float(x_min.strip())
            x_max = float(x_max.strip())

            plotter.plot(function_name, x_min, x_max)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()