from cmu_graphics import *

app.background = gradient('black', 'slateGrey', start='top')
level = 1
flashHealth=400
thorHealth=100
chit1=100
chit2=100
chit3=100
hits=0





# Sets a number of steps for how long a flash lasts.
app.stepsOfFlash = 6

# Sets how many steps until you see another set of lighning bolts.
app.stepsBetweenFlash = 15

lightning = Group()

clouds = Group(
    Circle(42, 50, 70, fill='grey', border='dimGrey'),
    Circle(162, 50, 120, fill='grey', border='dimGrey'),
    Circle(342, 50, 90, fill='grey', border='dimGrey'),
    Rect(0, 0, 400, 85, fill='grey')
    )

def makeLightningBolt(startX, startY):
    x1 = startX
    y1 = startY

    # Each lightning bolt is formed by 25 pieces: 25 lines that create a random
    # downward zigzag effect.
    for boltPiece in range(25):
        # Define a variable to give each bolt piece a random lineWidth between
        # 1 and 2 (inclusive).
        randomWidth = randrange(1, 3)

        # Define a variable x2 that is within 15 pixels of the x1.
        x2 = x1 + randrange(-15, 16)

        # Draw the lightning bolt segment to go down by a random distance
        # between 5 and 20 (inclusive).
        if (boltPiece == 24):
            y2 = 400
        else:
            y2 = y1 + randrange(5, 21)

        # Add a new line to the lightning Group.
        lightning.add(
            Line(x1, y1, x2, y2, fill='aliceBlue', lineWidth=randomWidth)
            )

        # The next bolt piece should start where this one ends.
        x1 = x2
        y1 = y2


diney = Group(
    # giraffe legs
Line(140, 350, 140, 320, fill=gradient('olive','darkOliveGreen','olive'), lineWidth=8,),
Line(100, 350, 100, 320, fill=gradient('olive','darkOliveGreen','olive'), lineWidth=8),
Line(80, 350, 80, 320, fill=gradient('olive','darkOliveGreen','olive'), lineWidth=8),
Line(140, 320, 140, 270,
     fill=gradient('olive', 'darkSeaGreen', 'olive',start='left'), lineWidth=8),
Line(100, 320, 100, 290,
     fill=gradient('olive', 'darkSeaGreen', 'olive',start='left'), lineWidth=8),
Line(80, 320, 80, 290, fill=gradient('olive', 'darkSeaGreen', 'olive',start='left'), lineWidth=8),

# giraffe body
Rect(60, 260, 100, 40, fill=gradient('olive', 'darkSeaGreen', 'olive',start='left'),
     rotateAngle=-20),

# giraffe tail
Line(70, 290, 50, 310, fill=gradient('olive','darkOliveGreen','olive'),arrowEnd=True),

# giraffe neck
Polygon(140, 250, 155, 265, 170, 230, 160, 220,
        fill=gradient('olive', 'darkSeaGreen', 'olive',start='top')),

# giraffe head
Polygon(155, 200, 160, 220, 190, 220, 190, 205,
        fill=gradient('olive', 'darkSeaGreen', 'olive',start='top'),rotateAngle=-40),
Oval(165, 215, 5,8, rotateAngle=-30),
Oval(165, 215, 2,7,fill='crimson', rotateAngle=-30),
Oval(165,219,1,5,fill='black'),

# giraffe ear
Line(147, 210, 152, 215,
     fill=gradient('olive', 'darkSeaGreen', 'olive',start='top'), lineWidth=6))
diney.bottom=150


diney.direction=1




app.steps=0
app.jump=False
background = Image('Screenshot+2024-01-11+1.54.32+PM.png',0,0)
background.width=400
background.height=400

info = Image('Screenshot+2024-01-11+2.00.46+PM.png',200,260)
info.width = 96
info.height=36

play = Image('ezgif.com-animated-gif-maker.gif',100,260)
play.width = 96
play.height=36

infoScreen = Image('Screenshot+2024-01-11+2.42.16+PM.png',0,0)
infoScreen.width=400
infoScreen.height=400
infoScreen.visible=False



thor = Image('Screenshot_2024-01-11_2.45.15_PM-removebg-preview.png',50,300)
thor.width=73
thor.height=65
thor.visible=False






ground = Rect(0,365,400,35)



bar = Rect(0,0,10,1)  
stop = Rect(0,146,10,45,fill='crimson')
lavel = Label("FALLING!",5,168.5,rotateAngle = -90,size=10)
bar.visible=False
stop.visible=False
lavel.visible=False




def startVisible():
    background.visible=False
    info.visible=False
    play.visible=False


def startVisiblez():
    background.visible=True
    info.visible=True
    play.visible=True
    infoScreen.visible=False



def onMousePress(x,y):
    if(play.contains(x,y)):
        startVisible()
        bar.visible=True
        stop.visible=True
        lavel.visible=True
        thor.visible=True

    if(info.contains(x,y)):
        startVisible()
        infoScreen.visible=True
    if(y<130):
        startVisiblez()



def onKeyHold(key):
    if(('right' in key) and thor.visible==True):
        thor.centerX+=3
    elif(('left' in key) and thor.visible==True):
        thor.centerX-=3
    if(('up' in key) and thor.visible==True):
        thor.centerY-=9
        app.steps+=1
        bar.height+=5
        app.jump=True
    else:
        app.jump=False
    if('space' in key and background.visible==True):
        breker.toFront()
        x, y = getPointInDir()
        while breker.hitsShape(thor)==False or breker.hitsShape(ground)==False:
            breker.centerY+=1
            breker.rotateAngle+=1


app.hits='left'










def onStep():


    if(thor.hitsShape(ground)):
        thor.bottom=365
        app.steps=0
    elif(app.jump==False and thor.hitsShape(ground)==False):
        thor.centerY+=6
    else:
        thor.centerY+=4
    if(thor.bottom==365):
        bar.height=1
    if app.steps>=30:
        thor.centerY*=1.1

    app.stepsBetweenFlash -= 1

    if (app.stepsBetweenFlash == 0):
        # Each lightning strike is made up of 4 individual lightning bolts.
        # Initializes where the bolts start here so each bolt has the same
        # starting position and stays close to the other bolts.
        startX = randrange(50, 350)
        startY = 100
        for bolt in range(4):
            makeLightningBolt(startX, startY)

        # Changes the clouds fill, and the background.
        clouds.fill = 'gainsboro'
        app.background = gradient('dimGrey', rgb(170, 180, 200), start='top')

        # Resets flash steps to 15, and steps of the flash to 6.
        app.stepsBetweenFlash = 15
        app.stepsOfFlash = 6

    # Decreases the number of steps the flash has been on for until it gets to 0.
    if (app.stepsOfFlash > 0):
        app.stepsOfFlash -= 1

    # When the strike has been on the canvas long enough, removes the lightning,
    # and changes the fills back to their original values.
    if (app.stepsOfFlash == 0):
        lightning.clear()
        clouds.fill = 'grey'
        app.background = gradient('black', 'slateGrey', start='top')
    if(diney.direction==1):
        diney.centerX+=6
        diney.rotateAngle+=5
        if(diney.right>=400):
            diney.direction=-1
    elif(diney.direction==-1):
        diney.centerX-=6
        diney.rotateAngle-=5
        if(diney.left<=0):
            diney.direction=1











cmu_graphics.run()
