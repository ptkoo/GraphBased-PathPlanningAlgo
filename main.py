import pygame

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze with Kruskal's Algorithm")

def draw_grid(screen, rows, cols, cell_size):
    for row in range(rows):
        for col in range(cols):
            x = col * cell_size
            y = row * cell_size
            # Draw cell (initially all cells are walls)
            pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size), 1)

def main():
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with black
        screen.fill(BLACK)
        
        # Draw the grid
        draw_grid(screen, ROWS, COLS, CELL_SIZE)
        
        # Update the display
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
