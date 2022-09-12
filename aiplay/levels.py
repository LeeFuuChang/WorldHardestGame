import pygame
from Build import Walls, Ballz

level_count = 1

def Setup(window, Background_Blocks_Row, Background_Blocks_Column, Wall_color, Check_Point_color):
    global Window, Window_width, Window_height, Background_Blocks_Columns, Background_Blocks_Rows, Wall_Color, Check_Point_Color, Block_Width_and_Height
    Window = window
    Window_width = Window.get_width()
    Window_height = Window.get_height()

    Background_Blocks_Columns = Background_Blocks_Column
    Background_Blocks_Rows = Background_Blocks_Row
    Wall_Color = Wall_color
    Check_Point_Color = Check_Point_color
    Block_Width_and_Height = Window_width//Background_Blocks_Rows

    assert Window_width/Background_Blocks_Columns == Window_height/Background_Blocks_Rows


class Config:
    def __init__(self):
        self.Window = Window
        self.Window_width = self.Window.get_width()
        self.Window_height = self.Window.get_height()

        self.Background_Blocks_Columns = Background_Blocks_Columns
        self.Background_Blocks_Rows = Background_Blocks_Rows
        self.Wall_Color = Wall_Color
        self.Check_Point_Color = Check_Point_Color
        self.Block_Width_and_Height = self.Window_height//self.Background_Blocks_Rows

class Level_one(Config):
    def __init__(self):
        #Super all Const Configs
        super().__init__()

        #Wall configs
        self.Wall_Coords = {
            "Top": [
                (18, 3, 13, 3),
                (13, 4, 6, 4),
                (6, 9, 5, 9),
                (5, 3, 2, 3)
            ],
            "Buttom": [
                (2, 10, 7, 10),
                (7, 9, 14, 9),
                (14, 4, 15, 4),
                (15, 10, 18, 10)
            ],
            "Left": [
                (2, 3, 2, 10),
                (15, 4, 15, 10),
                (13, 3, 13, 4),
                (6, 4, 6, 9)
            ],
            "Right": [
                (7, 10, 7, 9),
                (14, 9, 14, 4),
                (18, 10, 18, 3),
                (5, 9, 5, 3)
            ]
        }

        self.Wall_dict = {
            "Top": Walls(self.Window, (0, 0, 0), self.Block_Width_and_Height, 10),
            "Buttom": Walls(self.Window, (0, 0, 0), self.Block_Width_and_Height, 10),
            "Left": Walls(self.Window, (0, 0, 0), self.Block_Width_and_Height, 10),
            "Right": Walls(self.Window, (0, 0, 0), self.Block_Width_and_Height, 10)
        }



        #Ball configs
        self.Ball_Speed = 2.5

        self.Ball_Border = (6, 14)

        self.Ball_Coords = [
            (6, 4),
            (13, 5),
            (6, 6),
            (13, 7),
            (6, 8)
        ]

        self.Ball_List = {
            "Ball_1": Ballz(self.Window, (0, 0, 255), self.Block_Width_and_Height, self.Block_Width_and_Height//4, self.Ball_Coords[0], "Right", self.Ball_Speed, self.Ball_Border),
            "Ball_2": Ballz(self.Window, (0, 0, 255), self.Block_Width_and_Height, self.Block_Width_and_Height//4, self.Ball_Coords[1], "Left", self.Ball_Speed, self.Ball_Border),
            "Ball_3": Ballz(self.Window, (0, 0, 255), self.Block_Width_and_Height, self.Block_Width_and_Height//4, self.Ball_Coords[2], "Right", self.Ball_Speed, self.Ball_Border),
            "Ball_4": Ballz(self.Window, (0, 0, 255), self.Block_Width_and_Height, self.Block_Width_and_Height//4, self.Ball_Coords[3], "Left", self.Ball_Speed, self.Ball_Border),
            "Ball_5": Ballz(self.Window, (0, 0, 255), self.Block_Width_and_Height, self.Block_Width_and_Height//4, self.Ball_Coords[4], "Right", self.Ball_Speed, self.Ball_Border)
        }

        self.Ball_Distant = {
            "Ball_1": 100,
            "Ball_2": 100,
            "Ball_3": 100,
            "Ball_4": 100,
            "Ball_5": 100
        }



    #Draw background and walls
    def Draw_BackGround_Level_One(self):
        step = 0
        for BackGround_Row in range(0, self.Window_width, self.Block_Width_and_Height):
            for BackGround_Column in range(0, self.Window_height, self.Block_Width_and_Height):
                if step==0:
                    pygame.draw.rect(self.Window, (224, 218, 254), (BackGround_Row, BackGround_Column, self.Block_Width_and_Height, self.Block_Width_and_Height))
                    step += 1
                else:
                    pygame.draw.rect(self.Window, (248, 247, 255), (BackGround_Row, BackGround_Column, self.Block_Width_and_Height, self.Block_Width_and_Height))
                    step = 0
        
        
        self.Start_zone = pygame.draw.rect(self.Window, self.Check_Point_Color , (2*self.Block_Width_and_Height, 3*self.Block_Width_and_Height, 3*self.Block_Width_and_Height, 7*self.Block_Width_and_Height))
        self.Win_zone = pygame.draw.rect(self.Window, self.Check_Point_Color, (15*self.Block_Width_and_Height, 3*self.Block_Width_and_Height, 3*self.Block_Width_and_Height, 7*self.Block_Width_and_Height))
        self.Win_zone_coord = [int((self.Block_Width_and_Height*13)+(self.Block_Width_and_Height//2)), int((self.Block_Width_and_Height*3)+(self.Block_Width_and_Height//2))]

        for Wall_Placement in ["Top", "Buttom", "Left", "Right"]:
            for Coordnate in self.Wall_Coords[Wall_Placement]:
                self.Wall_dict[Wall_Placement].Draw(Coordnate) 
        
        
        return self.Wall_Coords, self.Wall_dict, self.Start_zone, self.Win_zone