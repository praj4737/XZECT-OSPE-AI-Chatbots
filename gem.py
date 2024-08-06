import google.generativeai as genai
import os
import os

genai.configure(api_key="AIzaSyDZ2hAL6ydGGpHsT2UfvORKMVi-LSYE-eI")
# api_key="AIzaSyDZ2hAL6ydGGpHsT2UfvORKMVi-LSYE-eI"

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(["who is gandhi"])
print(response.text)
print()