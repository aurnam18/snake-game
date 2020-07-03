import pygame
import time
import random

# Initalizes pygame
pygame.init()

# Defines colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Defines display width and height
dis_width = 600
dis_height = 400


# Creates display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Sets fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

# A function to display the score of the player on the screen
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# A function to draw the snake on the screen
# Draws a rectangle at every position in snake_list of size snake_block
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# A function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# The main function of the game
def gameLoop():
    game_over = False
    game_close = False

    # START CODING HERE

    # 1. Set x1 and y1 (the position of the block) to the center of the screen
    #snake_block.center(x1, y1)
    x1 = dis_width//2
    y1 = dis_height//2
    # 2. Set x1_change and y1_change to 0 since the snake isn't moving yet
    x1_change = 0
    y1_change = 0
    # A list that will change as the snake gets bigger
    snake_List = []
    # Sets the initial length of the snake to 1
    snake_length = 1

    #Position the food (foodx, foody) to a random location using random module
    foodx = random.random() * dis_width
    foody = random.random() * dis_height
    #While the game is not over
    while not game_over:

        # A loop to determines what happens after the player loses
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # START CODING HERE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # If the user presses an arrow key
            if event.type == pygame.KEYDOWN:

                # 3. Create if-statements that determine how the position of the snake
                #   changes depending on which arrow key is pressed
                #   Hint: Change the variables x1_change and y1_change
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -(snake_block)
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -(snake_block)
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # 4. Check if the position of x1 or y1 is outside of the display
        if x1+snake_block >= dis_width:
            game_close = True
        if y1+snake_block >= dis_height:
            game_close = True
        if x1 < 0:
            game_close = True
        if y1 < 0:
            game_close = True
        # 5. Add the change of the position to the position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # 6. Create an empty list for the current position of the snake
        current_position_of_snake = []
        # 7. Append the current position of the snake to the list
        #    Hint: You're creating a list with the length of two where
        #          [0] is x and [1] is y
        current_position_of_snake.append(x1)
        current_position_of_snake.append(y1)
        # 8. Add the new list you just created to snake_List
        snake_List.append(current_position_of_snake)
        # 9. If the length of snake_List is bigger than the snake_length,
        #   delete the first index of snake_List
        #   NOTE: You want to do this because you want snake_List to only contain
        #       lists of positions on the display that your snake is occupying.
        #       So you're deleting positions your snake has moved off of
        #       (which would be the oldest entry)
        if len(snake_List) > snake_length:
            del snake_List[0]
        # 10. Check if any part of your snake is touching any other part of your snake
        #   If so, end the game
        for x in range(len(snake_List)):
            for y in range(len(snake_List)):
                if x != y and snake_List[x] == snake_List[y]:
                    game_close = True
        our_snake(snake_block, snake_List)
        Your_score(snake_length - 1)

        pygame.display.update()

        # 11. Check if the position of the snake's head matches the position of the food
        #   If so, randomly generate a new food item
        #   And increase the length of the snake by 1
        if (x1+snake_block >= foodx and x1+snake_block <= foodx+snake_block) or (foodx+snake_block >= x1 and foodx+snake_block <= x1+snake_block):
          if (y1+snake_block >= foody and y1+snake_block <= foody+snake_block) or (foody+snake_block >= y1 and foody+snake_block <= y1+snake_block):
            foodx = random.random() * dis_width
            foody = random.random() * dis_height
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
