from data.settings import *

class Display(pg.Surface):
    def __init__(self, dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)):
        super().__init__(dimensions)
        
    def new(self, args):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        return self
    
    def event(self, event):
        return -1
