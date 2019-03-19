from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    return chr(random.randint(64, 95))
    pass


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))
    pass


def rndColorForChar():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


width = 240
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 36)

draw = ImageDraw.Draw(image)

for i in range(width):
    for j in range(height):
        draw.point((i, j), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColorForChar())

image = image.filter(ImageFilter.BLUR)
image.show()
