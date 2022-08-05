import pygame

paddleWidth = 5
paddleHeight = 75
paddleXPos = 20

class Ball:
  def __init__(self, xVel, yVel, x, y, r) -> None:
     self.xVel = xVel
     self.yVel = yVel
     self.x = x
     self.y = y
     self.radius = r
class Player:
  def __init__(self) -> None:
    self.score = 0

def checkPaddleBoundary(left, right, window, paddleHeight):
  if(left.y < 0):
    left.y = 0
  if(left.y > window.get_height() - paddleHeight):
    left.y = window.get_height() - paddleHeight
  if(right.y < 0):
    right.y = 0
  if(right.y > window.get_height() - paddleHeight):
    right.y = window.get_height() - paddleHeight

def checkBallBoundary(ball, window, left, right, leftPlayer, rightPlayer):
  if(ball.y > window.get_height() - ball.radius or ball.y < 0):
    ball.yVel *= -1
  if(ball.x > window.get_width() - ball.radius - paddleXPos):
    ball.x = window.get_width()/2
    ball.y = window.get_height()/2
    leftPlayer.score += 1
  if(ball.x < paddleXPos):
    ball.x = window.get_width()/2
    ball.y = window.get_height()/2
    rightPlayer.score += 1

  #check whether ball hits paddles
  if(ball.x < left.x + paddleWidth and (ball.y < left.y + paddleHeight and ball.y > left.y)):
    ball.xVel *= -1
  if(ball.x > right.x - ball.radius and (ball.y < right.y + paddleHeight and ball.y > right.y)):
    ball.xVel *= -1

def main():  
  pygame.init()
  pygame.font.init()
  leftPlayer = Player()
  rightPlayer = Player()

  my_font = pygame.font.SysFont('Comic Sans MS', 30)
  leftScore = my_font.render(str(leftPlayer.score), False, (255,255,255))
  rightScore = my_font.render(str(rightPlayer.score), False, (255,255,255))
  window = pygame.display.set_mode((600, 400))
  clock = pygame.time.Clock()

  #the ball
  xVel = 3
  yVel = 0.5
  rect = pygame.Rect(0, 0, 20, 20)
  ball = Ball(xVel, yVel, 0, 0, 20)
  
  #paddles
  paddleWidth = 5
  paddleHeight = 75
  leftPaddle = pygame.Rect(paddleXPos, window.get_height()/2 - paddleHeight/2, paddleWidth, paddleHeight)
  rightPaddle = pygame.Rect(window.get_width() - (paddleXPos+paddleWidth), window.get_height()/2 - paddleHeight/2, paddleWidth, paddleHeight)
  rect.center = window.get_rect().center
  ball.x = rect.centerx
  ball.y = rect.centery
  paddleVel = 2

  run = True
  while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    checkPaddleBoundary(leftPaddle, rightPaddle, window, paddleHeight)
    
    leftPaddle.y += (keys[pygame.K_s] - keys[pygame.K_w]) * paddleVel
    rightPaddle.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * paddleVel

    checkBallBoundary(ball,window,leftPaddle,rightPaddle, leftPlayer, rightPlayer)
    ball.x += ball.xVel
    ball.y += ball.yVel
    rect.x = ball.x
    rect.y = ball.y

    leftScore = my_font.render(str(leftPlayer.score), False, (255,255,255))
    rightScore = my_font.render(str(rightPlayer.score), False, (255,255,255))

    window.fill(600)
    pygame.draw.rect(window, (255, 0, 0), rect)
    for i in range(0,11):
      pygame.draw.rect(window, (255,255,255), pygame.Rect(window.get_width()/2, window.get_height() - i*window.get_height()/10, 5, window.get_height()/10-20))

    pygame.draw.rect(window, (255,255,255), leftPaddle)
    pygame.draw.rect(window, (255,255,255), rightPaddle)
    window.blit(leftScore, (window.get_width()/2 - 50,0))
    window.blit(rightScore, (window.get_width()/2 + 50,0))
    pygame.display.flip()

  pygame.quit()
  exit()

main()