import pickle
import os
import google.generativeai as genai
import matplotlib.pyplot as plt
import PIL.Image

google_api_key='AIzaSyBm1AppYECEOWE_vhMi7NrBl6Y3T718XLk'
genai.configure(api_key=google_api_key)

img=PIL.Image.open(r"C:\Users\a\Desktop\ANUJ_DOCUMENT\Anuj_photo.jpeg")
plt.imshow(img)
plt.axis('off') 
plt.show()

model = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0924')

response=model.generate_content(img)

