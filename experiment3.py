# from huggingface_hub import InferenceClient
# from PIL import Image
#
# # Hugging Face API key
# API_KEY = ""
#
# # Initialize Hugging Face InferenceClient
# client = InferenceClient(
#     provider="hf-inference",
#     api_key=API_KEY,
# )
#
# # Prompt for the image
# prompt = "Black clouds and neon colors in background , A BMW M5 white color with sunroof standing in center on a stage"
#
# # Generate image using Stable Diffusion XL model
# # Output will be a PIL.Image object
# image = client.text_to_image(
#     prompt,
#     model="stabilityai/stable-diffusion-xl-base-1.0"
# )
#
# # Display the image
# image.show()
#
# # Save the image
# image.save("output.png")
# print("✅ Image saved as output.png")
#
# # install package huggingface_hub
# # install pillow package