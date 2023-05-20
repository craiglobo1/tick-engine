import pygame as pg

class UI_Container:
    def __init__(self, pos : tuple = (0,0), size : tuple = (0,0), surf : pg = None, visible=True) -> None:
        self.pos = pos
        self.size = size
        self.surf = surf
        self.visible = visible
        self.hover = False

        # its a datatype with pos and size together and used for collision detection
        self.rect = pg.Rect(*self.pos, *self.size)

        # if clicked pos will be assigned if left mouse button pressed 
        self.clicked : tuple = None 
    
    #NOTE: look at pygame docs for get_pressed for mouse button under pygame.mouse
    def update(self, mouse_buttons : tuple , mouse_pos : tuple):
        
        # update rect
        self.rect.x, self.rect.y = self.pos
        
        # update clicked 
        if mouse_buttons[0]:
            self.clicked = mouse_pos
        else:
            self.clicked = None

        if self.rect.collidepoint(mouse_pos):
            self.hover = True
        
class Button(UI_Container):
    def __init__(self, pos: tuple = (0, 0), size: tuple = (0, 0), surf: tuple = None, visible=True) -> None:
        super().__init__(pos, size, surf, visible)
        self.size = (50,100)
        self.surf = pg.surface.Surface(size)
        self.surf.fill(pg.Color(255,0,0))

    def update(self, mouse_buttons: tuple, mouse_pos: tuple):
        super().update(mouse_buttons, mouse_pos)


    