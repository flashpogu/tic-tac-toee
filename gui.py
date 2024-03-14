import pygame
import sys
pygame.init()

WIDTH = 300
HEIGHT = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up the game board
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Set up the players
player1 = 'X'
player2 = 'O'
current_player = player1

# Set up the font
font = pygame.font.SysFont(None, 60)

# Function to draw the grid lines
def draw_lines():
    pygame.draw.line(window, BLACK, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 2)
    pygame.draw.line(window, BLACK, (2 * WIDTH / 3, 0), (2 * WIDTH / 3, HEIGHT), 2)
    pygame.draw.line(window, BLACK, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 2)
    pygame.draw.line(window, BLACK, (0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), 2)

# Function to draw the X symbol
def draw_x(row, col):
    pygame.draw.line(window, BLACK, (col * WIDTH / 3 + 20, row * HEIGHT / 3 + 20),
                     ((col + 1) * WIDTH / 3 - 20, (row + 1) * HEIGHT / 3 - 20), 2)
    pygame.draw.line(window, BLACK, ((col + 1) * WIDTH / 3 - 20, row * HEIGHT / 3 + 20),
                     (col * WIDTH / 3 + 20, (row + 1) * HEIGHT / 3 - 20), 2)

# Function to draw the O symbol
def draw_o(row, col):
    radius = min(WIDTH, HEIGHT) // 8
    center_x = col * WIDTH // 3 + WIDTH // 6
    center_y = row * HEIGHT // 3 + HEIGHT // 6
    pygame.draw.circle(window, BLACK, (center_x, center_y), radius, 2)

# Function to draw the board
def draw_board():
    for row in range(3):
        for col in range(3):
            if board[row][col] == player1:
                draw_x(row, col)
            elif board[row][col] == player2:
                draw_o(row, col)

# Function to check for a win
def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Main game loop
running = True
while running:
    # Fill the background with white
    window.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not check_win(player1) and not check_win(player2):
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            row = pos[1] // (HEIGHT // 3)
            col = pos[0] // (WIDTH // 3)

            # Update the board if the clicked cell is empty
            if board[row][col] == '':
                board[row][col] = current_player

                # Switch to the other player
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1

    # Draw the grid lines
    draw_lines()

    # Draw the X and O symbols on the board
    draw_board()

    # Check for a win
    if check_win(player1):
        text = font.render("Player X wins!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text, text_rect)
    elif check_win(player2):
        text = font.render("Player O wins!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()