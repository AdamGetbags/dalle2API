# -*- coding: utf-8 -*-
"""
@author: AdamGetbags // OpenAI, Dall-E 2 image generation
"""

# pip install openai

# import modules
import os
import openai
from openaiSecrets import org, secret
import webbrowser

# assign credentials
openai.organization = org
openai.api_key = secret

# ping
print(openai.Model.list())

# image generation
# response = openai.Image.create(
#   prompt="programmer at the computer, victorian art, victorian era",
#   n=4,
#   size="1024x1024"
# )

# # for all images generated, open url to view images
# for i in range(0, len(response['data'])):
#     # get image url
#     image_url = response['data'][i]['url']

#     # open url
#     webbrowser.open(image_url)

# image variation
response = openai.Image.create_variation(
  image=open("C:\\Users\\AmatVictoriaCuramIII\\Desktop\\theFolder\\Python\\AGetbags.png",
              "rb"),
  n=2,
  size="1024x1024"
)

# for all images generated, open url to view images
for i in range(0, len(response['data'])):
    # get image url
    image_url = response['data'][i]['url']

    # open url
    webbrowser.open(image_url)
