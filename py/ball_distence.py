def ball_distence():
    import math
    x = 0
    y = 0
    x_speed = 0.01
    y_speed = 0.02
    while True:
        x += x_speed
        y += y_speed
        if y - 0.5 < 0: 
            y_speed *= -1
            y_speed -= 0.01
            y += y_speed
            