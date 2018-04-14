import sys, pygame
import time


size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen, ball, ballrect = [None] * 3

def setup():
    global screen, ball, ballrect
    pygame.init()
    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("ball.gif")
    ballrect = ball.get_rect()


def main():
    global ballrect, last
    setup()
    last = time.time()
    while 1:
        cur = time.time()
        delta = cur - last
        #print(delta)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()
        time.sleep(max(1/60 - delta, 0))
        last = cur



# allows each file to have it's own
# functionality if ran as the main file
if __name__ == "__main__":
    main()
