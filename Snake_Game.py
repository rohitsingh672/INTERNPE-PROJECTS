import turtle, time, random
# Setup
win = turtle.Screen()
win.title("Mini Snake 🐍")
win.bgcolor("black")
win.setup(600, 600)
win.tracer(0)
# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"  # Snake is stopped at start
# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
segments = []
score = 0
# Movement
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "stop":
        return  # Don't move until a key is pressed
    x, y = head.xcor(), head.ycor()
    if head.direction == "up":
        head.sety(y + 20)
    if head.direction == "down":
        head.sety(y - 20)
    if head.direction == "left":
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(x + 20)
# Keyboard bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")
# Game loop
while True:
    win.update()
    # Wall collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0
    # Eat food
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        seg = turtle.Turtle()
        seg.shape("square")
        seg.color("lightgreen")
        seg.penup()
        segments.append(seg)
        score += 10
        print("Score:", score)
    # Move body
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    move()
    # Self collision
    for seg in segments:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
    time.sleep(0.1)
