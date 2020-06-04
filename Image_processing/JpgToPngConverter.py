import sys
import os

from PIL import Image

#grab first and second argument
image_folder=sys.argv[1]
output_folder=sys.argv[2]

#check if output folder exist if not create

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

#loop through image_folder 

for filename in os.listdir(image_folder):
	img=Image.open(f'{image_folder}{filename}')
	#convert images into png
	clean_name=os.path.splitext(filename)[0]
	#print(clean_name)

	#save to ouput_folder
	img.save(f'{output_folder}{clean_name}.png')
	print('all set!')