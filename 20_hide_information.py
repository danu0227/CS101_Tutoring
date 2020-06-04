from cs1media import *


# GRAYSCALE_IMG
# Grayscale formula = 0.3*R + 0.59*G + 0.11*B
def grayscale_img(target):
    img = load_picture(target)
    w, h = img.size()
    gray = create_picture(w, h, (0, 0, 0))
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            grayscale = int(((0.3 * r) + (0.59 * g) + (0.11 * b)))
            r, g, b = grayscale, grayscale, grayscale
            gray.set(x, y, (r, g, b))
    gray.save_as(target.split('.')[0] + "_gray.bmp")
    return target.split('.')[0] + "_gray.bmp"


# information to r, g, b value
def info_to_rgb(num):
    r = num // 9
    g = (num - r*9) // 3
    b = num % 3
    return r, g, b


# rgb value to information
def rgb_to_info(r, g, b):
    r = r % 3
    g = g % 3
    b = b % 3
    return r * 9 + g * 3 + b

# hide information image to target image
def hide_info(target, info):
    info_gray = grayscale_img(info)
    info_img = load_picture(info_gray)
    target_img = load_picture(target)
    target_w, target_h = info_img.size()
    secret = create_picture(target_w, target_h, (0, 0, 0))
    for y in range(target_h):
        for x in range(target_w):
            r, g, b = target_img.get(x, y)
            normalize = r//3*3, g//3*3, b//3*3
            grayscale = info_img.get(x, y)[0] // 10
            hide = info_to_rgb(grayscale)
            secret.set(x, y, (normalize[0]+hide[0], normalize[1]+hide[1], normalize[2]+hide[2]))
    secret.show()
    secret.save_as("photos/hidden.bmp")

# get hidden image from target image.
def get_info(target):
    hidden_img = load_picture(target)
    w, h = hidden_img.size()
    info_img = create_picture(w, h, (0, 0, 0))
    for y in range(h):
        for x in range(h):
            r, g, b = hidden_img.get(x, y)
            info = rgb_to_info(r, g, b)
            info_img.set(x, y, (info*10, info*10, info*10))
    info_img.show()

hide_info("photos/yangdal_cat.jpg", "photos/jerry.jpg")
get_info("photos/hidden.bmp")
