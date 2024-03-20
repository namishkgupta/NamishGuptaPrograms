from cmu_graphics import *
app.background = 'white'
app.stepsPerSecond = 60





# board and lines
board = Group(
Rect(0, 0, 400, 400, fill='paleGreen'),
Circle(200, 10, 40, fill=None, border='fireBrick', borderWidth=3),
Circle(200, 390, 40, fill=None, border='cornflowerBlue', borderWidth=3),
Rect(200, 5, 90, 10, fill=app.background, align='center'),
Rect(200, 395, 90, 10, fill=app.background, align='center'),
Line(50, 85, 350, 85, fill='fireBrick'),
Line(50, 305, 350, 305, fill='cornflowerBlue'),
Line(50, 200, 350, 200, fill='azure', dashes=True),
Circle(200, 200, 25, fill='lightGreen', border='azure'),
Circle(200, 200, 3, fill='azure')
)


# border

border = Group(
Circle(60, 20, 10, fill=None, border='white', borderWidth=5),
Circle(340, 20, 10, fill=None, border='white', borderWidth=5),
Circle(60, 380, 10, fill=None, border='white', borderWidth=5),
Circle(340, 380, 10, fill=None, border='white', borderWidth=5),
Circle(65, 25, 13, fill='paleGreen'),
Circle(335, 25, 13, fill='paleGreen'),
Circle(65, 375, 13, fill='paleGreen'),
Circle(335, 375, 13, fill='paleGreen'),
Line(60, 10, 340, 10, fill='white', lineWidth=5),
Line(50, 20, 50, 380, fill='white', lineWidth=5),
Line(350, 20, 350, 380, fill='white', lineWidth=5),
Line(60, 390, 340, 390, fill='white', lineWidth=5)
)


for x1 in range(155,246,5):
    Line(x1, 0, x1 + 5, 10, fill='black', lineWidth=0.5)
    Line(x1, 0, x1 - 5, 10, fill='black', lineWidth=0.5)
    Line(x1+5, 0, x1, 10, fill='black', lineWidth=0.5)
    Line(x1-5, 0, x1, 10, fill='black', lineWidth=0.5)
for x1 in range(155,246,5):
    Line(x1, 390, x1 + 5, 400, fill='black', lineWidth=0.5)
    Line(x1, 390, x1 - 5, 400, fill='black', lineWidth=0.5)
    Line(x1+5, 390, x1, 400, fill='black', lineWidth=0.5)
    Line(x1-5, 390, x1, 400, fill='black', lineWidth=0.5)
# score for blue player
scoreB = Label(0, 25, 360, fill='royalBlue', size=30)

# score for red goalie
scoreR = Label(0, 375, 40, fill='fireBrick', size=30)

# hockey puck
puck = Circle(200, 200, 10, fill='snow', border='grey')
puck.dx = 3
puck.dy = 3
puck.numHits = 0

player = Group(
    Circle(200, 365, 12, fill='royalBlue'),
    Circle(200, 365, 8, fill='cornflowerBlue'),
    Rect(190,350,5,10,fill='bisque',border='royalBlue',borderWidth=1),
    Rect(205,350,5,10,fill='bisque',border='royalBlue',borderWidth=1)
    )
goalie = Group(
    Circle(200, 35, 12, fill='fireBrick'),
    Circle(200, 35, 8, fill='crimson'),
    Rect(185,30,10,5,fill='bisque',border='fireBrick',borderWidth=1),
    Rect(205,30,10,5,fill='bisque',border='fireBrick',borderWidth=1)    
    )

def resetPuck():
    puck.centerX = 200
    puck.centerY = 200
    puck.dx = 3
    puck.dy = 3
    puck.numHits = 0

def hitPuck(paddle):
    # Deflect the puck differently based on if it hits on the left, middle,
    # or right.
    if (puck.centerX - paddle.centerX >= 4):
        puck.dx = 3 + puck.numHits
    elif (paddle.centerX - puck.centerX >= 4):
        puck.dx = -3 - puck.numHits
    else:
        puck.dx = 0

    # Deflect the ball differently based on if it hits on the top or bottom.
    if (puck.centerY - paddle.centerY >= 6):
        puck.dy = 3 + puck.numHits
    elif (paddle.centerY - puck.centerY >= 6):
        puck.dy = -3 - puck.numHits

    if (puck.numHits <= 10):
        puck.numHits += 1

def onMouseMove(mouseX, mouseY):
    if ((mouseX >= 60) and (mouseX <= 340) and (mouseY > 200)):
        player.centerX = mouseX
        player.centerY = mouseY

def onKeyPress(key):
    if (key == 'r'):
        resetPuck()
def onKeyHold(keys):
    if('p' in keys):
        resetPuck()
    if('p' in keys and 'o' in keys):
        resetPuck()

def onStep():

    puck.centerX += puck.dx
    puck.centerY += puck.dy

    # If there is a goal, increment the score and reset the puck.
    if ((puck.centerX >= 165) and (puck.centerX <= 235) and
        ((puck.centerY <= 20) or (puck.centerY >= 380))):
        if (puck.centerY <= 20):
            scoreB.value += 1
        elif (puck.centerY >= 380):
            scoreR.value += 1
        if(scoreR.value>=1):

            Rect(200, 200, 250, 150, fill=rgb(185, 70, 50), align='center',opacity=75)
            Label('GAME OVER', 200, 150, fill='white', size=30)
            Label('Blue Fortnites Won', 100, 185, fill='white', size=24, align='left')
            Label('Score: ' + str(scoreR.value), 150, 250, fill='white', size=24, align='left'),
            Label('Restart with r', 200, 230, fill='white', size=18)

        elif(scoreB.value>=1):

            Rect(200, 200, 250, 150, fill='royalBlue', align='center',opacity=50)
            Label('GAME OVER', 200, 150, fill='white', size=30)
            Label('Red Mincraft Dudez', 100, 185, fill='white', size=24, align='left')
            Label('Score: ' + str(scoreB.value), 150, 200, fill='white', size=24, align='left'),
            Label('Restart with r', 200, 230, fill='white', size=18)

        resetPuck()

    # Bounce the puck if necessary.
    if ((puck.centerX <= 60) or (puck.centerX >= 340)):
        puck.dx *= -1
    if ((puck.centerY <= 20) or (puck.centerY >= 380)):
        puck.dy *= -1

    # Move the goalie.
    if (puck.centerX - goalie.centerX < 0):
        goalie.centerX -= 5
    elif (puck.centerX - goalie.centerX > 0):
        goalie.centerX += 5
    if (goalie.centerX < 135):
        goalie.centerX = 135
    elif (goalie.centerX > 265):
        goalie.centerX = 265

    if (puck.hitsShape(player) == True):
        hitPuck(player)
    if (goalie.hitsShape(puck) == True):
        hitPuck(goalie)

cmu_graphics.run()
