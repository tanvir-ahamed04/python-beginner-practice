import openai
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]  # Corrected 'message' to 'messages' and wrapped the dictionary inside a list
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("GPT: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("GPT:", response)
