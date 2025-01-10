import requests

class QwenAgent:
    def __init__(self, api_url):
        """
        Initialize the QwenAgent with the API URL.
        :param api_url: The endpoint of the Qwen-2.5 model API
        """
        self.api_url = api_url

    def ask_question(self, question):
        """
        Send a question to the Qwen-2.5 model and retrieve the response.
        :param question: The user's question as a string
        :return: Model's answer as a string
        """
        payload = {"input": question}
        headers = {'Content-Type': 'application/json'}

        try:
            # Make a POST request to the Qwen API
            response = requests.post(self.api_url, json=payload, headers=headers)
            if response.status_code == 200:
                return response.json().get("output", "No response available.")
            else:
                return f"Error {response.status_code}: {response.text}"
        except Exception as e:
            return f"An error occurred: {str(e)}"


class CrewAI:
    def __init__(self, agent):
        """
        Initialize the CrewAI framework with a single agent.
        :param agent: An agent instance (e.g., QwenAgent)
        """
        self.agent = agent

    def handle_input(self, user_input):
        """
        Process the user's input using the agent.
        :param user_input: The user's input as a string
        :return: The agent's response
        """
        return self.agent.ask_question(user_input)


def main():
    """
    Main program loop to interact with the Qwen-2.5 model.
    """
    api_url = "http://localhost:8000/qwen"  # Replace with the Qwen-2.5 API endpoint
    qwen_agent = QwenAgent(api_url)

    # Initialize CrewAI with the QwenAgent
    crew_ai = CrewAI(agent=qwen_agent)

    print("Ask a question to Qwen-2.5! (type 'exit' to quit)")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Process input through CrewAI
        response = crew_ai.handle_input(user_input)
        print(f"Qwen-2.5: {response}")


if __name__ == "__main__":
    main()
