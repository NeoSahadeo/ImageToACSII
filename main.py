import sys
from PIL import Image
import argparse
import pathlib


def main():
    im = Image.open(PATH)

    width, height = im.size
    im = im.resize((round(width * SIZE_SCALE), round(height * SIZE_SCALE)))

    width, height = im.size
    im = im.rotate(270)

    image_list = []

    for x in range(0, width):
        row = []
        for y in range(0, height):
            px = im.getpixel((x, y))
            if px:
                r = px[0]
                g = px[1]
                b = px[2]
                # r, g, b, a = px
                total = (r + g + b)
                if total > 764:
                    row.append(ASCII_VALUES[0])
                elif total > 637:
                    row.append(ASCII_VALUES[1])
                elif total > 510:
                    row.append(ASCII_VALUES[2])
                elif total > 382:
                    row.append(ASCII_VALUES[3])
                elif total > 255:
                    row.append(ASCII_VALUES[4])
                elif total > 127:
                    row.append(ASCII_VALUES[5])
                else:
                    row.append(ASCII_VALUES[6])
        image_list.append(row)

    image_list = reversed(image_list)
    for x in image_list:
        for y in x:
            print(y, end="")
        print()


if __name__ == "__main__":
    BACKGROUND = "  "
    ASCII_VALUES = [
        f"#{BACKGROUND}",
        f"@{BACKGROUND}",
        f"O{BACKGROUND}",
        f"p{BACKGROUND}",
        f"){BACKGROUND}",
        f"-{BACKGROUND}",
        f".{BACKGROUND}",
    ]

    parser = argparse.ArgumentParser(prog="ASCII Image Generator")
    parser.add_argument("imagePath", help="The path to the image")
    parser.add_argument("--scale", help="Resize-Scale for the image (Default: 1)")
    args = parser.parse_args()

    SIZE_SCALE = 1
    if args.scale:
        SIZE_SCALE = float(args.scale)

    PATH = pathlib.Path(args.imagePath)

    main()
