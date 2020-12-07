def color_rgb(color):
    color_dict = {'red': (255, 0, 0),
                  'black': (0, 0, 0),
                  'white': (255, 255, 255)}
    color_code = color_dict[color]
    return color_code