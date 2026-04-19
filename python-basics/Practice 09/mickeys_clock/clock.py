import pygame
import datetime

# --- CONFIG ---
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
PATH = './mickeys_clock/images/'

# --- INIT ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


# --- LOAD IMAGES ---
def load_images():
    clock = pygame.transform.scale(
        pygame.image.load(PATH + 'main_clock.png'),
        (WIDTH, HEIGHT)
    )
    min_hand = pygame.image.load(PATH + 'left_hand.png')
    sec_hand = pygame.image.load(PATH + 'right_hand.png')
    return clock, sec_hand, min_hand


# --- ROTATION FUNCTION ---
def draw_hand(image, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=CENTER)
    screen.blit(rotated, rect)


# --- MAIN LOOP ---
def run_clock():
    clock_img, sec_img, min_img = load_images()
    clock_rect = clock_img.get_rect(center=CENTER)

    running = True
    while running:
        screen.fill("white")

        # Draw clock face
        screen.blit(clock_img, clock_rect)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Time
        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # Angles
        sec_angle = (-6 * seconds) + 95
        min_angle = (-6 * minutes) + 90

        # Draw hands
        draw_hand(sec_img, sec_angle)
        draw_hand(min_img, min_angle)

        pygame.display.flip()

    pygame.quit()


# --- START ---
if __name__ == "__main__":
    run_clock()