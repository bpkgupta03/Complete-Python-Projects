from PIL import Image,ImageFilter

img=Image.open('./Pokedox/pikachu.jpg')
#print(dir(img))
img=img.filter(ImageFilter.BLUR)
img.save('blur.png','png')


Img=img.convert('L')
Img.save('grey.png','png')
#Img.show()

crooked=img.rotate(290)
crooked.save('grey_rotate.png','png')

img2=Image.open('./Pokedox/squirtle.jpg')
resize=img2.resize((400,400))
#print(img2)
resize.save('squirtle_resize.png','png')

box=(100,100,400,500)
region=img2.crop(box)
region.save('squirtle_resize.png','png')

img3=Image.open('./astro.jpg')
#print(img3)
new_img=img3.resize((200,400))
new_img.save('astro_resize.jpg')

th=(200,200)
img3.thumbnail(th)
img3.save('./thumbnail.png')
img3.show()

