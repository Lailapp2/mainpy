import pygame
import sys
from player import Player

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

songs = ["music/st/track1.mp3", "music/track2.mp3"]
p = Player(songs)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: p.play()
            if event.key == pygame.K_s: p.stop()
            if event.key == pygame.K_n: p.next()
            if event.key == pygame.K_b: p.prev()
    
    screen.fill((200, 200, 200))
    pygame.display.flip()