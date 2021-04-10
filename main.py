import pygame
import time
from functions import explora, createLab, NoteRules, getStartPos
import labs as lb

def main():  
	NoteRules()
	laberintoJugador = createLab(lb.laberinto0)
	StartX = getStartPos(laberintoJugador)
	StartY = 0
	explora(laberintoJugador, StartY, StartX, 0)


if __name__ == "__main__":
	try:
		main()

	except Exception as e:
		print(e)