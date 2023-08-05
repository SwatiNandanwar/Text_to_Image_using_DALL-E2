# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:33:49 2023

@author: Pranjal Naphade
"""

import openai
import urllib.request
from PIL import Image
import streamlit as st



openai.api_key = "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"

def generate_image(image_description):

  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  

  img_url = img_response['data'][0]['url']

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img



# page title
st.title('DALL.E - Story Generation - OpenAI')

# text input box for image recognition
img_description = st.text_input('Story Desription')
words = img_description.split('.')
if st.button('Generate Image'):
    for i in range(0,len(words)):
        if(i>5):
            break;
        generated_img = generate_image(words[i])
        st.image(generated_img)
    