import turtle
import time
import random

delay = 0.1

# score
score = 0


# Score
score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game: Made by Abhinav Utkarsh")
window.bgcolor("light blue")
window.setup(width=625, height=625)
window.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# pen tools

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Happiness Rating: 0", align="center", font=("avenir next", 26, "normal"))


# Functions
def go_up():
    if head.direction != "dowindow":
        head.direction = "up"


def go_dowindow():
    if head.direction != "up":
        head.direction = "dowindow"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "dowindow":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_dowindow, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")


# Main game loop
while True:
    window.update()

    # check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() < -290
        or head.ycor() > 290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction("stop")

        # hide segs
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(
            "Happiness Rating: {}".format(score),
            align="center",
            font=("avenir next", 26, "normal"),
        )
    # colision check
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add a seg
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("circle")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)

        # make it fast speed
        delay -= 0.001

        # inc. the score
        pen.clear()
        score += 10
        pen.write(
            "Happiness Rating: {}".format(score),
            align="center",
            font=("avenir next", 26, "normal"),
        )
    # move the back segs
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    # move seg behind the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            # reset the score
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(
                "Happiness Rating: {}".format(score),
                align="center",
                font=("avenir next", 26, "normal"),
            )
    time.sleep(delay)

window.mainloop()
