import pygame
import os

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('A bit')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
run = True

animation = []

def get_sprite(sprite_name, sprite_scale):
   file_path   = os.path.dirname(__file__)
   sprite_path = os.path.join(file_path, ("sprites/" + sprite_name))
   sp = pygame.image.load(sprite_path)
   sp = pygame.transform.scale(sp, sprite_scale)
   return sp

animation.append(get_sprite('catty.png', (200, 200)))
animation.append(get_sprite('walk-1.png', (200, 200)))
animation.append(get_sprite('walk-2.png', (200, 200)))
#####################################################################


i = 0                   # for task '3*' and '4!'
current = animation[i]  # for task '3*' and '4!'

last_time=0

screen.fill(white)

while run:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
      
       # ###################### 4! #####################
#        keys = pygame.key.get_pressed()
#        screen.fill(white)
#        if keys[pygame.K_LEFT]:
#            current = animation[i]
#            i = i + 1
#            if i == 3:
#                i = 0
#    screen.blit(current, (width/2, height/2))
       #########################################################



  
   ###################################### Завдання 3* #####################################
   
   time_passed_in_ms = pygame.time.get_ticks()
   print("time: ", pygame.time.get_ticks(), " ms")

   if (pygame.time.get_ticks() - last_time) > 200:
       last_time = pygame.time.get_ticks()
       current = animation[i]
       screen.fill(white)
       screen.blit(current, (width/2, height/2))
       i = i + 1
       if i == 3:
           i = 0
   ########################################################################################
  
   pygame.display.update()

pygame.quit()

