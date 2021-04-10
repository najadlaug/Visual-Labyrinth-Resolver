import pygame
import labs as lb
import time
import keyboard

screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Labyrinth visual resolver")
icon = pygame.image.load('maze.png')
pygame.display.set_icon(icon)
calavera = pygame.image.load('calavera.png')
calaveraMini = pygame.transform.scale(calavera, (40, 40))
screen.fill((38, 38, 38))

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
        y += 40


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
			time.sleep(0.008)

def main():
	start = True
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		if start == True:
			createLab(lb.laberinto0)
			start = False

		drawLabyrinth(lb.laberinto0)

try:
	if __name__ == '__main__':
		main()

except Exception as e:
	print(e)