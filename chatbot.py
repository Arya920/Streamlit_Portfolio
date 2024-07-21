# chatbot.py

# Define the command responses using a dictionary
command_responses = {
    "location": "Chinsurah Thakurgali, Hooghly",
    "years of experience": "1 year"
}

def get_response(command):
    return command_responses.get(command.lower(), 
        "Not a valid command. The valid commands are:\n" + 
        "\n".join([f"{i+1}. '{cmd}'" for i, cmd in enumerate(command_responses.keys())])
    )