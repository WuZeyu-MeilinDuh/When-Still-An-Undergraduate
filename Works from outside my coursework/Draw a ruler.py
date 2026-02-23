def draw_line(tick_len, tick_label = ""):
    line = "-" * tick_len
    if tick_len:
        line += " " + tick_label
    print(line)

def draw_interval(centre_len):
    if centre_len > 0:
        draw_interval(centre_len - 1)
        draw_line(centre_len)
        draw_interval(centre_len - 1)

def draw_ruler(num_inch, major_len):
    draw_line(major_len, "0")

    for j in range(1, 1 + num_inch):
        draw_interval(major_len - 1)
        draw_line(major_len, str(j))

draw_ruler(3, 3)