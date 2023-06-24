import pygame

#initial game
pygame.init()

#create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adding Sounds")

#load sound effects
sound_1 = pygame.mixer.Sound('sound1.wav')
sound_2 = pygame.mixer.Sound('sound2.wav')

#play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

#change the volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()

#load background music
pygame.mixer.music.load("music.mp3")

#play and stop the music
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(10000)
pygame.mixer.music.stop()

#main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#end the game
pygame.quit()   
