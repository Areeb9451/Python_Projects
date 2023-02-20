from PIL import Image, ImageChops
img1, img2 = Image.open('1.jpg.jpg'), Image.open('2.jpg.jpg')
diff = ImageChops.difference(img1, img2)

if diff.getbbox():
    diff.show()


 