import turtle as t
import random as r

# set up screen
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgpic("grandStaff.png")

# message
t.hideturtle()
t.penup()
t.speed(100)
t.goto(0, 225)
t.write("Welcome to the Grand Staff Training Tool", False, align="center", font=("Lato", 16, "bold"))
t.goto(0, 200)
t.write("Input the note letter that you see displayed on the staff", False, align="center", font=("Lato", 12, "normal"))
t.goto(0, -225)
t.write("\u00A92021-Present Brenen Olson All Rights Reserved", False, align="center", font=("Lato", 8, "normal"))
t.speed()

# store note vertical positions
notePositions = {
    "A6" : 159,
    "G5" : 149,
    "F5" : 140,
    "E5" : 131,
    "D5" : 121,
    "C5" : 111,
    "B5" : 102,
    "A5" : 92,
    "G4" : 83,
    "F4" : 73,
    "E4" : 64,
    "D4" : 54,
    "C4+" : 44,
    "C4-" : -44,
    "B4" : -54,
    "A4" : -64,
    "G3" : -73,
    "F3" : -83,
    "E3" : -92,
    "D3" : -102,
    "C3" : -111,
    "B3" : -121,
    "A3" : -131,
    "G2" : -140,
    "F2" : -149,
    "E2" : -159 
}

noteRadius = 10
t.pensize(3)

# main event loop
for i in range(5):
    # move to new position
    note = r.choice(list(notePositions.keys()))
    t.goto(-105 + i * 70, notePositions[note]-noteRadius)
    print(note)

    # draw ledger lines when needed
    if note == "C4-" or note == "C4+" or note == "E2" or note == "A6":
        # find center of note
        t.left(90)
        t.forward(noteRadius)
        t.right(90)

        # draw line
        t.pendown()
        t.forward(20)
        t.backward(40)
        t.penup()
        t.forward(20)

        # return to original position
        t.right(90)
        t.forward(noteRadius)
        t.left(90)

    # draw note
    t.pendown()
    t.begin_fill()
    t.color("blue")
    t.fillcolor("blue")
    t.circle(10)
    t.end_fill()
    t.penup()

    # draw stem
    if notePositions[note] < -105 or 0 < notePositions[note] < 105: # stem up
        # position
        t.forward(noteRadius)
        t.left(90)
        t.forward(noteRadius)

        # draw stem
        t.pendown()
        t.forward(50)
        t.penup()

        # return to original position
        t.backward(50 + noteRadius)
        t.right(90)
        t.backward(noteRadius)
    else: # stem down
        # position
        t.backward(noteRadius)
        t.right(90)
        t.backward(noteRadius)

        # draw stem
        t.pendown()
        t.forward(50)
        t.penup()

        # return to original position
        t.backward(50 - noteRadius)
        t.left(90)
        t.forward(noteRadius)

    # user interaction
    userInput = (t.textinput("Enter Your Answer", "Notes Name:")).strip().upper()
    if userInput == note[0]:
        print("Good Job")
    else:
        print("Keep Trying")


# USE FOR DEBUGGING COORDINATES
# def click(x, y):
#     print("Mouse click at:", x, y)
# screen.onscreenclick(click, 1)
# t.done()

t.exitonclick()