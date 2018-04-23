from imageTools import*


ball = Picture("tennisball.jpg")
box = Picture("rectangle.jpg")
test = Picture("trial2.jpg")
square = Picture("blacksquare.jpg")
square2 = Picture("square2.png")
green = Picture("greenrectangle.jpg")
grey = Picture("greybox.jpg")
circle = Picture("greenball.jpg")
crowdedgreen = Picture("crowdedgreen.jpg")

finaltestwhite = Picture("finaltest.jpg")
finaltestcrowded = Picture("greencrowded.jpg")

def getColList(picture):
    """Returns a list of colors making up an object on a white background"""
    wid = picture.getWidth()
    hgt = picture.getHeight()
    colorList = []
    backlist = []
    for y in range(hgt):
        for x in range(wid):
            (r, g, b) = picture.getColor(x, y)
            dist = distance((255, 255, 255), (r, g, b))
            if dist < 80:
                backlist.append((r, g, b))
            else:
                colorList.append((r, g, b))
    return colorList

def getColMax(picture):
    """Calls on getColList and find the maximum value in this list"""
    colorList = getColList(picture)
    rList = []
    gList = []
    bList = []
    for entry in colorList:
        rList.append(entry[0])
        gList.append(entry[1])
        bList.append(entry[2])
    rMax = max(rList)
    gMax = max(gList)
    bMax = max(bList)
    (rM, gM,bM) = (rMax, gMax, bMax)
    return (rM, gM,bM)

def getColMin(picture):
    """Calls on getColList and find the minimum value in this list"""
    colorList = getColList(picture)
    rList = []
    gList = []
    bList = []
    for entry in colorList:
        rList.append(entry[0])
        gList.append(entry[1])
        bList.append(entry[2])
    rMin = min(rList)
    gMin = min(gList)
    bMin = min(bList)
    (rN, gN, bN) = (rMin, gMin, bMin)
    return (rN, gN, bN)

def getColAv(picture):
    """Calls on getColList and find the average value in this list"""
    colorList = getColList(picture)
    rList = []
    gList = []
    bList = []
    for entry in colorList:
        rList.append(entry[0])
        gList.append(entry[1])
        bList.append(entry[2])
    rSum = sum(rList)
    rLen = len(rList)
    rAv = rSum / rLen
    gSum = sum(gList)
    gLen = len(gList)
    gAv = gSum / gLen
    bSum = sum(bList)
    bLen = len(bList)
    bAv = bSum / bLen
    (rA, gA, bA) = (rAv, gAv, bAv)
    return (rA, gA, bA)


def identifyObject(whitePic, backPic):
    """Identifies an object based on the picture on a white background
    using getcolmax and getcolmin"""
    wid = backPic.getWidth()
    hgt = backPic.getHeight()
    bwPic = Picture(wid, hgt)
    min = getColMin(whitePic)
    max = getColMax(whitePic)
    for y in range(hgt):
        for x in range(wid):
            (r, g, b) = backPic.getColor(x, y)
            if r >= min[0] and r <= max[0] and g >= min[1] and g <= max[1] and b >= min[2] and b <= max[2]:
                bwPic.setColor(x, y, (255, 255, 255))
            else:
                bwPic.setColor(x, y, (0, 0, 0))
    return bwPic

# def blur(whitePic, backPic):
#
#
def colorIdentify(whitePic, backPic):
    wid = backPic.getWidth()
    hgt = backPic.getHeight()
    bwPic = identifyObject(whitePic, backPic)
    colorPic = Picture(wid, hgt)
    for y in range(hgt):
        for x in range(wid):
            (r, g, b) = bwPic.getColor(x, y)
            colorrgb = backPic.getColor(x, y)
            if (r, g, b) == (0, 0, 0):
                colorPic.setColor(x, y, colorrgb)
            else:
                colorPic.setColor(x, y, (255, 255, 255))
    return colorPic




# ball.explore()
# pic = identifyObject(ball)
# pic.explore()

# pic2 = identifyObject(green)
# pic2.explore()

# pic3 = identifyObject(box)
# pic3.explore()


# identifyObject(test)


# print(getColList(box))
# print("max:", getColMax(test))
# print("min:", getColMin(test))


finaltestcrowded.explore()
sample = identifyObject(finaltestwhite, finaltestcrowded)
sample.explore()
sample2 = colorIdentify(finaltestwhite, finaltestcrowded)
sample2.explore()