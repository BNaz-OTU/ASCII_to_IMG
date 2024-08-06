from PIL import Image, ImageDraw, ImageFont

import math

charSet1 = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]
charSet2 = '#Wo- '[::-1]

oneCharWidth = 8
oneCharHeight = 18

print('--------------------------------------------------------------------------------')
print('This Python file produces both a .txt file and .png file of the users desired image into ASCII characters.\n\nPlease ensure that the image is within the same directory as the Python file')
print('--------------------------------------------------------------------------------')

print('Please enter the filename: ')
filename = input()
print('----------------------------------------')

print('Please enter the scale (0 - 1): ')
scale = input()
print('----------------------------------------')

print(
    f'''Please pick between charSet1 or charSet2 for the conversion (1 or 2):\n\ncharSet1: " {charSet1} "\n\ncharSet2: " {charSet2} "\n''')
setId = input()
print('----------------------------------------')

print('Please enter the name of the newly generated PNG file (Do not include .png): ')
saveName = input()
print('----------------------------------------')


def convertToASCII(filename, scale, setId, saveName):

    if (setId == '1'):
        charArray = list(charSet1)

    else:
        charArray = list(charSet2)

    charLength = len(charArray)
    interval = charLength/256

    def getChar(inputInt):
        return charArray[math.floor(inputInt * interval)]

    text_file = open("Output.txt", "w")
    ScaleFactor = float(scale)

    holderImg = Image.open(filename)

    fnt = ImageFont.truetype("Keyboard.ttf", 15)

    width, height = holderImg.size
    print(f'OG Image size: {width} x {height} | Ratio: {height/width}')
    holderImg = holderImg.resize(
        (int(ScaleFactor * width), int(ScaleFactor * height * (oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = holderImg.size
    pix = holderImg.load()

    outputImage = Image.new(
        'RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))

    twidth, theight = outputImage.size
    print(f'New Image size: {twidth} x {theight} | Ratio: {theight/twidth}')

    d = ImageDraw.Draw(outputImage)

    for i in range(height):
        for j in range(width):
            red, green, blue = pix[j, i]
            h = int(red/3 + green/3 + blue/3)
            pix[j, i] = (h, h, h)
            text_file.write(getChar(h))
            d.text((j * oneCharWidth, i * oneCharHeight),
                   getChar(h), font=fnt, fill=(red, green, blue))
        text_file.write('\n')

    outputImage.save(saveName + ".png")
    print('Image has successfully been converted to the ASCII image. New image should be within your current directory.')


convertToASCII(filename, scale, setId, saveName)
