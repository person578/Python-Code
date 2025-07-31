import pygame
import sys

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game - Python")

# Colors
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BG = (34, 34, 34)

# Game settings
PADDLE_WIDTH, PADDLE_HEIGHT = 16, 100
BALL_SIZE = 16
PLAYER_X = 24
AI_X = WIDTH - PADDLE_WIDTH - 24

# Initial positions
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ai_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x = 5
ball_speed_y = 3

player_score = 0
ai_score = 0
font = pygame.font.SysFont("monospace", 48)
end_font = pygame.font.SysFont("monospace", 72)
small_font = pygame.font.SysFont("monospace", 28)

clock = pygame.time.Clock()

game_over = False
winner = None  # "player" or "ai"

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = WIDTH // 2 - BALL_SIZE // 2
    ball_y = HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x = 5 if pygame.time.get_ticks() % 2 == 0 else -5
    ball_speed_y = 3 if pygame.time.get_ticks() % 2 == 0 else -3

def ai_move():
    global ai_y
    center = ai_y + PADDLE_HEIGHT // 2
    # AI follows the ball with a slight lag
    if center < ball_y + BALL_SIZE // 2 - 12:
        ai_y += 5
    elif center > ball_y + BALL_SIZE // 2 + 12:
        ai_y -= 5
    # Clamp
    if ai_y < 0: ai_y = 0
    if ai_y > HEIGHT - PADDLE_HEIGHT: ai_y = HEIGHT - PADDLE_HEIGHT

def draw():
    WIN.fill(BG)
    # Middle dashed line
    for y in range(0, HEIGHT, 32):
        pygame.draw.rect(WIN, (85, 85, 85), (WIDTH//2-2, y, 4, 16))
    # Paddles
    pygame.draw.rect(WIN, CYAN, (PLAYER_X, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(WIN, MAGENTA, (AI_X, ai_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    # Ball
    pygame.draw.rect(WIN, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    # Scores
    player_text = font.render(str(player_score), True, WHITE)
    ai_text = font.render(str(ai_score), True, WHITE)
    WIN.blit(player_text, (WIDTH//2 - 80, 20))
    WIN.blit(ai_text, (WIDTH//2 + 45, 20))

    if game_over:
        if winner == "player":
            msg = "YOU WIN"
        else:
            msg = "sorry you lost"
        text_surface = end_font.render(msg, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        WIN.blit(text_surface, text_rect)

        # Optional: Show instruction to quit
        subtext = small_font.render("Press ESC or close the window to exit.", True, WHITE)
        subrect = subtext.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
        WIN.blit(subtext, subrect)
    pygame.display.flip()

def main():
    global player_y, ai_y, ball_x, ball_y, ball_speed_x, ball_speed_y
    global player_score, ai_score, game_over, winner

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Allow pressing ESC to quit after game over
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and game_over:
                    running = False

        # Mouse controls for left paddle
        mouse_y = pygame.mouse.get_pos()[1]
        player_y = mouse_y - PADDLE_HEIGHT // 2
        # Clamp
        if player_y < 0: player_y = 0
        if player_y > HEIGHT - PADDLE_HEIGHT: player_y = HEIGHT - PADDLE_HEIGHT

        if not game_over:
            ai_move()

            # Move ball
            ball_x += ball_speed_x
            ball_y += ball_speed_y

            # Wall collision
            if ball_y < 0:
                ball_y = 0
                ball_speed_y *= -1
            if ball_y + BALL_SIZE > HEIGHT:
                ball_y = HEIGHT - BALL_SIZE
                ball_speed_y *= -1

            # Player paddle collision
            if (ball_x < PLAYER_X + PADDLE_WIDTH and
                ball_y + BALL_SIZE > player_y and
                ball_y < player_y + PADDLE_HEIGHT):
                ball_x = PLAYER_X + PADDLE_WIDTH
                ball_speed_x *= -1
                deltaY = (ball_y + BALL_SIZE / 2) - (player_y + PADDLE_HEIGHT / 2)
                ball_speed_y = int(deltaY * 0.25)

            # AI paddle collision
            if (ball_x + BALL_SIZE > AI_X and
                ball_y + BALL_SIZE > ai_y and
                ball_y < ai_y + PADDLE_HEIGHT):
                ball_x = AI_X - BALL_SIZE
                ball_speed_x *= -1
                deltaY = (ball_y + BALL_SIZE / 2) - (ai_y + PADDLE_HEIGHT / 2)
                ball_speed_y = int(deltaY * 0.25)

            # Score & reset
            if ball_x < 0:
                ai_score += 1
                if ai_score >= 10:
                    game_over = True
                    winner = "ai"
                reset_ball()
            if ball_x + BALL_SIZE > WIDTH:
                player_score += 1
                if player_score >= 10:
                    game_over = True
                    winner = "player"
                reset_ball()

        draw()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()