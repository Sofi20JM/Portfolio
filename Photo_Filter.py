from ast import Num
from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import numpy as np


def apply_grayscale(image):
  img = Image.open(image)
  copy = img.copy()
  gray_scale = copy.convert("L") # The L mode represents grayscale (Luminance)
  gray_scale.save("edited_profile.png")
  # Show the image 
  plt.imshow(gray_scale, cmap='gray')  
  plt.axis('off')  
  plt.show()


def apply_blur(image):
  with Image.open(image) as img:
    copy = img.copy()
    blurred = copy.filter(ImageFilter.GaussianBlur(4)) 
  blurred.save('edited_profile.png')
  # Show the image 
  plt.imshow(blurred)  
  plt.axis('off')  
  plt.show()


def apply_yellow_filter(image):
  with Image.open(image) as img:
    output = []
    for pixel in img.getdata():
      yellow_only = (pixel[0], pixel[1], 0)
      output.append(yellow_only)
    yellow = img.putdata(output) 
  # Save Image and converts it into an array
    img.save('edited_profile.png')
    img_array = np.array(img)
  # Show Image
  plt.imshow(img_array)  
  plt.axis('off')  
  plt.show()


def increase_brightness(image, num):
  with Image.open(image) as img:
    enhancer = ImageEnhance.Brightness(img)
    img_brightened = enhancer.enhance(1+num/100)
    # Saving image 
    img_brightened.save('edited_profile.png')
    # Show the image using matplotlib
    plt.imshow(img_brightened)
    plt.axis('off') 
    plt.show()


def decrease_brightness(image, num):
  with Image.open(image) as img:
    enhancer = ImageEnhance.Brightness(img)
    img_darker = enhancer.enhance(1-num/100)
    # Saving image 
    img_darker.save('edited_profile.png')
    # Show the image using matplotlib
    plt.imshow(img_darker)
    plt.axis('off') 
    plt.show()


def apply_transparency(image, percentage):

  with Image.open(image) as img:
    rgba_image = img.convert("RGBA")
    r, g, b, a = rgba_image.split() 
    num = int(256 - percentage * 128 / 50)
    rgba_image.putalpha(num) 
    # Saves Image 
    rgba_image.save('edited_profile.png')
    # Shows Image 
    plt.imshow(rgba_image)
    plt.axis('off') 
    plt.show()


def half_size(image):
  with Image.open(image) as img:
    # Calculate the new width and heigth
    new_width = int(img.size[0] / 4.0)
    new_height = int(img.size[1] / 4.0)

    output = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    output.save('edited_profile.png')

    plt.imshow(output)
    plt.axis('off')
    plt.show()


def apply_filter(image): 
  print("Hi! What filter/efect would you like to apply?\n")
  print("Enter the correspondent number to the filter/effect you want to apply and select 0 when you want to quit:\n1. Gray Scale\n2. Blur\n3. Yellow Filter\n4. Increase Brightness\n5. Decrease Brightness\n6. Transparency\n7. Minimize\n0. Quit")
  
  with Image.open(image) as img:
    img.save('edited_profile.png')

  while True:
      user = input()
      if user.isalpha():
        print("Sorry, that is not an option. Prease try again")
      elif int(user) > 8 or int(user) < 0:
        print("Sorry, that is not an option. Prease try again")

      if int(user) == 1:
        apply_grayscale(img)
      
      if int(user) == 2:
        apply_blur(img)
      
      if int(user) == 3:
        apply_yellow_filter(img)
      
      if int(user) == 4:
        while True:
          num = input("Enter percentage of brightness: \n")
          if user.isalpha():
            print("Invalid answer. Try again.")
          elif int(user) <= 100 or int(user) >= 0:
            increase_brightness(image, num)
          else:
            print("Invalid answer. try again.\n")
      if int(user) == 5:
        while True:
          num = input("Enter percentage of darkness: \n")
          if int(user) <= 100 or int(user) >= 0 and not user.isalpha():
            decrease_brightness(Img, num)
          else:
            print("Invalid answer. try again.\n")
      if int(user) == 6:
        while True:
          num = input("Enter percentage of transparency: \n")
          if int(user) <= 100 or int(user) >= 0 and not user.isalpha():
            apply_transparency(img, num)
          else:
            print("Invalid answer. try again.\n")
      if int(user) == 7:
        half_size(img)
      
      if int(user) == 0:
        print("Here is your photo. Thank you!\n")
        plt.imshow("edited_profile.png")
        plt.axis('off')
        plt.show()      
        break
      

apply_filter('profile.png')