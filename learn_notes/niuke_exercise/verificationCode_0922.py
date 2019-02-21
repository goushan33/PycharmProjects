from PIL import Image, ImageDraw, ImageFont, ImageFilter#Image这些都是PIL的模块

import random

# 产生随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 产生随机颜色1:
#用64-255的整数表示RGB三色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:表示宽度为240个像素点，高度为60个像素点
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
#直接用arial.ttf文件，会报错。IOError: cannot open resource。因为PIL无法定位到字体文件的位置。
font = ImageFont.truetype(r'C:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_10.0.17134.1_none_5803fc87168579d6\arial.ttf', 36)

# 创建Draw对象:
draw = ImageDraw.Draw(image)

# 填充每个像素：背景颜色随机
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')