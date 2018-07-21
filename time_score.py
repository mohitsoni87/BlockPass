import pygame as pg
import time, random
from pygame.locals import *

pg.init()
car = pg.image.load('download.png')
car_d = car.get_rect().size
car_width = car_d[0];   car_height = car_d[1]
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
display_width = 800; display_height = 600;
pg.display.set_caption('First Game')
clock = pg.time.Clock()
start_time = time.time()
gamedisp = pg.display.set_mode((display_width, display_height))
scores = []
speed = 10
check = 0
count = 0
def text_objects(text, style):
      surface = style.render(text, True, black)
      return surface, surface.get_rect()

def GameOver(Text, TextRect):
      gamedisp.blit(Text, TextRect)
      pg.time.wait(2000)
      start()


def object(x, y, w, h, color):
      pg.draw.rect(gamedisp, blue, [x, y, w, h])
      
def start():
      global speed, count, check
      check = 0
      count = 0
      speed = 10
      x = 361.5
      y = 495
      gamedisp.fill(white)
      gamedisp.blit(car, (x, y))
      gameloop(x, y)

def Text_Formatting(text, font_size):
      style = pg.font.Font('freesansbold.ttf', font_size)
      Text, TextRect = text_objects(text, style)
      return Text, TextRect
      
def crash():
      global start_time
      score = format((time.time() - start_time), '0.2f')
      start_time = time.time()
      text = 'Game over'
      Text, TextRect = Text_Formatting(text, 115)
      TextRect.center = ((400), (300))
      GameOver(Text, TextRect)
      
def score(start):
      score = format((time.time() - start_time), '0.2f')
      score = float(score)
      global speed, check
      if(score > 5 and check == 0):
            speed += 2
            check = 1
      elif(score > 10 and check == 1):
            speed += 4
            check = 2
      elif(score > 15 and check == 2):
            speed += 4
            check = 3
      TEXT = 'Score:  '
      style = pg.font.Font('freesansbold.ttf', 30)
      Text, TextRect = text_objects(TEXT, style)
      TextRect.center = ((650), (50))
      gamedisp.blit(Text, TextRect)
      TEXT = str(score)
      Text, TextRect = text_objects(TEXT, style)
      TextRect.center = ((730), (50))
      gamedisp.blit(Text, TextRect)
      HighScore(score)

def HighScore(score):
      scores.append(float(score))
      highest_score = 'High Score:   '
      Text, TextRect = Text_Formatting(highest_score, 30)
      TextRect.center = ((150), (50))
      gamedisp.blit(Text, TextRect)
      highest_score = str(max(scores))
      Text, TextRect = Text_Formatting(highest_score, 30)
      TextRect.center = ((265), (50))
      gamedisp.blit(Text, TextRect)
      



def change(x, y):
      gamedisp.fill(white)
      gamedisp.blit(car, (x , y))



def gameloop(x, y):
      global count
      crashed = False
      rx = random.randrange(0, 800)
      ry = -300
      w = 100
      h = 100
      while not crashed:
            for event in pg.event.get():
                  if(event.type == QUIT):
                        crashed  = True
                        pg.quit()
                        quit()
                  if(event.type == KEYDOWN):
                        if (event.key == K_RIGHT):
                              x += 50
                              if (x > display_width - car_width):
                                    x = 0
                              
                        elif(event.key == K_LEFT):
                              x -= 50
                              if (x < 0):
                                    x = display_width - car_width
                              
                        elif(event.key == K_DOWN):
                              y += 50
                              if (y > display_height - car_height):
                                    crash()
                                    continue
                              
                        elif(event.key == K_UP):
                              y -= 50
                              if (y < 0):
                                    crash()
                                    continue
            change(x, y)
            object(rx, ry, w, h, black)
            score(start_time)
            
            ry += speed

            if(  ((rx + 100 >= x and rx <= x)  or (rx >= x and rx - 100 <= x) )    and  (ry + 100  >= y)  ):
                  crash()
                  
            if(ry > display_height):
                  count += 1
                  print(count)
                  gameloop(x, y)
                  
            pg.display.update()
            clock.tick(60)
start()

      
              

