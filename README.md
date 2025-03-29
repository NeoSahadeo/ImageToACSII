# Python image to ASCII

A very simple Python script that converts an inputed image into it's ASCII output based on brightness.
## Screenshots

*image from [mayebassett](https://mayebassett.blogspot.com/2022/11/can-wild-cat-be-domesticated.html)*

![Before](https://github.com/NeoSahadeo/ImageToACSII/blob/main/screenshots/NationalGeographic_2572187_square-1117243537.jpg?raw=true)

![After](https://github.com/NeoSahadeo/ImageToACSII/blob/main/screenshots/After.png?raw=true)



## Documentation

The main file is `main.py`.

Make sure to install [Pillow](https://pillow.readthedocs.io/en/stable/)

`pip install -r requirements.txt`

**General Command**

`python main.py imagePath [SCALE]`

---

Run `python main.py --help` for help.

```
usage: ASCII Image Generator [-h] [--scale SCALE] imagePath

positional arguments:
  imagePath      The path to the image

options:
  -h, --help     show this help message and exit
  --scale SCALE  Resize-Scale for the image (Default: 1)
```
## Authors

- [@NeoSahadeo](https://www.github.com/NeoSahadeo)


## Contributing

Contributions are always welcome!

Features that would be nice:

* [ ] Edge Detection
* [ ] Coloured outputs
* [ ] Ability to apply transformations
