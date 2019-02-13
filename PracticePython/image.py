from PIL import Image, ImageDraw, ImageFont

test = Image.open('头像.jpeg')
draw = ImageDraw.Draw(test)
ft = ImageFont.truetype('simhei.ttf', 30)
draw.text((test.size[0] * 0.8, 0), 'test', font=ft, fill='red')
test.show()