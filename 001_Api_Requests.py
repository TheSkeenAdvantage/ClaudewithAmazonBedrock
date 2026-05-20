import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")
model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0"

def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [
            {"text": text}
        ]
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": [
            {"text": text}
        ]
    }
    messages.append(assistant_message)

def chat(messages):
    response = client.converse(
        modelId=model_id,
        messages=messages
    )
    return response["output"]["message"]["content"][0]["text"]


# Make a starting list of messages
messages = []

# Add in the initial user question of "What's 1+1?"
add_user_message(messages, "What's 1+1?")

# Pass the list of messages into chat to get an answer
answer = chat(messages)

# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's followup question
add_user_message(messages, "And 3 more added to that?")

# Call chat again with the list of messages to get a final answer
answer = chat(messages)
print(answer)

#Make an initial list of messages
messages = []

#Use a 'while True' loop to run the chatbot forever
while True:
    #Get user input from the terminal
    user_input = input("User: ")
    print("User:", user_input)

    #Add the user message to the list of messages
    add_user_message(messages, user_input)

    #Pass the list of messages into chat to get an answer
    answer = chat(messages)

    #Take the answer and add it as an assistant message into our list
    add_assistant_message(messages, answer)

    #Print out the assistant's answer
    print("Assistant:", answer)
