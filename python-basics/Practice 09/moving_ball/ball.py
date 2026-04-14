"""
ball.py — Ball entity for the Moving Ball Game.
"""
 
import pygame
 
# Ball constants (spec: 50×50 pixel bounding box, radius 25)
BALL_RADIUS  = 25
BALL_STEP    = 20       # pixels per key press
BALL_COLOUR  = (220, 40, 40)   # red
SHINE_COLOUR = (255, 130, 130) # highlight
 
 
class Ball:
    """A red ball that moves on a bounded 2-D canvas."""
 
    def __init__(self, x: int, y: int, canvas_w: int, canvas_h: int) -> None:
        self.x        = x
        self.y        = y
        self.canvas_w = canvas_w
        self.canvas_h = canvas_h
        self.r        = BALL_RADIUS
        self.step     = BALL_STEP
        # track the last attempted move for feedback
        self.blocked  = False
 
    # ── Movement ───────────────────────────────────────────────────────────
    def _clamp_x(self, new_x: int) -> int:
        return max(self.r, min(self.canvas_w - self.r, new_x))
 
    def _clamp_y(self, new_y: int) -> int:
        return max(self.r, min(self.canvas_h - self.r, new_y))
 
    def move(self, dx: int, dy: int) -> None:
        """
        Attempt to move by (dx, dy).
        If the destination would leave the canvas the move is *ignored*
        (spec: "Ignore input that would move ball off-screen").
        """
        new_x = self.x + dx
        new_y = self.y + dy
        # boundary check — reject the move entirely if it crosses any edge
        if (self.r <= new_x <= self.canvas_w - self.r and
                self.r <= new_y <= self.canvas_h - self.r):
            self.x, self.y = new_x, new_y
            self.blocked   = False
        else:
            self.blocked = True   # flag so UI can flash a warning
 
    def move_up(self)    -> None: self.move( 0, -self.step)
    def move_down(self)  -> None: self.move( 0,  self.step)
    def move_left(self)  -> None: self.move(-self.step, 0)
    def move_right(self) -> None: self.move( self.step, 0)
 
    # ── Rendering ──────────────────────────────────────────────────────────
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the ball with a simple 3-D sheen."""
        cx, cy = self.x, self.y
 
        # Shadow
        pygame.draw.circle(surface, (180, 180, 180),
                           (cx + 4, cy + 5), self.r, 0)
 
        # Body
        pygame.draw.circle(surface, BALL_COLOUR, (cx, cy), self.r)
 
        # Shine highlight
        pygame.draw.circle(surface, SHINE_COLOUR,
                           (cx - self.r // 3, cy - self.r // 3),
                           self.r // 4)
 
        # Outline
        pygame.draw.circle(surface, (120, 20, 20), (cx, cy), self.r, 2)
 
    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.r, self.y - self.r,
                           self.r * 2, self.r * 2)