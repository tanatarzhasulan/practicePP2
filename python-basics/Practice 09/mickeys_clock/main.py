"""
Mickey's Clock — main.py
Displays an analogue clock using Mickey Mouse-style gloved hands.
  Left hand  → seconds
  Right hand → minutes
"""
 
import pygame
import sys
from clock import draw_clock, CLOCK_BG, GOLD, BLACK
 
# ── Constants ──────────────────────────────────────────────────────────────
WINDOW_W  = 520
WINDOW_H  = 560
FPS       = 60          # smooth second-hand sweep
CLOCK_R   = 180         # clock face radius
CLOCK_CX  = WINDOW_W // 2
CLOCK_CY  = WINDOW_H // 2 - 20
BG_TOP    = ( 15,  15,  40)
BG_BOT    = ( 40,  20,  60)
TITLE     = "Mickey's Clock  🕐"
 
 
def draw_gradient_background(surface: pygame.Surface) -> None:
    """Simple vertical gradient for a night-sky feel."""
    h = surface.get_height()
    for y in range(h):
        r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * y / h)
        g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * y / h)
        b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * y / h)
        pygame.draw.line(surface, (r, g, b), (0, y), (WINDOW_W, y))
 
 
def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption(TITLE)
    clock  = pygame.time.Clock()
 
    # Title font
    title_font = pygame.font.SysFont("Arial", 26, bold=True)
 
    while True:
        # ── Events ────────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
 
        # ── Draw ──────────────────────────────────────────────────────────
        draw_gradient_background(screen)
 
        # Title
        title_surf = title_font.render("Mickey's Clock", True, GOLD)
        screen.blit(title_surf, title_surf.get_rect(center=(CLOCK_CX, 28)))
 
        # Clock face + hands
        draw_clock(screen, CLOCK_CX, CLOCK_CY, CLOCK_R)
 
        # Legend
        leg_font = pygame.font.SysFont("Arial", 15)
        for i, (col, text) in enumerate([
            ((230, 230, 230), "Right hand (M) = Minutes"),
            ((180,  30,  30), "Left  hand (S) = Seconds"),
        ]):
            leg = leg_font.render(text, True, col)
            screen.blit(leg, (CLOCK_CX - 110, WINDOW_H - 50 + i * 20))
 
        pygame.display.flip()
        clock.tick(FPS)
 
 
if __name__ == "__main__":
    main()