import pygame 
from sys import exit 

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sean Ping pong game")
fps = pygame.time.Clock()
Run = True

player_y = screen.get_height()//2 - 70

player = pygame.Rect(10,screen.get_height()//2 - 70, 10,140)
opp = pygame.Rect(screen.get_width() - 20,player_y, 10,140)
ball = pygame.Rect(screen.get_width() // 2 - 15, screen.get_height() // 2 - 15, 30,30)

def ball_animation():
    global ball_speed_x,ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= 800:
        ball_speed_x *= -1 
        
    if ball.colliderect(player) or ball.colliderect(opp):
        ball_speed_x *= -1

def player_animation():
    global player_speed_y
    player.y = player_speed_y
    opp.y = opp_speed_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player_speed_y += 10
    if keys[pygame.K_UP]:
        player_speed_y -= 10
        
    if player.top <= 0:
        player.top = 0 
        
    if player.bottom >= screen.get_height():
        player.bottom = screen.get_height()
  
    
def opp_animation():
    global opp_speed_y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        opp_speed_y -= 10
    if keys[pygame.K_s]:
        opp_speed_y += 10
        
    if opp.top <= 0:
        opp.top = 0
        
    if opp.bottom >= screen.get_height():
        opp.bottom = screen.get_height()
        
    
    
        
ball_speed_x = 4
ball_speed_y = 4
player_speed_y = 0
opp_speed_y = 0 




while Run:
    fps.tick(60)
    pygame.display.flip()
    
    
    screen.fill("Black")
    pygame.draw.rect(screen,"White",player)
    pygame.draw.rect(screen,"White",opp)
    pygame.draw.ellipse(screen,"White",ball)
    pygame.draw.line(screen,"White",(screen.get_width()//2,0), (screen.get_width()//2,600))
    
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    player_animation()
    ball_animation()
    opp_animation()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            Run = False 
    