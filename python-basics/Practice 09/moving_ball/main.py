"""
Moving Ball Game — main.py
 
Controls
────────
  ↑  Move up
  ↓  Move down
  ←  Move left
  →  Move right
  R  Reset ball to centre
  Q  Quit
"""
 
import sys
import pygame
from ball import Ball, BALL_RADIUS, BALL_STEP
 
# ── Window / game settings ─────────────────────────────────────────────────
CANVAS_W  = 640
CANVAS_H  = 480
FPS       = 60
 
# Colours
WHITE       = (255, 255, 255)
BG_COLOUR   = (245, 245, 245)
GRID_COL    = (225, 225, 225)
BORDER_COL  = ( 80,  80, 200)
HUD_BG      = ( 30,  30,  50)
HUD_TEXT    = (200, 220, 255)
WARN_COL    = (255,  80,  50)
INFO_COL    = ( 80, 180,  80)
 
GRID_STEP   = 40     # pixels between grid lines
WARN_FRAMES = 30     # how long the boundary-hit warning flashes
 
 
def draw_grid(surface: pygame.Surface) -> None:
    """Light grid for visual depth."""
    for x in range(0, CANVAS_W, GRID_STEP):
        pygame.draw.line(surface, GRID_COL, (x, 0), (x, CANVAS_H))
    for y in range(0, CANVAS_H, GRID_STEP):
        pygame.draw.line(surface, GRID_COL, (0, y), (CANVAS_W, y))
 
 
def draw_hud(
    surface: pygame.Surface,
    ball: Ball,
    font: pygame.font.Font,
    small: pygame.font.Font,
    warn_timer: int,
) -> None:
    """Heads-up display at the bottom of the screen."""
    hud_rect = pygame.Rect(0, CANVAS_H - 40, CANVAS_W, 40)
    pygame.draw.rect(surface, HUD_BG, hud_rect)
    pygame.draw.line(surface, BORDER_COL, (0, CANVAS_H - 40), (CANVAS_W, CANVAS_H - 40), 2)
 
    pos_txt = font.render(
        f"X: {ball.x:4d}   Y: {ball.y:4d}   Step: {BALL_STEP}px", True, HUD_TEXT
    )
    surface.blit(pos_txt, (12, CANVAS_H - 28))
 
    if warn_timer > 0:
        warn = font.render("⚠  Boundary reached!", True, WARN_COL)
        surface.blit(warn, warn.get_rect(right=CANVAS_W - 12, centery=CANVAS_H - 20))
    else:
        hint = small.render("Arrow keys: move  |  R: reset  |  Q: quit", True,
                             (100, 120, 160))
        surface.blit(hint, hint.get_rect(right=CANVAS_W - 10, centery=CANVAS_H - 20))
 
 
def draw_boundary_wall(surface: pygame.Surface) -> None:
    """Draw the arena border."""
    pygame.draw.rect(surface, BORDER_COL,
                     (0, 0, CANVAS_W, CANVAS_H - 40), 3)
 
 
def main() -> None:
    pygame.init()
    screen     = pygame.display.set_mode((CANVAS_W, CANVAS_H))
    pygame.display.set_caption("Moving Ball Game")
    clock      = pygame.time.Clock()
 
    font_hud   = pygame.font.SysFont("Courier New", 15, bold=True)
    font_small = pygame.font.SysFont("Arial",        13)
 
    # Place ball at canvas centre (excluding HUD strip)
    game_h = CANVAS_H - 40
    ball   = Ball(CANVAS_W // 2, game_h // 2, CANVAS_W, game_h)
 
    warn_timer = 0   # frames remaining for boundary warning
 
    while True:
        # ── Events ────────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
 
            if event.type == pygame.KEYDOWN:
                k = event.key
 
                if k == pygame.K_q or k == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
 
                elif k == pygame.K_r:
                    ball.x, ball.y = CANVAS_W // 2, game_h // 2
                    ball.blocked   = False
                    warn_timer     = 0
 
                elif k == pygame.K_UP:
                    ball.move_up()
                elif k == pygame.K_DOWN:
                    ball.move_down()
                elif k == pygame.K_LEFT:
                    ball.move_left()
                elif k == pygame.K_RIGHT:
                    ball.move_right()
 
                if ball.blocked:
                    warn_timer = WARN_FRAMES
 
        # ── Draw ──────────────────────────────────────────────────────────
        screen.fill(BG_COLOUR)
        draw_grid(screen)
        draw_boundary_wall(screen)
        ball.draw(screen)
        draw_hud(screen, ball, font_hud, font_small, warn_timer)
 
        pygame.display.flip()
        clock.tick(FPS)
 
        if warn_timer > 0:
            warn_timer -= 1
 
 
if __name__ == "__main__":
    main()