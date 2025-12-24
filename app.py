import openai

# Replace with your actual API key
openai.api_key = "YOUR_API_KEY"

def ask_assistant(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print("AI Assistant Activated! (Type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = ask_assistant(user_input)
    print("Assistant:", response)
