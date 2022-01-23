import math

def rotate(char_pos, mouse_pos):
    spin = 0
    if (char_pos[0] > mouse_pos[0]):
        spin = 180
    xdiff = (char_pos[0] - mouse_pos[0])
    ydiff = -(char_pos[1] - mouse_pos[1])
    if ydiff == 0:
        ydiff = 0.01
    if xdiff == 0:
        xdiff = 0.001
    ans = math.degrees(math.atan((ydiff/xdiff)))
    return (ans - spin)

# rotate(0, 0, (100, 100))