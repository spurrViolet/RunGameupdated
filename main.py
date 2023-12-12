import random
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Go Go Reindeer!')


def menu():
    image = pygame.image.load("IMG_5531.png")
    image = pygame.transform.scale(image, (640, 480))
    while True:
        screen.blit(image, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(300, 325) and event.pos[1] in range(220, 228):
                    game()
def game():
    image = pygame.image.load("360_F_183288609_fXtejjyDNOg3uKLfgWDKteEEHYDtW3C2.png")
    image = pygame.transform.scale(image, (640, 480))
    bgx = 0

    player = pygame.image.load("christmas-sleigh-with-gifts-and-deer-in-pixel-art-style-santa-s-new-year-s-reindeer-cart-png.png")
    player = pygame.transform.rotozoom(player, 0, 0.12)
    player_y = 240
    gravity = .1
    jumpcount = 0
    jump =0

    tree = pygame.image.load("christmas-watercolor-snowy-winter-pine-tree-png.png")
    tree = pygame.transform.rotozoom(tree,0, .05)
    tree_x = 700
    tree_speed = .3
    while True:
        screen.blit(image, (bgx-640, 0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))

        bgx = bgx-.3
        if bgx <= -640:
            bgx=0

        p_rect = screen.blit(player, (30, player_y))
        if player_y < 240:
            player_y += gravity
        if jump == 1:
            player_y = player_y -4
            jumpcount +=1
            if jumpcount>40:
                jumpcount =0
                jump =0
        t_rect = screen.blit(tree,(tree_x, 360))
        tree_x -= tree_speed
        if tree_x< -50:
            tree_x = random.randint(700,800)
            tree_speed = random.randint(2, 5)



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                print('jump')
                jump = 1

menu()
game()
