import os
from flask import Flask, redirect, url_for, render_template, request
import mercantile
import requests
import shutil
import PIL
import math
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from os import listdir, mkdir, rmdir
from os.path import isfile, join
from PIL import Image
from geopy.geocoders import Nominatim
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/predict/<float(signed=True):lat>/<float(signed=True):longi>',methods=['GET','POST']) #/', methods=['POST', 'GET']) 

def predict(lat,longi):
#  lat = 28.5370703
#  longi = 77.2618051
  lat_lng = [lat, longi]
  delta = 0.01
  tl = [lat_lng[0] + delta, lat_lng[1] - delta]
  br = [lat_lng[0] - delta, lat_lng[1] + delta]
  z = 16  # Set the resolution
  tl_tiles = mercantile.tile(tl[1], tl[0], z)
  br_tiles = mercantile.tile(br[1], br[0], z)
  
  x_tile_range = [tl_tiles.x, br_tiles.x];
  print(x_tile_range)
  y_tile_range = [tl_tiles.y, br_tiles.y];
  print(y_tile_range)
  x_y_tile=[x_tile_range,y_tile_range]
  
  try:
    mkdir('static')
  except FileExistsError:
    shutil.rmtree('static')
    mkdir('static')

  try: 
   os.remove("./static/crop.png")
  except: pass

  #for file in os.listdir('./static'):
  #  if file.endswith('.png'):
  #      os.remove(file)

  try:
    mkdir('sat_images')
  except FileExistsError:
    shutil.rmtree('sat_images')
    mkdir('sat_images')
    
  try:
    mkdir('elevation_images')
  except FileExistsError:
    shutil.rmtree('elevation_images')
    mkdir('elevation_images')
  
  for i,x in enumerate(range(x_tile_range[0],x_tile_range[1]+1)):
    for j,y in enumerate(range(y_tile_range[0],y_tile_range[1]+1)):
        print(x,y)
        r = requests.get('https://api.mapbox.com/v4/mapbox.terrain-rgb/'+str(z)+'/'+str(x)+'/'+str(y)+'@2x.pngraw?access_token=pk.eyJ1Ijoia2FwYXN0b3IiLCJhIjoiY2p3eTg3eWJoMG1jZjQ4bzZmcGg5c3F3cSJ9.vhyCyD9xDDGP9EQnhB9xtA', stream=True)
        if r.status_code == 200:
            with open('./elevation_images/' + str(i) + '.' + str(j) + '.png', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)  
        
        r = requests.get('https://api.mapbox.com/v4/mapbox.satellite/'+str(z)+'/'+str(x)+'/'+str(y)+'@2x.png?access_token=pk.eyJ1Ijoia2FwYXN0b3IiLCJhIjoiY2p3eTg3eWJoMG1jZjQ4bzZmcGg5c3F3cSJ9.vhyCyD9xDDGP9EQnhB9xtA', stream=True)
        if r.status_code == 200:
            with open('./sat_images/' + str(i) + '.' + str(j) + '.png', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

  try:
    mkdir('composite_images')
  except FileExistsError:
    shutil.rmtree('composite_images')
    mkdir('composite_images')

  try:
    mkdir('animate')
  except FileExistsError:
    shutil.rmtree('animate')
    mkdir('animate')
  
  for img_name in ['elevation','sat']:
    image_files = ['./'+img_name+'_images/' + f for f in listdir('./'+img_name+'_images/')]
    images = [PIL.Image.open(x) for x in image_files]

    edge_length_x = x_tile_range[1] - x_tile_range[0]
    edge_length_y = y_tile_range[1] - y_tile_range[0]
    edge_length_x = max(1,edge_length_x)
    edge_length_y = max(1,edge_length_y)
    width, height = images[0].size

    total_width = width*edge_length_x
    total_height = height*edge_length_y

    composite = PIL.Image.new('RGB', (total_width, total_height))
    print(total_width,total_height)

    anim_idx = 0
    y_offset = 0
    for i in range(0,edge_length_x):
        x_offset = 0
        for j in range(0,edge_length_y):
            tmp_img = PIL.Image.open('./'+img_name+'_images/' + str(i) + '.' + str(j) + '.png')
            composite.paste(tmp_img, (y_offset,x_offset))
            x_offset += width
            composite.save('./animate/'+str(anim_idx).zfill(4)+'.jpg',optimize=True,quality=95)
            anim_idx += 1
            print(anim_idx)

            
        y_offset += height

    composite.save('./composite_images/'+img_name+'.png')

  # source = cv2.imread("composite_images/sat.png", 1)
  im = Image.open('composite_images/sat.png')
  cropped = im.crop((70, 80, 1000, 1000))
  # cropped.show()
  cropped.save('./static/crop.png')

    # Cropped Image
    # crop = source[70:1000, 80:1000]

    # Displaying all the images
    # cv2.imshow("Crop", crop)

    # k = cv2.waitKey(0)
    # if k == ord('s'):
    #    cv2.imwrite("crop.png", crop)

    # close all open windows
    # cv2.destroyAllWindows()

  img = cv2.imread("./static/crop.png")
  grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.figure(figsize=(20, 20))
    # plt.imshow(grid_RGB)  # Printing the original picture after converting to RGB

  grid_HSV = cv2.cvtColor(grid_RGB, cv2.COLOR_RGB2HSV)  # Converting to HSV
  lower_green = np.array([25, 52, 52])
  upper_green = np.array([102, 255, 255])

  mask = cv2.inRange(grid_HSV, lower_green, upper_green)
  res = cv2.bitwise_and(img, img, mask=mask)  # Generating image with the green part

  green_perc = (np.sum(mask) / np.size(mask)) / 255
  green_perc
  gp = 100 * green_perc

    # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray Image", gray_img)
    # cv2.waitKey(0)

    # shutil.rmtree('sat_images', ignore_errors=True)
    # shutil.rmtree('elevation_images', ignore_errors=True)
    # shutil.rmtree('composite_images', ignore_errors=True)
    # shutil.rmtree('animate', ignore_errors=True)

  return render_template('open.html',x_y_tile=x_y_tile,green_percentage=gp, lower_green=lower_green, upper_green=upper_green, lat_lng=lat_lng) #{'green_index': gp} # 'location': 'Kalkaji'} render_template('index.html', green_percentage=gp)

    #app.add_url_rule('/index/<lat,longi>','index',index)

if __name__ == "__main__":
     app.run(port=8080)