# from openai import OpenAI
#
# # OpenRouter API key
# API_KEY = "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"
#
# # Initialize OpenRouter client
# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=API_KEY
# )
#
# # Define your prompt here
# prompt = "what is cat?"
#
# # Optional: set temperature for creativity
# temperature = 0.6
#
# # Generate response
# completion = client.chat.completions.create(
#     extra_headers={
#         "HTTP-Referer": "http://localhost",  # Optional
#         "X-Title": "MyOpenRouterApp",       # Optional
#     },
#     model="openai/gpt-oss-20b:free",
#     messages=[{"role": "user", "content": prompt}],
#     temperature=temperature
# )
#
# # Print the chatbot's answer
# print("Prompt:", prompt)
# print("\nAnswer:", completion.choices[0].message.content)
#
#
# #  command to install package pip install openai
# #https://openrouter.ai/openai/gpt-oss-20b/api
# #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