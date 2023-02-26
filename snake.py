# https://www.pygame.org/docs/ref/transform.html

import random
import pygame
import sys

pygame.init()
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

black = (0, 0, 0)
green = (20, 150, 50)
white = (255, 255, 255)
red = (255, 0, 0)

width = 800
height = 600

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake | Mateusz Izydorczyk")

clock = pygame.time.Clock()

counter = 0


def message(message, x, y, size, color):
    font = pygame.font.Font("assets/vcrosdmono.ttf", size)
    msg = font.render(message, True, color)
    surface.blit(msg, [x, y])
    pygame.display.update()


def gameLoop():
    snake_length = 1
    snake_block = 20
    xpos = 280
    ypos = 300
    isRunning = True
    game_over = False
    isPaused = False
    xchange = 0
    ychange = 0
    food_amount = 0
    direction = int()  # 1 - up, 2 - right, 3 - down, 4 - left
    snake_list = []
    xpos_id = 0
    ypos_id = 1
    direction_id = 2
    are_clicked = 0

    snake_bubble = pygame.image.load('assets/bubble.png')
    snake_bubble_head = pygame.image.load('assets/bubble_head.png')
    snake_bubble_body = pygame.image.load('assets/bubble_body.png')
    snake_bubble_corner = pygame.image.load('assets/bubble_corner.png')
    walls = pygame.image.load("assets/borders.png")
    grass = pygame.image.load("assets/grass.png")

    class food:
        x = int()
        y = int()
        food_list = ["assets/red.png", "assets/orange.png", "assets/magenta.png"]  # feel free to add more

        def create(self, x, y, xsize, ysize, type):
            food.x = x
            food.y = y
            image = pygame.image.load(self.food_list[type])
            image = pygame.transform.scale(image, (xsize, ysize))
            surface.blit(image, (x, y))

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and are_clicked == 0:
                if event.key == pygame.K_UP:
                    if xchange == 0 and ychange == snake_block:
                        pass
                    else:
                        xchange = 0
                        ychange = -snake_block
                        direction = 1
                        are_clicked += 1
                elif event.key == pygame.K_DOWN:
                    if xchange == 0 and ychange == -snake_block:
                        pass
                    else:
                        xchange = 0
                        ychange = snake_block
                        direction = 3
                        are_clicked += 1
                elif event.key == pygame.K_LEFT:
                    if xchange == snake_block and ychange == 0:
                        pass
                    else:
                        xchange = -snake_block
                        ychange = 0
                        direction = 4
                        are_clicked += 1
                elif event.key == pygame.K_RIGHT:
                    if xchange == -snake_block and ychange == 0:
                        pass
                    else:
                        xchange = snake_block
                        ychange = 0
                        direction = 2
                        are_clicked += 1
                elif event.key == pygame.K_ESCAPE:
                    isPaused = True
        are_clicked = 0
        while isPaused: 
            message("Paused", 280, 100, 64, black)
            message("Press ESC to resume", 220, 170, 32, black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPaused = False
        while game_over:
            message("Game over!", 215, 100, 64, black)
            message("Press R to play again", 200, 170, 32, black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        snake_list = []
                        snake_length = 1
                        xpos = 280
                        ypos = 300
                        xchange = 0
                        ychange = 0
                        game_over = False
        # player move
        xpos += xchange
        ypos += ychange

        # background
        surface.blit(grass, (0, 0))

        # snake
        snake_head = [xpos, ypos, direction]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if snake_length == 1:
            for i in snake_list:
                temp = pygame.transform.scale(snake_bubble, (20, 20))
                surface.blit(temp, (i[xpos_id], i[ypos_id]))
        else:
            for i in range(1, len(snake_list) - 1):
                if (snake_list[i][direction_id] == 1 and snake_list[i + 1][direction_id] == 2) or (
                        snake_list[i][direction_id] == 4 and snake_list[i + 1][direction_id] == 3):  # 1 and 4
                    temp = pygame.transform.scale(snake_bubble_corner, (20, 20))
                    temp = pygame.transform.flip(temp, 1, 0)
                elif (snake_list[i][direction_id] == 1 and snake_list[i + 1][direction_id] == 4) or (
                        snake_list[i][direction_id] == 2 and snake_list[i + 1][direction_id] == 3):  # 1 and 2
                    temp = pygame.transform.scale(snake_bubble_corner, (20, 20))
                    temp = pygame.transform.flip(temp, 0, 0)
                elif (snake_list[i][direction_id] == 2 and snake_list[i + 1][direction_id] == 1) or (
                        snake_list[i][direction_id] == 3 and snake_list[i + 1][direction_id] == 4):  # 2 and 3
                    temp = pygame.transform.scale(snake_bubble_corner, (20, 20))
                    temp = pygame.transform.flip(temp, 0, 1)
                elif (snake_list[i][direction_id] == 3 and snake_list[i + 1][direction_id] == 2) or (
                        snake_list[i][direction_id] == 4 and snake_list[i + 1][direction_id] == 1):  # 3 and 4
                    temp = pygame.transform.scale(snake_bubble_corner, (20, 20))
                    temp = pygame.transform.flip(temp, 1, 1)
                else:
                    temp = pygame.transform.scale(snake_bubble_body, (20, 20))
                surface.blit(temp, (snake_list[i][xpos_id], snake_list[i][ypos_id]))

            temp = pygame.transform.scale(snake_bubble_head, (20, 20))
            if snake_list[len(snake_list) - 1][direction_id] == 1:
                temp = pygame.transform.rotate(temp, 90)
            elif snake_list[len(snake_list) - 1][direction_id] == 2:
                temp = pygame.transform.rotate(temp, 0)
            elif snake_list[len(snake_list) - 1][direction_id] == 3:
                temp = pygame.transform.rotate(temp, 270)
            elif snake_list[len(snake_list) - 1][direction_id] == 4:
                temp = pygame.transform.rotate(temp, 180)
            surface.blit(temp, (snake_list[len(snake_list) - 1][xpos_id], snake_list[len(snake_list) - 1][ypos_id]))

            previous = snake_list[1][direction_id]
            temp = pygame.transform.scale(snake_bubble_head, (20, 20))
            if previous == 1:
                temp = pygame.transform.rotate(temp, 270)
            elif previous == 2:
                temp = pygame.transform.rotate(temp, 180)
            elif previous == 3:
                temp = pygame.transform.rotate(temp, 90)
            elif previous == 4:
                temp = pygame.transform.rotate(temp, 0)
            surface.blit(temp, (snake_list[0][xpos_id], snake_list[0][ypos_id]))

        # food
        if food_amount == 0:
            foodonsnake = True
            while foodonsnake:
                foodx = random.randint(1, (800 - 20 - 20) / 20) * 20
                foody = random.randint(1, (600 - 20 - 20) / 20) * 20
                for i in range(0, len(snake_list)):
                    if round(foodx - snake_list[i][xpos_id]) == 0 and round(foody - snake_list[i][ypos_id]) == 0:
                        foodonsnake = True
                        break
                    else:
                        foodonsnake = False
            food_amount += 1
            random_food = random.randint(0, len(food.food_list) - 1)

        food.create(food, foodx, foody, snake_block, snake_block, random_food)
        if round(xpos - food.x) == 0 and round(ypos - food.y) == 0:
            snake_length += 1
            food_amount += -1

        # hitself
        for i in snake_list[:len(snake_list) - 1]:
            if i[xpos_id] == snake_head[xpos_id] and i[ypos_id] == snake_head[ypos_id]:
                game_over = True

        # borders
        surface.blit(walls, (0, 0))
        if xpos > width - 20 - snake_block or xpos < 20 or ypos > height - 20 - snake_block or ypos < 20:
            game_over = True

        # score box
        message("Score:" + str(snake_length - 1), 30, 25, 32, black)

        pygame.display.update()
        clock.tick(15)


gameLoop()
