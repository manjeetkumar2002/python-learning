from openai import OpenAI

# OpenRouter API key
API_KEY = "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"

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)


def generate_text(prompt, temperature=1.0):
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "http://localhost",  # Optional
            "X-Title": "MyOpenRouterApp",  # Optional
        },
        model="openai/gpt-oss-20b:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature  # Added temperature here
    )
    return completion.choices[0].message.content


def main():
    print("📝 OpenRouter Text Generation App with Temperature")
    print("Type 'exit' to quit.\n")

    # Ask user for temperature
    while True:
        try:
            temp_input = input("Set temperature (0.0 to 2.0, default 1.0): ").strip()
            if temp_input == "":
                temperature = 1.0
            else:
                temperature = float(temp_input)
                if not (0.0 <= temperature <= 2.0):
                    print("❌ Temperature must be between 0.0 and 2.0. Using default 1.0")
                    temperature = 1.0
            break
        except ValueError:
            print("❌ Invalid input. Enter a number between 0.0 and 2.0.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        try:
            response = generate_text(user_input, temperature)
            print(f"Bot: {response}\n")
        except Exception as e:
            print("❌ Error:", e)
            break


if __name__ == "__main__":
    main()
