import os
import colorama
import pygame
import time
import keyboard
from colorama import Back, Fore, Style
from os import system

screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Labyrinth visual resolver")
icon = pygame.image.load('maze.png')
pygame.display.set_icon(icon)
calavera = pygame.image.load('calavera.png')
calavera = pygame.transform.scale(calavera, (30, 30))
crown = pygame.image.load('crown.png')
crown = pygame.transform.scale(crown, (30, 30))
warning = pygame.image.load('warning.png')
warning = pygame.transform.scale(warning, (20, 20))
NoteText = pygame.image.load('NOTE.png')
NoteText = pygame.transform.scale(NoteText, (100, 30))
screen.fill((38, 38, 38))
pygame.display.update()

def explora (laberinto, fila, columna, cont):
    resultado = False
    drawLabyrinth(laberinto)
    time.sleep(0.1)

    if fila == 0 or fila == len(laberinto) or columna == 0 or columna == len(laberinto[0]):
        if cont == 0:
            cont += 1
            print("CONT: ", cont)

        elif cont == 1:
            print("Has llegado al final del camino!")

    try:
        # Pruebo un camino (Sud)
        if laberinto[fila][columna-1] == ".":
            laberinto[fila][columna] = "O"
            resultado = explora(laberinto, fila, columna-1, cont)
            laberinto[fila][columna] = "X"
            resultado = True
            drawLabyrinth(laberinto)
            time.sleep(0.1)

        # Pruebo un camino (Norte)
        if laberinto[fila][columna+1] == ".":
            laberinto[fila][columna] = "O"
            resultado = explora(laberinto, fila, columna+1, cont)
            laberinto[fila][columna] = "X"
            resultado = True
            drawLabyrinth(laberinto)
            time.sleep(0.1)

        # Pruebo un camino (Este)
        if laberinto[fila+1][columna] == ".":
            laberinto[fila][columna] = "O"
            resultado = explora(laberinto, fila+1, columna, cont)
            laberinto[fila][columna] = "X"
            resultado = True
            drawLabyrinth(laberinto)
            time.sleep(0.1)

        # Pruebo un camino (Oeste)
        if laberinto[fila-1][columna] == ".":
            laberinto[fila][columna] = "O"
            resultado = explora(laberinto, fila-1, columna, cont)
            laberinto[fila][columna] = "X"
            resultado = True
            drawLabyrinth(laberinto)
            time.sleep(0.1)

        # Si ningun camino ha ido bien, marco el camino como incorrecto
        if resultado == False:
            laberinto[fila][columna] = "M"

    except:
        laberinto[fila][columna] = "C"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                drawLabyrinth(laberinto)
    return resultado


def createLab(matClean):
    while not keyboard.is_pressed("esc"):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if keyboard.is_pressed("space"):
            mouse = pygame.mouse.get_pos()
            ListMouseX = int(mouse[0] / 40)
            ListMouseY = int(mouse[1] / 40)
            print(ListMouseY, ListMouseX)   
            matClean[ListMouseY][ListMouseX] = "."
            drawLabyrinth(matClean)
            time.sleep(0.0001)

        if keyboard.is_pressed("delete"):
            mouse = pygame.mouse.get_pos()
            ListMouseX = int(mouse[0] / 40)
            ListMouseY = int(mouse[1] / 40)
            print(ListMouseY, ListMouseX)   
            matClean[ListMouseY][ListMouseX] = "*"
            drawLabyrinth(matClean)
            time.sleep(0.0001)

    return matClean


def drawLabyrinth(lista):
    x = 0
    y = 0
    for i in lista:
        x = 0
        for string in i:
            if string == "*":
                pygame.draw.rect(screen, (38, 38, 38), [x, y, 40, 40])

            if string == ".":
                pygame.draw.rect(screen, (0, 176, 246), [x, y, 40, 40])

            if string == "O":
                pygame.draw.rect(screen, (0,128,0), [x, y, 40, 40])

            if string == "X":
                pygame.draw.rect(screen, (110,0,20), [x, y, 40, 40])

            if string == "M":
                pygame.draw.rect(screen, (0,0,0), [x, y, 40, 40])
                screen.blit(calavera, (x+5,y+5))

            if string == "C":
                pygame.draw.rect(screen, (255,255,0), [x, y, 40, 40])
                screen.blit(crown, (x+5,y+5))

            pygame.display.update()
            x += 40
        pygame.display.update()
        y += 40


def drawBox():
    pygame.font.init()
    myfont = pygame.font.SysFont('Helvetica', 14)

    pygame.draw.rect(screen, (16,16,16), [275, 165, 250, 150]) 
    pygame.draw.line(screen, (240,240,240), (275, 165), (525, 165), 3) #UP LINE
    pygame.draw.line(screen, (240,240,240), (275, 165), (275, 315), 3) #LEFT LINE
    pygame.draw.line(screen, (240,240,240), (275, 315), (525, 315), 3) #DOWN LINE
    pygame.draw.line(screen, (240,240,240), (525, 165), (525, 315), 3) #RIGHT LINE

    screen.blit(warning, (300, 180))
    screen.blit(warning, (480, 180))
    screen.blit(NoteText, (350, 175))

    textsurface = myfont.render('- You can only start the Labyrinth up', False, (240, 240, 240))
    screen.blit(textsurface, (285,215))
    textsurface = myfont.render("- You can't finish the Labyrinth up", False, (240, 240, 240))
    screen.blit(textsurface, (285,240))

    textsurface = myfont.render("press enter to continue", False, (240, 240, 240))
    screen.blit(textsurface, (325,280))


def NoteRules():
    ClickedOk = False
    while ClickedOk == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        drawBox()
        pygame.display.update()

        if keyboard.is_pressed('enter'):
            ClickedOk = True
            screen.fill((38, 38, 38))
            pygame.display.update()

def getStartPos(laberinto):
    for i in range(len(laberinto[0])):
        if laberinto[0][i] == ".":
            return i

