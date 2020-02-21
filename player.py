
"""
The player in the game
"""
class Player():

    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    # x_move - int of pixels to move horizontally
    # y_move - int of pixels to move vertically
    def movePlayer(self, x_move, y_move):
        self.x += x_move
        self.y += y_move
