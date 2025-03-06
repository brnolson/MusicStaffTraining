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
t.write("Welcome to the Grand Staff Training Tool!", False, align="center", font=("Lato", 16, "bold"))
t.goto(0, 200)
t.write("Input the note letter that you see displayed on the staff.", False, align="center", font=("Lato", 12, "normal"))
t.goto(0, -275)
t.write("\u00A92021-Present Brenen Olson. All Rights Reserved.", False, align="center", font=("Lato", 8, "normal"))

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
score = 0

# main event loop
for i in range(5):
    # move to new position
    note = r.choice(list(notePositions.keys()))
    t.goto(-105 + i * 70, notePositions[note]-noteRadius)

    # draw ledger lines when needed
    if note == "C4-" or note == "C4+" or note == "E2" or note == "A6":
        # find center of note
        t.left(90)
        t.forward(noteRadius)
        t.right(90)

        # draw line
        t.pendown()
        t.color("black")
        t.forward(20)
        t.backward(40)
        t.color("blue")
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
    notesAvailable = ["A", "B", "C", "D", "E", "F", "G"]
    attempts = 0
    title = f"Attempt 1"
    message = f"Notes Remaining:\n{notesAvailable}:"

    # give three attempts to answer correctly
    while attempts != 3:
        userInput = t.textinput(title, message)

        # ensure only valid input is stripped and uppercased
        if userInput is None:
            break
        else:
            userInput= userInput.strip().upper()

            if userInput in notesAvailable:
                notesAvailable.remove(userInput)
                message = f"Notes Remaining:\n{notesAvailable}:"
            else: 
                message = f"Only in put Letters From:\n{notesAvailable}:"
                # skip rest of loop to give unlimited syntax attempts
                continue
        
        # add adjusted score if correct
        if userInput == note[0]:
            score += (1 * (0.5 ** attempts))
            break 

        # handle attempts
        attempts += 1
        title = f"{3 - attempts} Attempts Remaining"

    # handle no user input
    if userInput is None:
        continue

# write out final score
t.goto(0, -200)
t.color("red")
t.write(f"FINAL SCORE: {score} / 5", False, align="center", font=("Lato", 18, "bold"))

# end game messages
if score < 2.5:
    endMessage = "Keep Practicing!"
elif 2.5 <= score < 4:
    endMessage = "You're Learning Fast!"
elif 4 <= score < 5:
    endMessage = "You're Almost There!"
else:
    endMessage = "Perfect!"
t.goto(0, -222)
t.write(endMessage, False, align="center", font=("Lato", 12, "italic"))

# print end game results to console
print(f"\n----------------------\nFINAL SCORE: {score} / 5\n{endMessage}\n----------------------\n")

# # USE FOR DEBUGGING COORDINATES
# def click(x, y):
#     print("Mouse click at:", x, y)
# screen.onscreenclick(click, 1)
# t.done()

t.exitonclick()