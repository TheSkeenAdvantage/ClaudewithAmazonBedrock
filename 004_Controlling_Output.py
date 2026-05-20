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

def chat(messages, system=None, temperature=1.0):
    params = {
        "modelId": model_id, 
        "messages": messages,
        "inferenceConfig": {"temperature": temperature}
    }
    
    if system:
        params["system"] = [{"text": system}]
    
    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]


messages = []
add_user_message(messages, "Is coffee or tea better for breakfast?")
add_assistant_message(messages, "Coffee is better because")

chat(messages)
