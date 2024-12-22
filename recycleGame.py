import pgzrun, random

WIDTH = 800
HEIGHT = 600

speed = 10

ITEMS = ["battery", "paper", "chips", "bottle"]

gameState = "play"

currentLevel = 1
items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bground", (0,0))
    
    if gameState == "win":
        screen.draw.text("You win!", fontsize = 30, center = (WIDTH/2, HEIGHT/2), color = "white") 
    elif gameState == "lose":
        screen.draw.text("Game Over! Try the level again", fontsize = 30, center = (WIDTH/2, HEIGHT/2), color = "white")
    elif gameState == "play":
        for i in items:
            i.draw()     

def update():
    global items
    if len(items) == 0:
        makeItems(currentLevel)

def makeItems(noOfItems):
    requiredItems = getOptionToCreate(noOfItems)
    createObjects = createItems(requiredItems)
    posItems(createObjects)
    animateItems(createObjects)
    return createObjects

def getOptionToCreate(noOfItems):
    createObjects = ["paper"]   
    for i in range(noOfItems):
        createObjects.append(random.choice(ITEMS))
    return createObjects

def createItems(createObjects):
    newItems = []
    for i in createObjects:
        object = Actor(i+"img")
        newItems.append(object)
    return newItems

def posItems(newItems):
    noOfGaps = len(newItems) + 1
    gapSize = WIDTH/noOfGaps
    random.shuffle(newItems)
    
    for i, item in enumerate(newItems):
        xpos = (i+1)*gapSize
        item.x = xpos

def animateItems(newItems):
    global animations
    
    for i in newItems:
        duration = speed - currentLevel
        i.anchor = ("center", "bottom")
        animation = animate(i, duration = duration, on_finished = gameOver, y = HEIGHT)
        animations.append(animation)
        
def gameOver():
    print("Game Over!")                 
pgzrun.go()            