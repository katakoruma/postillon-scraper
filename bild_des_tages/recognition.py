#%%'
import pytesseract, os, json, shutil, re, textwrap
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from matplotlib import pyplot as plt
 
path_source = 'pictures'
path_final = 'pictures_export'
#%%'

elements = os.listdir(path_source)

for file in elements:
    source = f'{path_source}/{file}'
 
    img = Image.open(source)

    # Initialize drawing context
    draw = ImageDraw.Draw(img)

    #%%

    custom_config = r'--oem 3 --psm 6'

    numpydata = np.asarray(img)[865::,300::,:]
    text = pytesseract.image_to_string(numpydata, config=custom_config, lang='deu')

    first_n = text.find('\n')
    text = text[first_n::]

    text = text.replace('|', '').replace('\n',' ')

    text = re.sub(r'\s+', ' ', text)

    hyphen_pos = text.find('- ')

    if hyphen_pos != -1:
        if text[hyphen_pos + 2].islower() and not text[hyphen_pos - 1].isdigit():
            text = text.replace('- ','')
        else:
            text = text.replace('- ','-')

    print(text)



    #%%


    position_square = (0, 865)  # Position where text will be placed (x, y)
    square_size = (2000, 500)  # Size of the black square

    layer_d = 2

    # Draw black square
    #square_x, square_y = position[0] + text_width + 10, position[1]  # Adjust position relative to text
    #draw.rectangle([square_x, square_y, square_x + square_size[0], square_y + square_size[1]], fill="black")

    # Create gradient
    for i in range(int(square_size[1]/layer_d)):
        gradient_opacity = 40 + int(10 * (i / square_size[1] * layer_d))  # Opacity increases from 0 to 255
        gradient_rect = [(position_square[0], position_square[1] + i * layer_d),  # Top left corner
                            (position_square[0] + square_size[0], position_square[1] + (i + 1) * layer_d)]  # Bottom right corner
        gradient_color = (gradient_opacity, gradient_opacity, gradient_opacity)  # Black color with variable opacity
        draw.rectangle(gradient_rect, fill=gradient_color)



    #%%
        
    position_text = [770,870]
    h = 70

    font_size = 60 
    text_width = 50


    position_text = [770,850]
    h = 75

    font_size = 67 
    text_width = 44


    # Load font
    #font = ImageFont.truetype("Python_encrypted/postillon_newsticker_crawler/bild_des_tages/Arial.ttf", font_size)
    font = ImageFont.truetype("/Volumes/Secomba/leon/Boxcryptor/sciebo/code/Python_encrypted/postillon_newsticker_crawler/bild_des_tages/Comic_Sans_MS.ttf", font_size)


    # Draw text on image
    wrapped_text = textwrap.wrap(text, width=text_width)
    #draw.text((text_x, text_y), wrapped_text, font=font, fill=font_color)

    position_text[1] += (5-len(wrapped_text)) * h/2

    for line in wrapped_text:
        w = draw.textlength(line, font=font)
        draw.text((position_text[0] + (text_width - w) / 2, position_text[1]), line, font=font)
        position_text[1] += h


    #%%'
        
    img.save(f'{path_final}/{file}')
