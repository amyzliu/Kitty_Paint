#paint.py
#Amy-Zhiying Liu
#Paint Program! This program simulates the Microsoft Paint program. The user can
#choose among various tools such as: pencil, eraser, spraypaint and brush, save/
#load files and stamp on small bitmaps.

from pygame import *
from random import *
from glob import *

font.init() # initialize font
streetFont = font.Font("STREH___.TTF", 20)
blackbox=image.load("More Pics/blackbox.png")
blackbox2=image.load("More Pics/blackbox2.png")
bluebox=image.load("More Pics/bluebox.png")

# prevents aggravating noise if the user clicks quickly
mixer.pre_init(44100,16,2,1024*4) 
init()# initialize mixer
stampsound = mixer.Sound("sound/stamp.ogg")# load in sound

mixer.music.load("sound/themesong.mp3")
mixer.music.play(-1)
vol=0.5

hotpink = (255,105,180)
lightpink = (255,160,122)
white = (255,255,255)
col = hotpink # initial colour 

screen = display.set_mode((985,800))
background = image.load("More Pics/background.png")
display.set_caption("Welcome to Sanrio's Paint Software Developed by Amy Liu! Paint with Hello Kitty and Friends!")
screen.blit(background,(0,0))
canvasRect=Rect(328,26,643,453)

def oval(mx,my,ax,ay,size):
    try: # checks if oval width is greater than the set size to prevent crashing
        draw.ellipse(screen,col,(min(ax,mx),min(ay,my),abs(ax-mx),abs(ay-my)),size)
    except: return
    
def load():
    try: 
        txt=getName()
        picture=image.load(txt)
        screen.blit(picture,(328,26))
    except: return # if an improper name was entered, go back to the program 
    
def save():
    txt=getName()
    if len(txt)>4: # file name must have something in front of its extension
        if txt[-4]==".":
            period=txt.index(".")
            if txt[period:]==".bmp" or txt[period:]==".jpg" or txt[period:]==".png":
                image.save(screen.subsurface(canvasRect),txt)
    else:
        # if the user gives an improper extension, program saves as a PNG file 
        txt+=".png" 
        image.save(screen.subsurface(canvasRect),txt)
        
def getName():
    ans = ""                    # final answer will be built one letter at a time.
    streetFont = font.Font("STREH___.ttf", 20)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(695,504,254,25) 
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    draw.rect(screen,(white),choiceArea)        # draw the text window and the text.
    draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
    for i in range(n):
        txtPic = streetFont.render(pics[i], True, hotpink)   #
        screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = streetFont.render(ans, True, (0,0,0))   
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans

humourFont = font.Font("STREH___.ttf", 20)
y = 20

tool = "pencil" # initial tool is pencil
start = 0,0
size = 1

undolist = [screen.copy()]
redolist = []
polylist = []
stamps = ["stamp1","stamp2","stamp3","stamp4","stamp5","stamp6","stamp7","stamp8",
          "stamp9","stamp10","stamp11","stamp12"]
stamptexts = ["stamp1text","stamp2text","stamp3text","stamp4text","stamp5text",
              "stamp6text","stamp7text","stamp8text","stamp9text","stamp10text",
              "stamp11text","stamp12text"]
toolrects = ["pencilRect","eraserRect","sprayRect","polyemptyRect","polyfullRect"
             ,"lineRect","brushRect","rectemptyRect","rectfullRect","ovalemptyRect"
             ,"ovalfullRect","eyedropRect"]
tools = ["pencil","eraser","spray","polyempty","polyfull","line","brush","rectempty"
         ,"rectfull","ovalempty","ovalfull","eyedrop"]
#---------------------------------------toolRects
penguinRect=Rect(700,705,67,95) # hidden cloud tool
pencilRect=Rect(33,145,49,47)
eraserRect=Rect(137,145,49,47)
sprayRect=Rect(240,145,49,47)
polyemptyRect=Rect(33,229,24,47)
polyfullRect=Rect(58,229,24,47)
lineRect=Rect(137,229,49,47) 
brushRect=Rect(240,229,49,47)
rectemptyRect=Rect(33,315,24,47)    
rectfullRect=Rect(58,315,24,47)
ovalemptyRect=Rect(137,315,24,47)
ovalfullRect=Rect(162,315,24,47)
eyedropRect=Rect(240,315,49,47)

colRect = Rect(142,382,156,156)
greyRect = Rect(290,497,74,74)
pauseRect = Rect(576,647,20,20)
playRect = Rect(407,648,20,20)

minusRect = Rect(440,765,30,30)
plusRect = Rect(557,765,30,30)

clearRect = Rect(226,641,75,28) 
undoRect = Rect(123,560,75,28) 
redoRect = Rect(226,578,75,28)
saveRect = Rect(21,597,75,28)
loadRect = Rect(121,622,75,28)

#----------------stamp locations
maru=image.load("Stamp Images/maru.png")
stamp1Rect=Rect(50,678,111,54)

frog=image.load("Stamp Images/frog.png")
stamp2Rect=Rect(28,737,60,60)

dog=image.load("Stamp Images/dog.png")
stamp3Rect=Rect(114,708,62,88)

boy=image.load("Stamp Images/boy.png")
stamp4Rect=Rect(290,684,65,50)

evil=image.load("Stamp Images/evil.png")
stamp5Rect=Rect(291,746,61,50)

choco=image.load("Stamp Images/choco.png")
stamp6Rect=Rect(652,757,47,41)

duck=image.load("Stamp Images/duck.png")
stamp7Rect=Rect(768,715,59,84)

rac=image.load("Stamp Images/rac.png")
stamp8Rect=Rect(885,739,50,60)

cinna=image.load("Stamp Images/cinna.png")
stamp9Rect=Rect(652,711,39,34)

purin=image.load("Stamp Images/purin.png")
stamp10Rect=Rect(598,727,45,40)

melody=image.load("Stamp Images/melody.png")
stamp11Rect=Rect(827,707,57,93)

king=image.load("Stamp Images/king.png")
stamp12Rect=Rect(934, 706,50,94)

#----Hello Kitty's speech bubble text images
cloudtext=image.load("Text Images/cloudtext.png")
stamp1text=image.load("Text Images/stamp1text.png")
stamp2text=image.load("Text Images/stamp2text.png")
stamp3text=image.load("Text Images/stamp3text.png")
stamp4text=image.load("Text Images/stamp4text.png")
stamp5text=image.load("Text Images/stamp5text.png")
stamp6text=image.load("Text Images/stamp6text.png")
stamp7text=image.load("Text Images/stamp7text.png")
stamp8text=image.load("Text Images/stamp8text.png")
stamp9text=image.load("Text Images/stamp9text.png")
stamp10text=image.load("Text Images/stamp10text.png")
stamp11text=image.load("Text Images/stamp11text.png")
stamp12text=image.load("Text Images/stamp12text.png")
penciltext=image.load("Text Images/penciltext.png")
erasertext=image.load("Text Images/erasertext.png")
spraytext=image.load("Text Images/spraytext.png")
polyemptytext=image.load("Text Images/polyemptytext.png")
polyfulltext=image.load("Text Images/polyfulltext.png")
linetext=image.load("Text Images/linetext.png")
brushtext=image.load("Text Images/brushtext.png")
rectemptytext=image.load("Text Images/rectemptytext.png")
rectfulltext=image.load("Text Images/rectfulltext.png")
ovalemptytext=image.load("Text Images/ovalemptytext.png")
ovalfulltext=image.load("Text Images/ovalfulltext.png")
eyedroptext=image.load("Text Images/eyedroptext.png")
undotext=image.load("Text Images/undotext.png")
redotext=image.load("Text Images/redotext.png")
cleartext=image.load("Text Images/cleartext.png")
savetext=image.load("Text Images/savetext.png")
loadtext=image.load("Text Images/loadtext.png")
                       
running =True
while running:
    screen.set_clip(None)
    draw.ellipse(screen,col,(554,526,42,48)) # shows current colour in an oval
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            if e.button==1: 
                screenpic=screen.copy()
                start=e.pos
            if e.button==4:
                size=min(20,size+1) # 20 is the maximum size
            if e.button==5:
                size=max(1,size-1)
            ax,ay=e.pos
            if undoRect.collidepoint(ax,ay):
                if len(undolist)>1:             
                    redolist.append(undolist[-1])
                    # add the last element of undolist to redolist, then 
                    del undolist[-1] # delete it from the undolist and
                    screen.blit(undolist[-1],(0,0)) # blit the last pic 
            if redoRect.collidepoint(ax,ay):
                if len(redolist)>0:
                    # blit the last element of the redolist,
                    screen.blit(redolist[-1],(0,0))
                    undolist.append(redolist[-1]) # then append it to undolist
                    del redolist[-1] # and finally delete it from redolist
        if e.type==MOUSEBUTTONUP:
            # if user clicked on canvas or clicked clear, take a screenshot
            if canvasRect.collidepoint(ax,ay) or clearRect.collidepoint(ax,ay): # if click
                undolist.append(screen.copy()) 

    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()         
    
    coords = streetFont.render("("+str(mx)+","+str(my)+")",True,hotpink)
    # blit a black box behind the coordinates of the mouse position
    screen.blit(blackbox,(32,534))
    # show current mouse position
    screen.blit(coords,(32,534))
    # shows current size; fontsize depends on the current size
    sizeFont = font.Font("STREH___.TTF", size+19)
    currentsize = sizeFont.render(str(size),True,hotpink)
    screen.blit(blackbox2,(32,430))
    screen.blit(currentsize,(32,430))       

    mixer.music.set_volume(vol)

    if mb[0]==1:
    # coldist equals the distance from mouse to centre of colour wheel
    # if distance is less than wheel radius, the current colour is the colour
    # at the mouse click        
        coldist = ((mx-220)**2+(my-460)**2)**0.5
        greydist = ((mx-327)**2+(my-534)**2)**0.5 # greyscale colour wheel
        # Since ax,ay is the position when mouse button is down, it must be used
        # for the tools below to make sure that there is only one tool selected
        # each time, and that dragging the mouse to different tools will not
        # change the tool that was selected by mouse click.
        if colRect.collidepoint(ax,ay):
            if coldist<=78:
                col=screen.get_at((ax,ay))
        if greyRect.collidepoint(ax,ay):
            if greydist<=37:
                col=screen.get_at((ax,ay))        
        pausedist = ((mx-586)**2+(my-657)**2)**0.5 # pauses music
        if pauseRect.collidepoint(ax,ay):
            if pausedist<=10:
                mixer.music.pause()
                
        playdist = ((mx-417)**2+(my-658)**2)**0.5 # unpauses music
        if playRect.collidepoint(ax,ay):
            if playdist<=10:
                mixer.music.unpause()

        minusdist = ((mx-455)**2+(my-778)**2)**0.5 # lowers volume
        if minusRect.collidepoint(ax,ay):
            if minusdist<=15:
                vol-=0.1
                mixer.music.set_volume(vol)

        plusdist= ((mx-542)**2+(my-778)**2)**0.5 # raises volume
        if plusRect.collidepoint(ax,ay):
            if plusdist<=15:
                vol+=0.1
                mixer.music.set_volume(vol)
        if penguinRect.collidepoint(ax,ay):
            tool="cloud"
            
        for r in range(len(tools)):
            if eval(toolrects[r-1]).collidepoint(ax,ay):
                tool=tools[r-1]
                
        for q in range(len(stamps)):
            if eval(str(stamps[q-1])+"Rect").collidepoint(ax,ay):
                tool=stamps[q-1]
        if clearRect.collidepoint(mx,my):
           draw.rect(screen,white,canvasRect) # draws a white canvas            
        if saveRect.collidepoint(mx,my):
            save()
        if loadRect.collidepoint(mx,my):
            load()            
#----------------------------what the tools do if clicked on canvas

        if canvasRect.collidepoint(ax,ay):
# (ax,ay) is used here to prevent tools from being dragged into the canvas.
# If it was replaced with (mx,my), stamps could be dragged in, disallowing the
# undo tool to recognize a mousebuttondown action in the canvas.
            screen.set_clip(canvasRect)
            if tool=="pencil": # draws a line from old mouse pos to new mouse pos
                draw.aaline(screen,col,(ox,oy),(mx,my),3) 
                
            if tool=="brush":
                d=((ox-mx)**2+(oy-my)**2)**0.5
                dx=mx-ox # x-coord of distance between old point and new point 
                dy=my-oy 
                if d==0:
                    d=1 # set distance as the closest positive integer to zero
                        # to avoid division by zero
                rx=dx/d # ratio 
                ry=dy/d
                for i in range (int(d)):
                    draw.circle(screen,col,(int(ox),int(oy)),size)
                    # draws a circle at every pixel of the mouse position
                    ox+=rx 
                    oy+=ry
                    
            if tool=="eraser":
                # code is identical to the brush except for the colour
                d=((ox-mx)**2+(oy-my)**2)**0.5
                dx=mx-ox
                dy=my-oy
                if d==0:
                    d=1 
                rx = dx/d
                ry = dy/d
                for i in range (int(d)):
                    draw.circle(screen,white,(int(ox),int(oy)),size)
                    ox+=rx
                    oy+=ry
                    
            if tool=="spray":
                # draws random tiny circles in a mouse-position-designated
                # area of a circle with a changeable radius
                for i in range(size*2):
                    randx=randint(mx-size-9,mx+size+9)
                    randy=randint(my-size-9,my+size+9)
                    if (randx-mx)**2+(randy-my)**2<=(size+9)**2:
                        draw.circle(screen,col,(randx,randy),0)

            if tool=="line":
                screen.blit(screenpic,(0,0)) # only shows the most recent line
                draw.line(screen,col,start,(mx,my),size)
                
            # Strangely and unfortunately, there is such thing as negative
            # areas. To ensure a positive, realistic area, set absolute value.
            if tool=="rectempty":
                screen.blit(screenpic,(0,0))
                draw.rect(screen,col,(min(ax,mx),min(ay,my),abs(ax-mx),abs(ay-my)),size)
                
            if tool=="rectfull":
                screen.blit(screenpic,(0,0))
                draw.rect(screen,col,(min(ax,mx),min(ay,my),abs(ax-mx),abs(ay-my)))

            if tool=="ovalempty":
                screen.blit(screenpic,(0,0))
                # oval width should be greater than set width
                if abs(ax-mx)>size and abs(ay-my)>size:
                    oval(mx,my,ax,ay,size) 
                    oval(mx+1,my,ax+1,ay,size) # draw a 2nd oval 1 pixel to the
                                               # right to cover up the holes
            if tool=="ovalfull":
                screen.blit(screenpic,(0,0))
                draw.ellipse(screen,col,(min(ax,mx),min(ay,my),abs(ax-mx),abs(ay-my)))
                
            if tool=="eyedrop":
                col=screen.get_at((mx,my))
             
            if tool=="stamp1":
                screen.blit(screenpic,(0,0)) # only blits most recent stamp 
                screen.blit(maru,(mx-25,my-25))
                stampsound.play() # play sound when stamping
            if tool=="stamp2":
                screen.blit(screenpic,(0,0))
                screen.blit(frog,(mx-30,my-30))
                stampsound.play()                
            if tool=="stamp3":
                screen.blit(screenpic,(0,0))
                screen.blit(dog,(mx-30,my-30))
                stampsound.play()               
            if tool=="stamp4":
                screen.blit(screenpic,(0,0))
                screen.blit(boy,(mx-30,my-33))
                stampsound.play()                
            if tool=="stamp5":
                screen.blit(screenpic,(0,0))
                screen.blit(evil,(mx-25,my-33))
                stampsound.play()               
            if tool=="stamp6":
                screen.blit(screenpic,(0,0))
                screen.blit(choco,(mx-25,my-25))
                stampsound.play()               
            if tool=="stamp7":
                screen.blit(screenpic,(0,0))
                screen.blit(duck,(mx-30,my-35))
                stampsound.play()             
            if tool=="stamp8":
                screen.blit(screenpic,(0,0))
                screen.blit(rac,(mx-30,my-30))
                stampsound.play()                
            if tool=="stamp9":
                screen.blit(screenpic,(0,0))
                screen.blit(cinna,(mx-35,my-40))
                stampsound.play()               
            if tool=="stamp10":
                screen.blit(screenpic,(0,0))
                screen.blit(purin,(mx-30,my-30))
                stampsound.play()               
            if tool=="stamp11":
                screen.blit(screenpic,(0,0))
                screen.blit(melody,(mx-24,my-45))
                stampsound.play()               
            if tool=="stamp12":
                screen.blit(screenpic,(0,0))
                screen.blit(king,(mx-40,my-45))
                stampsound.play()
                
            if tool=="cloud":
            # draws clusters of overlapping circles in the form of clouds
                for i in range(randint(1,25)):
                    x=randint(mx-randint(1,size),mx+randint(size+1,size*5))
                    y=randint(my-randint(1,size),my+randint(size+1,size*5))
                    draw.circle(screen,col,(x,y),randint(size*2,size*4))
                    
    if tool=="polyempty":
        if mb[0]==1:
            # if left-clicked on canvas, append clicked points to a list
            if canvasRect.collidepoint((mx,my)):
                screen.set_clip(canvasRect)
                polylist.append((ax,ay)) 
        if mb[2]==1: 
            if len(polylist)>2: # polygons only exist with at least 3 points
                # if right-clicked, draw a polygon with the list of points
                draw.polygon(screen,col,polylist,size)
                polylist=[] # delete everything in the list to start a new polygon
    if tool=="polyfull": # same code as the empty polygon tool except filled
        if mb[0]==1:
            if canvasRect.collidepoint((mx,my)):
                screen.set_clip(canvasRect)
                polylist.append((ax,ay)) 
        if mb[2]==1:
            if len(polylist)>2:
                draw.polygon(screen,col,polylist)
                polylist=[]
    if tool!="polyfull" and tool!="polyempty":
        polylist=[] # list is empty when the user isn't drawing a polygon
#--------------------------------stamp selection
    for i in range(len(stamps)):
        if tool==stamps[i-1]:
            screen.blit(eval(stamps[i-1]+"text"),(695,504))
#-------------------------------tool selection and hovers
    if tool=="cloud":
        screen.blit(cloudtext,(695,504))            
# if mouse position collides point with tool, draw a light pink border
# if mouse clicks a tool, draw a hot pink border
# if mouse is neither clicking nor colliding with a tool, draw a white border

    for h in range(len(tools)):
        if tool==tools[h]:
            draw.rect(screen,hotpink,eval(toolrects[h]),3)
            screen.blit(eval(tools[h]+"text"),(695,504))
        elif eval(toolrects[h]).collidepoint(mx,my):
            draw.rect(screen,lightpink,eval(toolrects[h]),3)
        else:
            draw.rect(screen,white,eval(toolrects[h]),3)
# the tools below have hovertexts (and the ones above don't) because accidentally
# clicking these buttons perform functions that don't require clicking the canvas
    #undo
    if undoRect.collidepoint(start):
        draw.line(screen,hotpink,(123,583),(197,583),2)
    elif undoRect.collidepoint(mx,my):
        draw.line(screen,lightpink,(123,583),(197,583),2)
        screen.blit(undotext,(695,504))
    else:
        draw.line(screen,(0,0,0),(123,583),(197,583),2)
    #redo
    if redoRect.collidepoint(start):
        draw.line(screen,hotpink,(230,605),(301,605),2)
    elif redoRect.collidepoint(mx,my):
        draw.line(screen,lightpink,(230,605),(301,605),2)
        screen.blit(redotext,(695,504))
    else:
        draw.line(screen,(0,0,0),(230,605),(301,605),2)
    #clear
    if clearRect.collidepoint(start):
        draw.line(screen,hotpink,(229,669),(298,669),2)
    elif clearRect.collidepoint(mx,my):
        draw.line(screen,lightpink,(229,669),(298,669),2)
        screen.blit(cleartext,(695,504))
    else:
        draw.line(screen,(0,0,0),(229,669),(298,669),2)
    #save
    if saveRect.collidepoint(start):      
        draw.line(screen,hotpink,(25,622),(94,622),2)
    elif saveRect.collidepoint(mx,my):
        draw.line(screen,lightpink,(25,622),(94,622),2)
        screen.blit(savetext,(695,504))
    else:
        draw.line(screen,(0,0,0),(25,622),(94,622),2)
    #load
    if loadRect.collidepoint(start):
        draw.line(screen,hotpink,(123,647),(196,647),2)
    elif loadRect.collidepoint(mx,my):
        draw.line(screen,lightpink,(123,647),(196,647),2)
        screen.blit(loadtext,(695,504))
    else:
        draw.line(screen,(0,0,0),(123,647),(196,647),2)
        
    ox,oy=mx,my # coords of the "old point"; used in pencil, brush, and eraser 
    display.flip()
font.quit() 
del humourFont
quit()
