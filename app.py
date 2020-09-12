#TODO:
	#New button for menu -> game screen
	#points
	#new file for funks

import pygame
from random import choice

pygame.init()
pygame.font.init()

screen_width = 800
screen_height = 400
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)

#load pics and resize
rock = pygame.image.load("pics/rock.png")
rock = pygame.transform.scale(rock, (100, 100))
paper = pygame.image.load("pics/paper.png")
paper = pygame.transform.scale(paper, (100, 100))
scissors = pygame.image.load("pics/scissors.png")
scissors = pygame.transform.scale(scissors, (100, 100))

def add_pic(hand, pos):
    if hand == "rock":
        screen.blit(rock, pos)
    if hand == "paper":
        screen.blit(paper, pos)
    if hand == "scissors":
        screen.blit(scissors, pos)

def get_random_hand():
    hands = ["rock", "paper", "scissors"]
    return choice(hands)

def new_black_screen():
    screen.fill((0,0,0))

def check_win(player, enemy):
    if (player == "rock" and enemy == "scissors") or (player == "paper" and enemy == "rock") or (player == "scissors" and enemy == "paper"):
        return "player"
    elif player == enemy:
        return "draw"
    else:
        return "enemy"

def last_screen(p_hand, e_hand):

    player_hand = p_hand
    enemy_hand = e_hand
    player_hand_pos = (230, 120)
    enemy_hand_pos = (470, 120)
    winner = check_win(player_hand, enemy_hand)
    
    screen.fill((0,0,0))
    print_text(20, "Play again", (20,20))
    add_pic(player_hand, player_hand_pos)
    add_pic(enemy_hand, enemy_hand_pos)
    print_text(50, "VS", (360,120))

    if winner != "draw":
        print_text(35, f"{winner.capitalize()} wins", (310,250))
    else:
        print_text(35, "Its a DRAW", (295,250))


def game_screen():
    screen.fill((0,0,0))
    print_text(50, "Pick one", (300, 20))
    print_text(35, "Rock", (130, 170))
    print_text(35, "Paper", (130, 240))
    print_text(35, "Scissors", (125, 305))
    

def main_screen():
    screen.fill((0,0,0))
    print_text(50, "Welcome To KPS", (200, 20))
    print_text(30, "New", (370,250))
    print_text(30, "Exit", (370,300))


def print_text(fontsize, text, position):
    fonts = pygame.font.SysFont("Comic Sans MS", int(fontsize))
    text = fonts.render(text, False, (255,255,255))
    screen.blit(text, position)


def clicks(mouse_x,mouse_y):
    #Start
    if (mouse_x > 369 and mouse_x < 430) and (mouse_y > 261 and mouse_y < 287):
        return "start"
    #Exit
    elif (mouse_x > 370 and mouse_x < 430) and (mouse_y > 310 and mouse_y < 338):
        return "exit"
    #Rock
    elif (mouse_x > 130 and mouse_x < 208) and (mouse_y > 178 and mouse_y < 214):
        return "rock"
    #Paper
    elif (mouse_x > 130 and mouse_x < 220) and (mouse_y > 250 and mouse_y < 289):
        return "paper"
    #Scissors
    elif (mouse_x > 128 and mouse_x < 262) and (mouse_y > 317 and mouse_y < 347):
        return "scissors"
    #Newgame
    elif (mouse_x > 20 and mouse_x < 109) and (mouse_y > 25 and mouse_y < 50):
        return "newgame"
    else:
        pass


def current_screen(screen, player_hand=None, enemy_hand=None):
    if screen != "last":
        if screen == "main":
            main_screen()

        if screen == "new":
            new_black_screen()
        
        if screen == "game":
            game_screen()
    else:
        last_screen(player_hand, enemy_hand)

run = True
current = "main"
current_hand = None
current_enemy_hand = None

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            run = False

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            # print(f'x: {mouse_x} y: {mouse_y}')

            if clicks(mouse_x, mouse_y) == "start" and current == "main":
                print("Start pressed...")
                current = "game"

            elif clicks(mouse_x, mouse_y) == "exit" and current == "main":
                print("Exit pressed...")
                run = False

            elif clicks(mouse_x, mouse_y) == "rock" and current == "game":
                print("Rock pressed...")
                current = "last"
                current_hand = "rock"
                current_enemy_hand = get_random_hand()
            
            elif clicks(mouse_x, mouse_y) == "paper" and current == "game":
                print("Paper pressed...")
                current = "last"
                current_hand = "paper"
                current_enemy_hand = get_random_hand()
            
            elif clicks(mouse_x, mouse_y) == "scissors" and current == "game":
                print("Scissors pressed...")
                current = "last"
                current_hand = "scissors"
                current_enemy_hand = get_random_hand()

            elif clicks(mouse_x, mouse_y) == "newgame" and current == "last":
                current = "game"


        if keys[pygame.K_b]:
            current = "main"             
        
    current_screen(current,player_hand=current_hand, enemy_hand=current_enemy_hand)
    pygame.display.update()

pygame.QUIT