import pygame

class MainWindow():
    
    def __init__(self,w,h):
        self.width = w
        self.height = h
        self.observers = dict()
        
        pygame.init()
        self.screen = pygame.display.set_mode([w,h])
    
    def register(self, ob, callback):
        if callback == None:
            callback = getattr(ob,'notify')

        self.observers[ob] = callback

    def unregister(self, ob):
        del self.observers[ob]
    
    def mainloop(self):

        while True:
            
            event = pygame.event.get()

            for ev in event:
                if ev.type != pygame.NOEVENT:
                    for ob, cb in self.observers.items():
                        cb(ev)
