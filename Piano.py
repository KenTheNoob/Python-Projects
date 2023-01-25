import pygame
from random import randint
pygame.init()
pygame.display.set_caption("Piano")
pygame.mouse.set_visible(True)
win = pygame.display.set_mode((840,680))
sheet = pygame.image.load(r'C:\Users\\21kch\\Desktop\\VS Code\\Python\\img\\' + "piano" + '.png')
note = pygame.image.load(r'C:\Users\\21kch\\Desktop\\VS Code\\Python\\img\\' + "note" + '.png')
run = True
correct = False
keypress = ""
random = 0
cleff = 1
key = "d"
treble = {0:"d",1:"e",2:"f",3:"g",4:"a",5:"b",6:"c",7:"d",8:"e",9:"f",10:"g"}
base = {0:"f",1:"g",2:"a",3:"b",4:"c",5:"d",6:"e",7:"f",8:"g",9:"a",10:"b"}
position = 195
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    keypress = "a"
                elif event.key == pygame.K_b:
                    keypress = "b"
                elif event.key == pygame.K_c:
                    keypress = "c"
                elif event.key == pygame.K_d:
                    keypress = "d"
                elif event.key == pygame.K_e:
                    keypress = "e"
                elif event.key == pygame.K_f:
                    keypress = "f"
                elif event.key == pygame.K_g:
                    keypress = "g"
                elif event.key == pygame.K_DOWN:
                    keypress = "down"
                if keypress == key:
                    correct = True
                    print("correct")
                else:
                    print("incorrect")
                keystate = "down"
            if event.type == pygame.KEYUP:
                keypress = ""
                keystate = "up"
    if correct == True and keystate == "up":
        random = randint(0,10)
        cleff = randint(0,1)
        if cleff == 0:
            position = 447
            key = base.get(random)
        if cleff == 1:
            position = 195
            key = treble.get(random)
        correct = False
        keystate == "down"
    win.blit(pygame.transform.scale(sheet, (640, 480)), (100, 100))
    win.blit(pygame.transform.scale(note, (80, 110)), (300, position-13.1*random))
    pygame.time.delay(100)
    pygame.display.update()
pygame.quit()