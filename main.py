import pygame

pygame.init()

window_w = 800 # window width
window_h = 600 # window height

# create the window and the clock
window = pygame.display.set_mode((window_w, window_h))
clock =  pygame.time.Clock()

# colors
white = (255, 255, 255)

# this function is called when the user closes the window
def game_quit():
    pygame.quit()
    quit()

# main game loop
def game_loop():
    running = True

    while running:
        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_quit()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
