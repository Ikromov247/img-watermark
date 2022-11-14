from PIL import Image, ImageDraw, ImageFont, ImageOps
 
#read the image
img = Image.open("example.jpg")
#get image size
width, height = img.size
#read a font in ttf format
font = ImageFont.truetype('example.ttf', 30)
#create an editable image
draw = ImageDraw.Draw(img)
#add 7 watermarks
for i in range(1,7):
    cors = (width*0.15*i, height*0.15*i)
    draw.text(cors, "Watermark", (240,240,237),font)

#show the resulting image. 
img.show()
#img.save("result.jpg")
#to save the image