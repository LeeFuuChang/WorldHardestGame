import pygame
from Our_Little_Thing import Little_Thing
import levels
import os
import time
import neat


pygame.init()
pygame.display.set_caption("WorldHardestGame")



#！！！CONST Values！！！
Screen_Height = 910 #70X13
Screen_Width = 1400 #70X20
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))


Background_Blocks_Rows = 13
Background_Blocks_Columns = 20


levels.Setup(Screen, Background_Blocks_Rows, Background_Blocks_Columns, (255,255,255), (158, 242, 155))

    
Level_List = [
    levels.Level_one()
]

step = 0

def main(genomes, _config):
    global keep, Level_List, step

    Agents = []
    nets = []
    ge = []
    run = True

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, _config)
        nets.append(net)
        Agents.append(Little_Thing(Screen, 225, 435))
        g.fitness = 0
        ge.append(g)

    min_d = 5000000
    min_x = 700
    min_y = 210

    while run:

        Screen.fill((170, 165, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False                                                                                                                                                                                                                                                                                                                                                                                                                                               
                pygame.quit()

        #Draw walls and background
        Level_List[0].Draw_BackGround_Level_One()

        for ball in Level_List[0].Ball_List.keys():
            Level_List[0].Ball_List[ball].Draw_and_Movement()

        for x, Agent in enumerate(Agents):
            # Detect wall collision and get user input actions
            if any(Agent.SELF.colliderect(wall) for wall in Level_List[0].Wall_dict["Top"].List):
                Agent.Can_UP = False

            if any(Agent.SELF.colliderect(wall) for wall in Level_List[0].Wall_dict["Buttom"].List):
                Agent.Can_Down = False

            if any(Agent.SELF.colliderect(wall) for wall in Level_List[0].Wall_dict["Left"].List):
                Agent.Can_Left = False
            
            if any(Agent.SELF.colliderect(wall) for wall in Level_List[0].Wall_dict["Right"].List):
                Agent.Can_Right = False

            if Agent.SELF.colliderect(Level_List[0].Win_zone):
                ge[x].fitness += 50000
                Agents.pop(x)
                nets.pop(x)
                ge.pop(x)

            #Ball Collision with the player
            for ball in Level_List[0].Ball_List.keys():
                #count distant between ball and player
                #sqrt( (x1 - x2)**2 + (y1 - y2)**2 ) 
                X_distant = Level_List[0].Ball_List[ball].X_center - Agent.Center[0]
                Y_distant = Level_List[0].Ball_List[ball].Y_center - Agent.Center[1]

                Level_List[0].Ball_Distant[ball] = ( X_distant**2 + Y_distant**2 )**0.5
                if any(distant <= 36.0 for distant in Level_List[0].Ball_Distant.values()):
                    ge[x].fitness -= 100
                    Agents.pop(x)
                    nets.pop(x)
                    ge.pop(x)
                
            Ball_D_list = list(Level_List[0].Ball_Distant.values())
            Win_zone_coordnates = Level_List[0].Win_zone_coord
            D = ( (Agent.Center[0] - Win_zone_coordnates[0])**2 + (Agent.Center[1] - Win_zone_coordnates[1])**2 )**0.5

            if Agent.Center[1] > min_y:
                min_y = Agent.Center[1]
                ge[x].fitness += 2
                if Level_List[0].Block_Width_and_Height*5 > Level_List[0].Block_Width_and_Height*5:
                    if Agent.Center[1] < min_x:
                        min_x = Agent.Center[1]
                        ge[x].fitness += 4
                    else:
                        ge[x].fitness -= 1
                else:
                    ge[x].fitness -= 1
            else:
                ge[x].fitness -= 1

            output = nets[x].activate((
                Agent.Center[0], Agent.Center[1],
                Win_zone_coordnates[0], Win_zone_coordnates[1],
                D,
                Ball_D_list[0],
                Ball_D_list[1],
                Ball_D_list[2],
                Ball_D_list[3],
                Ball_D_list[4]
            ))
            Agent.Action(output)
            Agent.Draw()

        pygame.display.update()


def Run_Neat(filepath):
    Config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, filepath)

    play = neat.population.Population(Config)

    play.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    play.add_reporter(stats)

    best_player = play.run(main, 50)


if __name__ == "__main__":
    Config_file_path = os.path.join(os.path.dirname(__file__), "config.txt") 
    Run_Neat(Config_file_path)