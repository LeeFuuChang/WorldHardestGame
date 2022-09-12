import pygame
from Our_Little_Thing import Little_Thing
import levels
import os
import time


trys = 0

for level in range(levels.level_count):
    keep = True

    while(keep):
        pygame.init()
        pygame.display.set_caption("WorldHardestGame")



        #！！！CONST Values！！！
        Screen_Height = 910 #50X13
        Screen_Width = 1400 #70X20
        Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
        

        Background_Blocks_Rows = 13
        Background_Blocks_Columns = 20


        levels.Setup(Screen, Background_Blocks_Rows, Background_Blocks_Columns, (255,255,255), (158, 242, 155))

            
        Level_List = [
            levels.Level_one()
        ]


        def main():
            global keep

            Agent = Little_Thing(Screen, 225, 435)

            run = True
            a = 0
            while run:



                Screen.fill((170, 165, 255))



                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run=False
                        pygame.quit()



                #Draw walls and background
                Level_List[0].Draw_BackGround_Level_One()



                # Detect wall collision and get user input actions
                if any(Agent.SELF.colliderect(wall) for wall in Level_List[level].Wall_dict["Top"].List):
                    Agent.Can_UP = False

                if any(Agent.SELF.colliderect(wall) for wall in Level_List[level].Wall_dict["Buttom"].List):
                    Agent.Can_Down = False

                if any(Agent.SELF.colliderect(wall) for wall in Level_List[level].Wall_dict["Left"].List):
                    Agent.Can_Left = False
                
                if any(Agent.SELF.colliderect(wall) for wall in Level_List[level].Wall_dict["Right"].List):
                    Agent.Can_Right = False

                key = pygame.key.get_pressed()
                Agent.Action(key)
                Agent.Draw()



                if Agent.SELF.colliderect(Level_List[level].Win_zone):
                    print("Winner！！！")
                    print("You Tried {} times".format(trys))
                    run = False
                    keep = False



                #Handle Ball Movements
                for ball in Level_List[level].Ball_List.keys():
                    Level_List[level].Ball_List[ball].Draw_and_Movement()



                #Ball Collision with the player
                for ball in Level_List[level].Ball_List.keys():
                    #count distant between ball and player
                    #sqrt( (x1 - x2)**2 + (y1 - y2)**2 ) 
                    X_distant = Level_List[level].Ball_List[ball].X_center - Agent.Center[0]
                    Y_distant = Level_List[level].Ball_List[ball].Y_center - Agent.Center[1]

                    Level_List[level].Ball_Distant[ball] = ( X_distant**2 + Y_distant**2 )**0.5
                    if any(distant <= 36.0 for distant in Level_List[level].Ball_Distant.values()):
                        print("Dead")
                        run = False
                            


                #Print out player Coordernate
                a += 1
                if int(a) >= 500:
                    os.system("cls")
                    print("Player:")
                    print(Agent.Center)
                    print("\nDistant:")
                    for item in Level_List[level].Ball_Distant.items():
                        print(item)
                    a = 0

                

                pygame.display.update()



        if __name__ == "__main__":
            main()
            trys += 1