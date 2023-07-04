import pygame

# consts of colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)

# the list of colors
colors = [WHITE, BLACK, RED, GREEN, BLUE, YELLOW, PINK]
WIDTH = 800  # ширина игрового окна
HEIGHT = 800 # высота игрового окна
FPS = 30 # частота кадров в секунду

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-tac-toe")
clock = pygame.time.Clock()

occupiedPlace = { 
        "1" : None,
        "2" : None,
        "3" : None,
        "4" : None,
        "5" : None,
        "6" : None,
        "7" : None,
        "8" : None,
        "9" : None
        }
stop = True
whoWin = ""
def checkWin():
    global stop, whoWin
    if stop:
        if occupiedPlace["1"] == occupiedPlace["2"] == occupiedPlace["3"] and occupiedPlace["1"] != None:
            pygame.draw.aaline(screen, GREEN, (250, 250), (550,250))
            stop = False
            whoWin = occupiedPlace["1"]
        elif occupiedPlace["4"] == occupiedPlace["5"] == occupiedPlace["6"] and occupiedPlace["4"] != None:
            pygame.draw.aaline(screen, GREEN, (250, 350), (550,350))
            stop = False
            whoWin = occupiedPlace["4"]
        elif occupiedPlace["7"] == occupiedPlace["8"] == occupiedPlace["9"] and occupiedPlace["7"] != None:
            pygame.draw.aaline(screen, GREEN, (250, 450), (550,450))
            stop = False
            whoWin = occupiedPlace["7"]
        elif occupiedPlace["1"] == occupiedPlace["4"] == occupiedPlace["7"] and occupiedPlace["1"] != None:
            pygame.draw.aaline(screen, GREEN, (300, 200), (300,500))
            stop = False
            whoWin = occupiedPlace["1"]
        elif occupiedPlace["2"] == occupiedPlace["5"] == occupiedPlace["8"] and occupiedPlace["2"] != None:
            pygame.draw.aaline(screen, GREEN, (400, 200), (400,500))
            stop = False
            whoWin = occupiedPlace["2"]
        elif occupiedPlace["3"] == occupiedPlace["6"] == occupiedPlace["9"] and occupiedPlace["3"] != None:
            pygame.draw.aaline(screen, GREEN, (500, 200), (500,500))
            stop = False
            whoWin = occupiedPlace["3"]
        elif occupiedPlace["1"] == occupiedPlace["5"] == occupiedPlace["9"] and occupiedPlace["1"] != None:
            pygame.draw.aaline(screen, GREEN, (250, 200), (550,500))
            stop = False
            whoWin = occupiedPlace["1"]
        elif occupiedPlace["3"] == occupiedPlace["5"] == occupiedPlace["7"] and occupiedPlace["3"] != None:
            pygame.draw.aaline(screen, GREEN, (550, 200), (250,500))
            stop = False
            whoWin = occupiedPlace["3"]
def getCenterOfPlace(place):
    centreOfplace = { # (x, y) - coordinates of the centers of the places
                "1" : (300,250),
                "2" : (400,250),
                "3" : (500,250),
                "4" : (300,350),
                "5" : (400,350),
                "6" : (500,350),
                "7" : (300,450),
                "8" : (400,450),
                "9" : (500,450)
                }
    return centreOfplace[place]

def getNumberOfPlace(coord: tuple):
    if  200 <= coord[1] <= 300: # check Y
        if 250 <= coord[0] <= 350: # check X
            return "1"
        elif 350 <= coord[0] <= 450:
            return "2"
        elif 450 <= coord[0] <= 550:
            return "3"
    elif  300 <= coord[1] <= 400: # check Y
        if 250 <= coord[0] <= 350: # check X
            return "4"
        elif 350 <= coord[0] <= 450:
            return "5"
        elif 450 <= coord[0] <= 550:
            return "6"
    elif  400 <= coord[1] <= 500: # check Y
        if 250 <= coord[0] <= 350: # check X
            return "7"
        elif 350 <= coord[0] <= 450:
            return "8"
        elif 450 <= coord[0] <= 550:
            return "9"

def drawCross(coord: tuple):
    c = getCenterOfPlace(getNumberOfPlace(coord))
    if occupiedPlace[getNumberOfPlace(coord)] == None and stop:
        pygame.draw.aaline(screen, RED, (c[0] - 50, c[1] - 50),(c[0] + 50, c[1] + 50))
        pygame.draw.aaline(screen, RED, (c[0] + 50, c[1] - 50),(c[0] - 50, c[1] + 50))
        occupiedPlace[getNumberOfPlace(coord)] = "Cross"

def drawZero(coord: tuple):
    c = getCenterOfPlace(getNumberOfPlace(coord))
    if occupiedPlace[getNumberOfPlace(coord)] == None and stop:
        pygame.draw.circle(screen,BLUE,c,45, 3)
        occupiedPlace[getNumberOfPlace(coord)] = "Zero"

def whoWins():
    if stop == False:
        t = pygame.font.Font(None, 50)
        text = t.render(f"{whoWin} won!", 1, PINK)
        screen.blit(text, (350, 600))
    elif stop:
        if all(map(lambda p: True if occupiedPlace[p] != None else False, occupiedPlace)):
            d = pygame.font.Font(None, 50)
            tD = d.render("Draw!", 1, PINK)
            screen.blit(tD, (350, 600))
                
pygame.draw.aaline(screen, WHITE, (250, 300),(550,300))
pygame.draw.aaline(screen, WHITE, (250, 400),(550,400))
pygame.draw.aaline(screen, WHITE, (350, 200),(350,500))
pygame.draw.aaline(screen, WHITE, (450, 200),(450,500))
pygame.display.update()

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                """ 
                Рисуется крестик
                """
                drawCross(event.pos)
                pygame.display.update()
            elif event.button == 3:
                """ 
                Рисуется нолик
                """
                drawZero(event.pos)
                pygame.display.update()
    checkWin()
    whoWins()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
