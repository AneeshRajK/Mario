import pygame
from pygame.locals import *
import sys


class Input():
    def __init__(self, entity):
        self.mouseX = 0
        self.mouseY = 0
        self.entity = entity

    def checkForInput(self):
        self.checkForKeyboardInput()
        self.checkForMouseInput()
        self.checkForQuitAndRestartInputEvents()

    def checkForKeyboardInput(self):
        pressedKeys = pygame.key.get_pressed()
        if(pressedKeys[K_LEFT] and not pressedKeys[K_RIGHT]):
            self.entity.traits['goTrait'].direction = -1
        elif(pressedKeys[K_RIGHT] and not pressedKeys[K_LEFT]):
            self.entity.traits['goTrait'].direction = 1
        else:
            self.entity.traits['goTrait'].direction = 0
        if(pressedKeys[K_SPACE]):
            self.entity.traits['jumpTrait'].start()
        else:
            self.entity.gravity = 1.25
        if(pressedKeys[K_LSHIFT]):
            self.entity.traits['goTrait'].boost = True
        else:
            self.entity.traits['goTrait'].boost = False

    def checkForMouseInput(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.isRightMouseButtonPressed():
            self.entity.levelObj.addKoopa(
                mouseY / 32, mouseX / 32 - self.entity.camera.pos.x)
            self.entity.levelObj.addGoomba(
                mouseY / 32, mouseX / 32 - self.entity.camera.pos.x)
        if self.isLeftMouseButtonPressed():
            self.entity.levelObj.addCoin(
                mouseX / 32 - self.entity.camera.pos.x, mouseY / 32)

    def checkForQuitAndRestartInputEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.checkIfRestartEvent(event):
                self.entity.restart = True

    def isLeftMouseButtonPressed(self):
        return pygame.mouse.get_pressed()[0]

    def isRightMouseButtonPressed(self):
        return pygame.mouse.get_pressed()[2]

    def checkIfRestartEvent(self, event):
        return (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
        (event.type == pygame.KEYDOWN and event.key == pygame.K_F5)
