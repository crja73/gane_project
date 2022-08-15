import pygame
import time
from win32api import GetSystemMetrics

print(help(pygame))
disable_points = [[250, 100], [300, 100], [250, 150], [300, 150], [350, 150], [250, 200], [300, 200], [350, 200]]
base_1_coords = [[50, 300], [100, 300], [50, 350], [100, 350]]
base_2_coords = [[1100, 500], [1150, 500], [1100, 550], [1150, 550]]


class Game(object):
    def __init__(self):

        self.bg = pygame.image.load("strateg_map.jpg")
        self.user_width = GetSystemMetrics(0)
        self.user_height = GetSystemMetrics(1)
        self.SD = pygame.display.set_mode((self.user_width, self.user_height - 50))
        self.x = 1100
        self.y = 0
        self.main_hero = pygame.image.load('main_hero.png').convert_alpha()
        self.main_hero_2 = pygame.image.load('main_hero_2.png').convert_alpha()
        self.main_hero_right = pygame.image.load('main_hero_right.png').convert_alpha()
        self.main_hero_2_left = pygame.image.load('main_hero_2_left.png').convert_alpha()

        self.x2 = 1150
        self.y2 = 0
        self.mode = 1  #активная моделька, которую и будем перемещать
        self.turn_counter_1 = 0   # счетчик для того, чтобы считать ходы
        self.user_turn_2 = 0    # определение игрока, чей сейчас ход

        self.way = 0  # оба смотрт налево (0 - налево, 1 - направо)
        self.way_2 = 0

        

#-----------------------------------

    def moove_1_yb(self):
        for i in range(10):
            self.y -= 5
            self.draw()
            time.sleep(0.05)

    def moove_1_yf(self):
        for i in range(10):
            self.y += 5
            self.draw()
            time.sleep(0.05)

    def moove_1_xb(self):
        for i in range(10):
            self.x -= 5
            self.draw()
            time.sleep(0.05)

    def moove_1_xf(self):
        for i in range(10):
            self.x += 5
            self.draw()
            time.sleep(0.05)

#-----------------------------------

    def moove_2_yb(self):
        for i in range(10):
            self.y2 -= 5
            self.draw()
            time.sleep(0.05)

    def moove_2_yf(self):
        for i in range(10):
            self.y2 += 5
            self.draw()
            time.sleep(0.05)

    def moove_2_xb(self):
        for i in range(10):
            self.x2 -= 5
            self.draw()
            time.sleep(0.05)
    
    def moove_2_xf(self):
        for i in range(10):
            self.x2 += 5
            self.draw()
            time.sleep(0.05)

#-----------------------------------

    def second_window(self):
        Game_2().run()

    def process_events(self, mode):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if mode == 1:    # ходит main_hero(белый)
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed():
                        if event.key == pygame.K_w and self.y > 0 and (not(self.y - 50 == self.y2 and self.x == self.x2)) and self.turn_counter_1 < 100 and [self.x, self.y - 50] not in disable_points:
                            self.moove_1_yb()
                            self.turn_counter_1 += 1
                            
                        if event.key == pygame.K_s and (not(self.y + 50 == self.y2 and self.x == self.x2)) and self.turn_counter_1 < 100 and self.y < self.user_height - 100 and [self.x, self.y + 50] not in disable_points:
                            self.moove_1_yf()
                            self.turn_counter_1 += 1

                        if event.key == pygame.K_a and self.x > 0 and (not(self.y == self.y2 and self.x - 50 == self.x2)) and self.turn_counter_1 < 100 and self.x != 0 and [self.x - 50, self.y] not in disable_points:
                            self.way = 0   #для поворота налево
                            self.draw()
                            self.moove_1_xb()
                            self.turn_counter_1 += 1
                              
                            
                        if event.key == pygame.K_d and (not(self.y == self.y2 and self.x + 50 == self.x2)) and self.turn_counter_1 < 100 and self.x < self.user_width - 50 and [self.x + 50, self.y] not in disable_points:
                            self.way = 1    # для поворота направо
                            self.draw()
                            self.moove_1_xf()
                            self.turn_counter_1 += 1
                            
                            


                        if event.key == pygame.K_ESCAPE:
                            exit()

            else:   # Ходит main_hero_2(черный)
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed():
                        if event.key == pygame.K_w and self.y2 > 0 and (not(self.y == self.y2 - 50 and self.x == self.x2)) and self.turn_counter_1 < 100 and [self.x2, self.y2 - 50] not in disable_points:
                            self.moove_2_yb()
                            self.turn_counter_1 += 1
                            
                        if event.key == pygame.K_s and (not(self.y == self.y2 + 50 and self.x == self.x2)) and self.turn_counter_1 < 100 and self.y2 < self.user_height - 100 and [self.x2, self.y2 + 50] not in disable_points:
                            self.moove_2_yf()
                            self.turn_counter_1 += 1
                            
                        if event.key == pygame.K_a and self.x2 > 0 and (not(self.y == self.y2 and self.x == self.x2 - 50)) and self.turn_counter_1 < 100 and [self.x2 - 50, self.y2] not in disable_points:
                            self.way_2 = 0  # Для поворота налево
                            self.draw()
                            self.moove_2_xb()
                            self.turn_counter_1 += 1
                            
                            
                        if event.key == pygame.K_d and (not(self.y == self.y2 and self.x == self.x2 + 50)) and self.turn_counter_1 < 100 and self.x2 < self.user_width - 50 and [self.x2 + 50, self.y2] not in disable_points:
                            self.way_2 = 1    # для поворота направо
                            self.draw()
                            self.moove_2_xf()
                            self.turn_counter_1 += 1
                            

                        if event.key == pygame.K_ESCAPE:
                            exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.turn_counter_1 = 0
                    if event.pos[0] > self.x and event.pos[0] < self.x + 50 and event.pos[1] > self.y and event.pos[1] < self.y + 50:
                        self.mode = 1
                    elif event.pos[0] > self.x2 and event.pos[0] < self.x2 + 50 and event.pos[1] > self.y2 and event.pos[1] < self.y2 + 50:
                        self.mode = 2
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed():
                    if event.key == pygame.K_e:
                        if abs(self.x - self.x2) <= 50 and abs(self.y - self.y2) <= 50:
                            
                            self.second_window()
                        elif [self.x, self.y] in base_1_coords or [self.x, self.y] in base_2_coords or [self.x2, self.y2] in base_1_coords or [self.x2, self.y2] in base_2_coords:

                            Base().run()


    def draw(self):
        
        self.SD.blit(self.bg, (0, 0))
        
        


        # line_x = 50
        # line_y = 50
        # for i in range(self.user_width // 50):
        #     pygame.draw.line(self.SD, (0, 0, 0), (line_x, 0), (line_x, self.user_height))
        #     line_x += 50
        # for i in range(self.user_height // 50):
        #     pygame.draw.line(self.SD, (0, 0, 0), (0, line_y), (self.user_width, line_y))
        #     line_y += 50
        if self.mode == 1 and self.way == 0 and self.way_2 == 0:   # если оба смотрят налево
            self.SD.blit(self.main_hero, (self.x, self.y))
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x, self.y, 50, 50), width = 2)
            self.SD.blit(self.main_hero_2_left, (self.x2, self.y2))

        elif self.mode == 1 and self.way == 0 and self.way_2 == 1:   #если main_hero смотрит налево, а main_hero_2 направо
            self.SD.blit(self.main_hero, (self.x, self.y))
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x, self.y, 50, 50), width = 2)
            self.SD.blit(self.main_hero_2, (self.x2, self.y2))

        elif self.mode == 1 and self.way == 1 and self.way_2 == 0:
            self.SD.blit(self.main_hero_right, (self.x, self.y))
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x, self.y, 50, 50), width = 2)
            self.SD.blit(self.main_hero_2_left, (self.x2, self.y2))

        elif self.mode == 1 and self.way == 1 and self.way_2 == 1:
            self.SD.blit(self.main_hero_right, (self.x, self.y))
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x, self.y, 50, 50), width = 2)
            self.SD.blit(self.main_hero_2, (self.x2, self.y2))



        elif self.mode == 2 and self.way_2 == 0 and self.way == 0:
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x2, self.y2, 50, 50), width = 5)
            self.SD.blit(self.main_hero_2_left, (self.x2, self.y2))
            self.SD.blit(self.main_hero, (self.x, self.y))

        elif self.mode == 2 and self.way_2 == 0 and self.way == 1:
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x2, self.y2, 50, 50), width = 5)
            self.SD.blit(self.main_hero_2_left, (self.x2, self.y2))
            self.SD.blit(self.main_hero_right, (self.x, self.y))

        elif self.mode == 2 and self.way_2 == 1 and self.way == 0:
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x2, self.y2, 50, 50), width = 5)
            self.SD.blit(self.main_hero_2, (self.x2, self.y2))
            self.SD.blit(self.main_hero, (self.x, self.y))
        elif self.mode == 2 and self.way_2 == 1 and self.way == 1:
            pygame.draw.rect(self.SD, (255, 0, 0), (self.x2, self.y2, 50, 50), width = 5)
            self.SD.blit(self.main_hero_2, (self.x2, self.y2))
            self.SD.blit(self.main_hero_right, (self.x, self.y))



        pygame.display.flip()

    def run(self):

        while True:
            self.process_events(self.mode)
            self.draw()


class Game_2(Game):
    def __init__(self):
        super().__init__()
        self.point_circle_x = 0   # для отрисовки кругов
        self.point_circle_y = 0
        self.fight_map = pygame.image.load("fight_map.png")

        self.battle_x = 0   # для основного игрока
        self.battle_y = 0


    def draw(self):
        super().__init__()
        self.SD.blit(self.fight_map, (0, 0))

        pygame.draw.ellipse(self.SD, (255, 0, 0), (self.battle_x * 25, self.battle_y * 25 + 4, 25, 20))
        pygame.draw.ellipse(self.SD, (255, 0, 0), (self.point_circle_x * 25, self.point_circle_y * 25 + 4, 25, 20), 2)
        pygame.display.update()

    def battle_moove(self):
        
        if self.point_circle_x > self.battle_x and self.point_circle_y == int(self.battle_y):   # сдвиг на право
            for j in range((self.point_circle_x - int(self.battle_x)) * 4):
                self.battle_x += 0.25
                self.draw()
                time.sleep(0.02)

        elif self.point_circle_x < self.battle_x and self.point_circle_y == int(self.battle_y):   # сдвиг на лево
            for j in range((int(self.battle_x) - self.point_circle_x) * 4):
                self.battle_x -= 0.25
                self.draw()
                time.sleep(0.02)

        elif self.point_circle_y > self.battle_y and self.battle_x == int(self.point_circle_x):    # сдвиг вниз
            for j in range((self.point_circle_y - int(self.battle_y)) * 4):

                self.battle_y += 0.25
                self.draw()
                time.sleep(0.02)

        elif self.battle_y > self.point_circle_y and self.battle_x == self.point_circle_x:   # сдвиг вверх
            for j in range((int(self.battle_y) - self.point_circle_y) * 4):
                self.battle_y -= 0.25
                self.draw()
                time.sleep(0.02)

        elif self.point_circle_x > self.battle_x and self.point_circle_y > self.battle_y:   # сдвиг по диагонали вниз вправо
            while self.point_circle_x != self.battle_x and self.point_circle_y != self.battle_y:
                
                self.battle_x += 0.25
                self.draw()
                time.sleep(0.02)
                self.battle_y += 0.25
                self.draw()
                time.sleep(0.02)

            if self.point_circle_x == self.battle_x:
                for j in range((self.point_circle_y - int(self.battle_y)) * 4):
                    self.battle_y += 0.25
                    self.draw()
                    time.sleep(0.02)
            elif self.point_circle_y == self.battle_y:
                for j in range((self.point_circle_x - int(self.battle_x)) * 4):
                    self.battle_x += 0.25
                    self.draw()
                    time.sleep(0.02)

        elif self.point_circle_x > self.battle_x and self.point_circle_y < self.battle_y:    # сдвиг по диагонали вправо вверх

            while self.point_circle_x != self.battle_x and self.point_circle_y != self.battle_y:
                    
                self.battle_x += 0.25
                self.draw()
                time.sleep(0.02)
                self.battle_y -= 0.25
                self.draw()
                time.sleep(0.02)

            if self.point_circle_x == self.battle_x:
                for j in range((self.point_circle_y - int(self.battle_y)) * 4):
                    self.battle_y -= 0.25
                    self.draw()
                    time.sleep(0.02)
            elif self.point_circle_y == self.battle_y:
                for j in range((self.point_circle_x - int(self.battle_x)) * 4):
                    self.battle_x += 0.25
                    self.draw()
                    time.sleep(0.02)

        elif self.point_circle_x < self.battle_x and self.point_circle_y < self.battle_y:   # сдвиг по диагонали влево вверх

            while self.point_circle_x != self.battle_x and self.point_circle_y != self.battle_y:
                    
                self.battle_x -= 0.25
                self.draw()
                time.sleep(0.02)
                self.battle_y -= 0.25
                self.draw()
                time.sleep(0.02)

            if self.point_circle_x == self.battle_x:
                for j in range((int(self.battle_y) - self.point_circle_y) * 4):
                    self.battle_y -= 0.25
                    self.draw()
                    time.sleep(0.02)
            elif self.point_circle_y == self.battle_y:
                for j in range((int(self.battle_x) - self.point_circle_x) * 4):
                    self.battle_x -= 0.25
                    self.draw()
                    time.sleep(0.02)

        elif self.point_circle_x < self.battle_x and self.point_circle_y > self.battle_y:   # сдвиг по диагонали влево вниз

            while self.point_circle_x != self.battle_x and self.point_circle_y != self.battle_y:
                    
                self.battle_x -= 0.25
                self.draw()
                time.sleep(0.02)
                self.battle_y += 0.25
                self.draw()
                time.sleep(0.02)

            if self.point_circle_x == self.battle_x:
                for j in range((self.point_circle_y - int(self.battle_y)) * 4):
                    self.battle_y += 0.25
                    self.draw()
                    time.sleep(0.02)
            elif self.point_circle_y == self.battle_y:
                for j in range((int(self.battle_x) - self.point_circle_x) * 4):
                    self.battle_x -= 0.25
                    self.draw()
                    time.sleep(0.02)



    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed():
                    if event.key == pygame.K_ESCAPE:
                        self.flag = False

            if event.type == pygame.MOUSEMOTION:
                self.point_circle_x = event.pos[0] // 25
                self.point_circle_y = event.pos[1] // 25

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.battle_moove()
                

    def run(self):
        super().__init__()
        self.flag = True
        while self.flag:
            self.process_event()
            self.draw()
           

class Base(Game):
    def __init__(self):
        super().__init__()
        self.flag = True


    def process_event(self):
        super().__init__()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed():
                    if event.key == pygame.K_ESCAPE:
                        self.flag = False

    def draw(self):
        super().__init__()
        self.SD.fill((255, 255, 255))
        pygame.display.update()

    def run(self):
        super().__init__()
        self.flag = True
        while self.flag:
            self.process_event()
            self.draw()



def main():
    pygame.init()
    game = Game()
    game.run()

if __name__ == '__main__':
    main()