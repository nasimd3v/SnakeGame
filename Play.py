import time
import pygame, sys, random


class Play:
    def __init__(self, level):
        self.difficulty = level
        pygame.init()
        self.frame_size_x = pygame.display.Info().current_w
        self.frame_size_y = pygame.display.Info().current_h
        self.game_window = pygame.display.set_mode((self.frame_size_x, self.frame_size_y),pygame.FULLSCREEN)

        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        self.fps_controller = pygame.time.Clock()

        self.snake_pos = [100, 50]

        self.snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10,
                         random.randrange(1, (self.frame_size_y // 10)) * 10]
        self.food_spawn = True

        self.direction = 'RIGHT'
        self.change_to = self.direction

        self.score = 0

        def game_over():
            my_font = pygame.font.SysFont('times new roman', 90)
            game_over_surface = my_font.render('Game Over', True, self.red)
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.midtop = (self.frame_size_x/2, self.frame_size_y/4)
            self.game_window.fill(self.black)
            self.game_window.blit(game_over_surface, game_over_rect)
            show_score(0, self.red, 'times', 20)
            pygame.display.flip()
            time.sleep(1)
            pygame.quit()



        # Score
        def show_score(choice, color, font, size):
            score_font = pygame.font.SysFont(font, size)
            score_surface = score_font.render('Score : ' + str(self.score), True, color)
            score_rect = score_surface.get_rect()
            if choice == 1:
                score_rect.midtop = (self.frame_size_x / 10, 15)
            else:
                score_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 1.25)
            self.game_window.blit(score_surface, score_rect)
            pygame.display.flip()

        # Main logic
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Whenever a key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # W -> Up; S -> Down; A -> Left; D -> Right
                    if event.key == pygame.K_UP or event.key == ord('w'):
                        self.change_to = 'UP'
                    if event.key == pygame.K_DOWN or event.key == ord('s'):
                        self.change_to = 'DOWN'
                    if event.key == pygame.K_LEFT or event.key == ord('a'):
                        self.change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT or event.key == ord('d'):
                        self.change_to = 'RIGHT'
                    # Esc -> Create event to quit the game
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Making sure the snake cannot move in the opposite direction instantaneously
            if self.change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'

            # Moving the snake
            if self.direction == 'UP':
                self.snake_pos[1] -= 10
            if self.direction == 'DOWN':
                self.snake_pos[1] += 10
            if self.direction == 'LEFT':
                self.snake_pos[0] -= 10
            if self.direction == 'RIGHT':
                self.snake_pos[0] += 10

            # Snake body growing mechanism
            self.snake_body.insert(0, list(self.snake_pos))
            if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
                self.score += 1
                self.food_spawn = False
            else:
                self.snake_body.pop()

            # Spawning food on the screen
            if not self.food_spawn:
                self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10,
                                 random.randrange(1, (self.frame_size_y // 10)) * 10]
            self.food_spawn = True

            # GFX
            self.game_window.fill(self.black)
            for pos in self.snake_body:
                # Snake body
                # .draw.rect(play_surface, color, xy-coordinate)
                # xy-coordinate -> .Rect(x, y, size_x, size_y)
                pygame.draw.rect(self.game_window, self.green, pygame.Rect(pos[0], pos[1], 10, 10))

            # Snake food
            pygame.draw.rect(self.game_window, self.white, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))

            # Game Over conditions
            # Getting out of bounds
            if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x - 10:
                game_over()
            if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y - 10:
                game_over()
            # Touching the snake body
            for block in self.snake_body[1:]:
                if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                    game_over()

            show_score(1, self.white, 'consolas', 20)
            pygame.display.update()
            self.fps_controller.tick(self.difficulty)
