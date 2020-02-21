
import window, game
import pygame as pg
import sys

class Controller():

    def __init__(self):
        self.game = game.Game()
        pass

    def notify(self,event):

        # Quit
        if event.type == pg.QUIT:
            sys.exit()
        # Key up pressed
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                print("You pressed w")

        # Key down pressed
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                print("You pressed s")
        # Key right 
