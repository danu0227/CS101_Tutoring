from cs1media import *


# NEGATIVE IMG
def negative_img(target, file_type):
    img = load_picture(target + file_type)
    w, h = img.size()
    negative = create_picture(w, h, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            r, g, b = 255 - r, 255 - g, 255 - b
            negative.set(x, y, (r, g, b))
    negative.show()
    negative.save_as(target + "_negative" + file_type)


# GRAYSCALE_IMG
# Grayscale formula = 0.3*R + 0.59*G + 0.11*B
def grayscale_img(target, file_type):
    img = load_picture(target + file_type)
    w, h = img.size()
    gray = create_picture(w, h, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            grayscale = int(((0.3 * r) + (0.59 * g) + (0.11 * b)))
            r, g, b = grayscale, grayscale, grayscale
            gray.set(x, y, (r, g, b))
    gray.show()
    gray.save_as(target + "_gray" + file_type)


# MOSAIC_IMG
def avgrgb(image, ps, w, h):
    r, g, b = 0, 0, 0
    size = ps ** 2
    for x in range(w * ps, (w + 1) * ps):
        for y in range(h * ps, (h + 1) * ps):
            col = image.get(x, y)
            r += col[0]
            g += col[1]
            b += col[2]
    return r // size, g // size, b // size


def setpix(image, ps, w, h, rgb):
    for x in range(w * ps, (w + 1) * ps):
        for y in range(h * ps, (h + 1) * ps):
            image.set(x, y, rgb)


def mosaic_img(target, file_type, ps):
    img = load_picture(target + file_type)
    w, h = img.size()
    mosaic = create_picture(w // ps * ps, h // ps * ps, (0, 0, 0))
    for i in range(w // ps):
        for j in range(h // ps):
            col = avgrgb(img, ps, i, j)
            setpix(mosaic, ps, i, j, col)
    mosaic.show()
    mosaic.save_as(target + "_mosaic" + file_type)


# BLUR_IMG
# average the 5*5 box containing the target point at the center.
def blur_img(target, file_type):
    img = load_picture(target + file_type)
    w, h = img.size()
    blur = create_picture(w, h, (0, 0, 0))
    for i in range(w):
        for j in range(h):
            if i < 2 or i > w - 3 or j < 2 or j > h - 3:
                blur.set(i, j, img.get(i, j))
            else:
                R, G, B = (0, 0, 0)
                for k in range(-2, 3):
                    for l in range(-2, 3):
                        r, g, b = img.get(i + k, j + l)
                        R += 1.0 / 25.0 * r
                        G += 1.0 / 25.0 * g
                        B += 1.0 / 25.0 * b
                R = int(R)
                G = int(G)
                B = int(B)
                blur.set(i, j, (R, G, B))
    blur.show()
    blur.save_as(target + "_blur" + file_type)


blue = (19, 81, 207)
img = create_picture(200, 200, blue)
img.set_title("BLUE!!")

img.show()
target = "./photos/cat1"
file_type = ".jpg"

# ORIGINAL IMG
img1 = load_picture(target + file_type)
img1.show()

# Generate files
negative_img(target, file_type)
grayscale_img(target, file_type)
mosaic_img(target, file_type, 10)
blur_img(target, file_type)

target = "./photos/cat2"
file_type = ".jpg"

# ORIGINAL IMG
img1 = load_picture(target + file_type)
img1.show()

# Generate files
negative_img(target, file_type)
grayscale_img(target, file_type)
mosaic_img(target, file_type, 10)
blur_img(target, file_type)
