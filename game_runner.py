from base.important_variables import *
import time


while True:
    start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    game_window.run()
    keyboard.run()
    history_keeper.last_time = velocity_calculator.time


    end_time = time.time()
    velocity_calculator.time = end_time - start_time

