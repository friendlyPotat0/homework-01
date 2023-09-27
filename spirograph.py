import turtle

def draw_star_polygon(carl, length, points, offset):
    carl.color("#fba572")
    carl.penup()
    carl.goto(- (length / 2), offset)
    carl.pendown()

    angle = 180 - (360 / points)
    for _ in range(0, points):
        carl.forward(length)
        carl.left(angle)

def draw_tree_pattern(carl, branch_length, angle, depth):
    if depth == 0:
        return
    else:
        carl.forward(branch_length)
        carl.right(angle)
        draw_tree_pattern(carl, branch_length * 0.7, angle, depth - 1)
        carl.left(angle * 2)
        draw_tree_pattern(carl, branch_length * 0.7, angle, depth - 1)
        carl.right(angle)
        carl.backward(branch_length)

def draw_radial_tree_pattern(carl, branch_length, branches, angle, depth):
    carl.color("#444250")
    carl.penup()
    carl.goto(0, 0)
    carl.pendown()

    for _ in range(branches):
        draw_tree_pattern(carl, branch_length, angle, depth)
        carl.right(360 / branches)

def main():
    carl = turtle.Turtle()
    carl.getscreen().bgcolor("#f9e4e1")
    carl.hideturtle()
    carl.width(2)
    carl.speed(0)

    draw_star_polygon(carl, 500, 36, -20)
    draw_radial_tree_pattern(carl, 100, 12, 30, 5)

    turtle.done()

if __name__ == "__main__":
    main()
