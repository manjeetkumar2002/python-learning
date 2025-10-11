# from openai import OpenAI
#
# # Hugging Face API key
# API_KEY = ""
#
# # Initialize OpenRouter client
# client = OpenAI(
#     base_url="https://router.huggingface.co/v1",
#     api_key=API_KEY
# )
#
# # Define your prompt here
# prompt = "Explain the concept of quantum computing in simple words."
#
# # Set temperature (0.0 = deterministic, 1.0 = creative)
# temperature = 0.7 # temperature determine the quality of output
#
# # Generate text completion
# completion = client.chat.completions.create(
#     model="openai/gpt-oss-120b:fireworks-ai",
#     messages=[{"role": "user", "content": prompt}],
#     temperature=temperature
# )
#
# # Print prompt and generated answer
# print("Prompt:", prompt)
# print("\nAnswer:", completion.choices[0].message.content)