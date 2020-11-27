import turtle
from Turkey import Turkey
from PIL import Image, ImageDraw


def set_background(filename):
    try:
        image = Image.open(filename)
    except FileNotFoundError:
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)


def draw_lane_markers(num_turkeys):
    lane_maker = turtle.Turtle()
    lane_maker.hideturtle()
    lane_maker.shape(None)
    lane_maker.penup()
    lane_maker.speed(0)
    lane_maker.fillcolor('black')

    for i in range(num_turkeys):
        start_height = -(HEIGHT / 2)
        height = start_height + (i * (HEIGHT / num_turkeys))
        lane_maker.goto(-(WIDTH / 2), height)
        lane_maker.setheading(0)
        lane_maker.begin_fill()
        for k in range(2):
            lane_maker.forward(WIDTH)
            lane_maker.left(90)
            lane_maker.forward(10)
            lane_maker.left(90)
        lane_maker.end_fill()

# ===================== DO NOT EDIT THE CODE ABOVE ============================


if __name__ == '__main__':
    game_over = False
    WIDTH = 1150
    HEIGHT = 600

    # 1. Set the window variable to turtle.Screen()
    window = turtle.Screen()
    # 2. Call the window's setup() method with the WIDTH and HEIGHT variables
    window.setup(WIDTH, HEIGHT)
    # 3. Call the set_background() method with 'grass.png'
    set_background('grass.png')
    # 4. Run your code. You should see a window with an image of grass
    # 5. Set the Turkey.window variable to the window variable created in step 1
    # Turkey.window = window
    Turkey.window = window
    # 6. Create and set a variable to hold the number of Turkeys you want
    # in the race from 2 to 7
    numberofTurkeys = 7
    # 5. Call the draw_lane_markers function and pass in the number of turkeys
    draw_lane_markers(numberofTurkeys)
    # 6. Create and set a variable to hold the width of each lane
    # *HINT* the lane width is the HEIGHT of the window divided by the number of
    #        turkeys in the race
    lanewidth = HEIGHT/numberofTurkeys
    # 7. Create a variable called start_x and set it to -(WIDTH / 2)
    start_x = -(WIDTH / 2)
    # 8. Create a variable called start_y and set it to (HEIGHT / 2)
    start_y = (HEIGHT / 2)
    # 9. Create your turkey competitors!
    # gobbler = Turkey(start_x, start_y - (1 * lane_width))
    #
    # *HINT* the (1 * lane_width) part will be different for each turkey
    fred = Turkey(start_x, start_y - (0 * lanewidth), "fred")
    bob = Turkey(start_x, start_y - (1 * lanewidth), "bob")
    lisa = Turkey(start_x, start_y - (2 * lanewidth), "lisa")
    annie = Turkey(start_x, start_y - (3 * lanewidth), "annie")
    leo = Turkey(start_x, start_y - (4 * lanewidth), "leo")
    sam = Turkey(start_x, start_y - (5 * lanewidth), "sam")
    willow = Turkey(start_x, start_y - (6 * lanewidth), "willow")

    while not  game_over:
        pass

        # 10. Call the trot() method for each one of your turkeys!
        fred.trot()
        bob.trot()
        lisa.trot()
        annie.trot()
        leo.trot()
        sam.trot()
        willow.trot()
        # 11. For each turkey, use an 'if' statement and call your turkey's
        # check_finish() method
        # if gobbler.check_finish():
        if sam.check_finish():
            sam.winner()
            game_over=True

        if bob.check_finish():
            bob.winner()
            game_over = True

        if lisa.check_finish():
            lisa.winner()
            game_over = True

        if annie.check_finish():
            annie.winner()
            game_over = True

        if fred.check_finish():
            fred.winner()
            game_over = True

        if leo.check_finish():
            leo.winner()
            game_over = True

        if willow.check_finish():
            willow.winner()
            game_over = True
            # 12. If the turkey finished, call that turkey's winner() method,
            # gobbler.winner()

            # 13. set the game_over variable to True


# ===================== DO NOT EDIT THE CODE BELOW ============================

    turtle.done()
