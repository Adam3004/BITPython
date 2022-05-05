from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    width, height = image.size
    pixels = list(image.getdata())
    image = [pixels[i:i + width] for i in range(0, len(pixels), width)]

    return image


def save_image(filename, image):
    flat_image = [item for sublist in image for item in sublist]
    height, width = len(image), len(image[0])
    image_out = Image.new("L", (width, height))
    image_out.putdata(flat_image)
    image_out.save(filename)


def color_to_grey(image):
    for row in image:
        for i in range(len(row)):
            row[i] = colour_changer(row[i], True)

    return image


def colour_changer(rgb: tuple, average=True):
    if average:
        greyScale = sum(rgb) / 3
    else:
        greyScale = (0.3 * rgb[0]) + (0.59 * rgb[1]) + (0.11 * rgb[2])

    return greyScale


if __name__ == "__main__":
    in_file = "img1.jpg"
    out_file = "img1Black.jpg"
    image = load_image(in_file)
    image = color_to_grey(image)
    save_image(out_file, image)
