import openai

openai.api_key = "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"

# Get user's name
user_name = input("Enter your name: ")
print("Respond with exit to exit the program.")

while True:
    # Get user input
    user_input = input(f"{user_name}: ")

    # Break the loop if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Use the OpenAI module to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use an appropriate engine
        prompt=f"{user_name}: {user_input}",
        max_tokens=150  # You can adjust this based on your preference
    )

    # Extract the generated text from the response
    ai_response = response.choices[0].text.strip()

    # Replace a placeholder with the custom name
    ai_response_with_name = ai_response.replace("AI:", f"{user_name}'s AI:")

    # Print the modified response
    print(ai_response_with_name)

