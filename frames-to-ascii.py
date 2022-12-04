import pathlib
import PIL
from PIL import Image

for i in range(1, 6577, 1):
    print(i)
    path = 'badAppleFrames/img' + '{:d}'.format(i).zfill(4) + '.jpeg'
    image = PIL.Image.open(path)

    USED_CHARS = ["@", "#", "S", "%", "X", "?", "*", "+", ";", ":", ",", ".", " "]

    new_height = int(150)
    new_width = int(new_height * image.width / image.height)

    chara: str = ''.join(USED_CHARS[int(pixel // 19.7)] for pixel in
                         image.resize((int(new_width), int(new_height))).convert("L").getdata())

    ascii_image = "\n".join([chara[index:(index + new_width)] for index in range(0, len(chara), new_width)])

    prefix = pathlib.PurePath(path).stem
    with open(f"converted/ascii_{prefix}.txt", "w") as f:
        f.write(ascii_image)
