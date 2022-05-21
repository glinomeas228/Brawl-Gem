leggins=1
o=0
v=0
a=400
b=300
n=2
c=random(600)
d=0
nice=0
lol=int(random(4))
shopopen=0
n=4
p=10
s=60
l=0
count=0
viborbg=0
def setup():
    size(800,600)
    frameRate(120)
    global loading,viborskina,skins,skins2,gem,gameover,lol,shopimage,shop,p,icon,rules,backgrounds
    loading=[loadImage('123.bmp'),loadImage('123v2.bmp'),loadImage('123v3.bmp'),loadImage('123v4.bmp')]
    viborskina=loadImage('1234.bmp')
    skins=[loadImage('1.png'),loadImage('2.png'),loadImage('3.png')]
    skins2=[loadImage('1right.png'),loadImage('2right.png'),loadImage('3right.png')]
    gem=loadImage('gem.png')
    gameover=loadImage('gameover.bmp')
    shopimage=loadImage('shopimage.png')
    shop=loadImage('shop.bmp')
    icon=loadImage('infoicon.png')
    rules=loadImage('rules.bmp')
    backgrounds=[loadImage('background0.bmp'),loadImage('background1.jpg'),loadImage('background2.jpg'),loadImage('background3.png'),loadImage('background4.jpg'),loadImage('background5.jpg'),loadImage('background6.jpg')]
def draw():
    global loading,viborskina,skins,skins2,o,v,a,b,n,gem,c,d,gameover,nice,lol,shopimage,shopopen,shop,n,p,s,icon,rules,l,count,backgrounds,viborbg
    background(255)
    o=o+1
    if shopopen==0:
        count=count+1
    frameRate(s)
    fill('#005FFF')
    if count==400:
        count=0
        nice=nice+l
    if s>400:
        s=400
    if s>400 and key=='3' and shopopen==1 and nice>99:
        s=400
    textSize(100)
    if d>450 and a>c-70 and a<c+70 and shopopen==0:
        background(255)
        d=0
        c=random(600)
        nice=nice+1
    if shopopen==0:
        gameplay()
    if o>120 and o<1000000 and shopopen==0:
        background(255,255,255)
        image(viborskina,0,0,800,600)
        image(skins[v],300,250,150,150)
    if d>590:
        background(255)
        image(gameover,0,0,800,600)
        noLoop()
    if o<120 and shopopen==0:
        image(loading[lol],0,0,800,600)
        
    if shopopen==1:
        image(shop,0,0,800,600)
    if shopopen==2:
        image(rules,0,0,800,600)
    if shopopen==2 and key=='1':
        shopopen=0
    if n<1:
        n=1
        nice=nice+40
    if a<-50 or a>750:
        background(255)
        textSize(60)
        image(gameover,0,0,800,600)
        noLoop()
def keyPressed():
    global v,n,a,b,o,p,shopopen,s,n,d,nice,l,viborbg,backgrounds
    playermovement()
    if key==ENTER:
        o=1000000000000000000000000
    skinselection()
    if v>2:
        v=0
    if v==-1:
        v=2
    if l>20 and shopopen==1 and key=='4':
        l=20
        nice=nice+50
    if key=='1' and shopopen==1:
        shopopen=0
    if key=='2' and shopopen==1 and nice>39:
        nice=nice-40
        n=n-0.2
        d=d+n
    if key=='2' and shopopen==1 and nice<40:
        n=n
    if key=='3' and shopopen==1 and nice>99:
        nice=nice-100
        s=s+5
    if key=='3' and shopopen==1 and nice<100:
        s=s
    if key=='0' and shopopen==0:
        shopopen=2
    if key=='4' and shopopen==1 and nice<50:
        l=l
    if key=='4' and shopopen==1 and nice>49:
        nice=nice-50
        l=l+1
def mouseClicked():
    storeopeningwiththemouse()
def gameplay():
    global leggins,loading,viborskina,skins,o,v,a,b,n,gem,c,d,gameover,nice,lol,shopimage,shopopen,shop,n,p,s,icon,rules,l,count,backgrounds,viborbg
    if leggins==1:
        image(skins[v],a,500,100,100)
    if leggins==2:
        image(skins2[v],a,500,100,100)
    if o>1000000000000 and shopopen==0:
        d=d+n
        image(gem,c,d,50,50)
        image(shopimage,0,0,100,100)
        image(icon,750,0,50,45)
        text(nice,400,300)
def playermovement():
    global loading,viborskina,skins,skins2,o,v,a,b,n,gem,c,d,leggins,gameover,nice,lol,shopimage,shopopen,shop,n,p,s,icon,rules,l,count,backgrounds,viborbg
    if keyCode==LEFT and shopopen==0:
        a=a-p
        leggins=1
    if keyCode==RIGHT and shopopen==0:
        a=a+p
        leggins=2
def skinselection():
    global loading,viborskina,skins,o,v,a,b,n,gem,c,d,gameover,nice,lol,shopimage,shopopen,shop,n,p,s,icon,rules,l,count,backgrounds,viborbg
    if key=='+':
        v=v+1
    if key=='-':
        v=v-1
    if key=='=':
        v=v+1
def storeopeningwiththemouse():
    global shopopen
    if mouseX<100 and mouseY<100:
        shopopen=1
