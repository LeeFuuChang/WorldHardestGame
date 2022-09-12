import pygame

class Little_Thing:
    def __init__(self, window, x, y, width=40, height=40, color=(255, 0, 0), move_speed=1):
        self.Width = width
        self.Height = height
        self.Color = color
        self.Window = window
        self.Speed = move_speed
        self.SELF = pygame.draw.rect(self.Window, self.Color, (x, y, self.Width, self.Height))

        self.Center = [self.SELF.x - int(self.Width/2), self.SELF.y - int(self.Height/2)]
        
        self.Can_UP = True
        self.Can_Down = True
        self.Can_Right = True
        self.Can_Left = True
    
    def Action(self, action):
        if action[pygame.K_UP] and (self.SELF.y - self.Speed) > 0 and self.Can_UP: #UP
            self.SELF.y -= self.Speed
        if action[pygame.K_DOWN] and (self.SELF.y + self.Speed) < (self.Window.get_height()-self.Height) and self.Can_Down: #Down
            self.SELF.y += self.Speed
        if action[pygame.K_RIGHT] and (self.SELF.x + self.Speed) < (self.Window.get_width()-self.Width) and self.Can_Right: #Right
            self.SELF.x += self.Speed
        if action[pygame.K_LEFT] and (self.SELF.x - self.Speed) > 0 and self.Can_Left: #Left
            self.SELF.x -= self.Speed

        self.Center = [self.SELF.x + int(self.Width/2), self.SELF.y + int(self.Height/2)]
    
    def Draw(self):
        self.SELF = pygame.draw.rect(self.Window, (127, 0, 0), (self.SELF.x, self.SELF.y, self.Width, self.Height))
        pygame.draw.rect(self.Window, self.Color, (self.SELF.x+5, self.SELF.y+5, self.Width-10, self.Height-10))
        

        self.Can_UP = True
        self.Can_Down = True
        self.Can_Right = True
        self.Can_Left = True