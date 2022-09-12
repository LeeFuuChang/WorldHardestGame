import pygame

class Walls:
    def __init__(self, Window, Color, Block_W_H, Wall_len):
        assert type(Color) == tuple
        assert Wall_len < Block_W_H/2
        
        self.Window = Window
        self.Color = Color
        self.List = []
        self.Len = 0
        self.Block_W_H = Block_W_H
        self.Wall_len = Wall_len

    def Draw(self, Coord):
        assert type(Coord) == tuple

        X_1, Y_1, X_2, Y_2 = Coord

        assert X_1 == X_2 or Y_1 == Y_2

        if X_1 == X_2:
            if Y_1<Y_2:
                X_start, Y_start, X_end, Y_end = X_1, Y_1, X_2, Y_2
            else:
                X_start, Y_start, X_end, Y_end = X_1, Y_2, X_2, Y_1
        else:
            if X_1<X_2:
                X_start, Y_start, X_end, Y_end = X_1, Y_1, X_2, Y_2
            else:
                X_start, Y_start, X_end, Y_end = X_2, Y_1, X_1, Y_2

        wall = pygame.draw.rect(self.Window, self.Color, (
            X_start*self.Block_W_H - int(self.Wall_len/2), 
            Y_start*self.Block_W_H - int(self.Wall_len/2), 
            abs(X_end-X_start)*self.Block_W_H + self.Wall_len, 
            abs(Y_end-Y_start)*self.Block_W_H + self.Wall_len))
        if wall not in self.List:
            self.List.append(wall)
        self.Len = len(self.List)

class Ballz:
    def __init__(self, Window, Color, Block_W_H, Radius, Coord, First_direct, speed, border):
        assert type(Color) == tuple
        assert type(Coord) == tuple
        assert Block_W_H/2 > Radius
        assert len(Coord) == 2
        assert speed >= 1

        self.Window = Window
        self.Color = Color
        self.List = []
        self.Len = 0
        self.Block_W_H = Block_W_H
        self.Half_Block_W_H = self.Block_W_H/2
        self.Radius = Radius
        self.Speed = speed
        self.Border = border

        self.X_center = int(self.Block_W_H*Coord[0]+self.Half_Block_W_H)
        self.Y_center = int(self.Block_W_H*Coord[1]+self.Half_Block_W_H)
        
        if First_direct.lower() == "left":
            self.Going_Left = True
        else:
            self.Going_Left = False


    def Draw_and_Movement(self, Move=True):
        
        if Move:
            if not self.X_center+self.Speed >= self.Border[1]*self.Block_W_H-self.Radius and not self.Going_Left:
                self.X_center += self.Speed
            else:
                self.Going_Left = True

            if not self.X_center-self.Speed <= self.Border[0]*self.Block_W_H+self.Radius and self.Going_Left:
                self.X_center -= self.Speed
            else:
                self.Going_Left = False

        pygame.draw.circle(self.Window, (0, 0, 75), [self.X_center, self.Y_center], self.Radius+2)
        pygame.draw.circle(self.Window, self.Color, [self.X_center, self.Y_center], self.Radius-2)