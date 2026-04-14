import pygame
import math
import datetime
 
 
# ── Colours ────────────────────────────────────────────────────────────────
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)
DARK_GREY  = ( 50,  50,  50)
SKIN       = (255, 220, 177)
GLOVE      = (255, 255, 255)
GLOVE_LINE = (180, 180, 180)
RED        = (200,  30,  30)
YELLOW     = (255, 220,   0)
CLOCK_BG   = ( 30,  30,  60)
GOLD       = (212, 175,  55)
 
 
def draw_mickey_face(surface: pygame.Surface, cx: int, cy: int, r: int) -> None:
    """Draw a simple Mickey face as the clock body."""
    # ── Ears ─────────────────────────────────────────────────────────────
    ear_r = int(r * 0.42)
    pygame.draw.circle(surface, BLACK, (cx - int(r * 0.72), cy - int(r * 0.72)), ear_r)
    pygame.draw.circle(surface, BLACK, (cx + int(r * 0.72), cy - int(r * 0.72)), ear_r)
 
    # ── Clock bezel / face ────────────────────────────────────────────────
    pygame.draw.circle(surface, GOLD,     (cx, cy), r + 6)
    pygame.draw.circle(surface, DARK_GREY,(cx, cy), r + 2)
    pygame.draw.circle(surface, CLOCK_BG, (cx, cy), r)
 
    # ── Hour markers ─────────────────────────────────────────────────────
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        is_five = (i % 5 == 0)
        inner = r - (14 if is_five else 8)
        outer = r - 4
        x1 = cx + int(inner * math.cos(angle))
        y1 = cy + int(inner * math.sin(angle))
        x2 = cx + int(outer * math.cos(angle))
        y2 = cy + int(outer * math.sin(angle))
        colour = GOLD if is_five else (80, 80, 120)
        width  = 3    if is_five else 1
        pygame.draw.line(surface, colour, (x1, y1), (x2, y2), width)
 
    # ── Numeral dots at 12 / 3 / 6 / 9 ──────────────────────────────────
    for i, (lbl, ang) in enumerate(
        [("12", -90), ("3", 0), ("6", 90), ("9", 180)]
    ):
        tx = cx + int((r - 28) * math.cos(math.radians(ang)))
        ty = cy + int((r - 28) * math.sin(math.radians(ang)))
        font = pygame.font.SysFont("Arial", max(14, r // 7), bold=True)
        txt  = font.render(lbl, True, GOLD)
        surface.blit(txt, txt.get_rect(center=(tx, ty)))
 
 
def draw_glove_hand(
    surface: pygame.Surface,
    cx: int, cy: int,
    angle_deg: float,
    length: int,
    thickness: int,
    colour: tuple,
    label: str = "",
) -> None:
    """
    Draw a Mickey-style gloved hand as a clock hand.
    The 'glove' is a filled circle at the tip; the arm tapers from the pivot.
    angle_deg : 0° = 12-o'clock (upward), clockwise positive.
    """
    rad = math.radians(angle_deg - 90)          # convert to math convention
    tip_x = cx + int(length * math.cos(rad))
    tip_y = cy + int(length * math.sin(rad))
 
    # Shadow
    shadow_off = 3
    sx = tip_x + shadow_off
    sy = tip_y + shadow_off
    pygame.draw.line(surface, (0, 0, 0, 80),
                     (cx + shadow_off, cy + shadow_off), (sx, sy), thickness + 2)
 
    # Arm
    pygame.draw.line(surface, colour, (cx, cy), (tip_x, tip_y), thickness)
 
    # Glove knuckle lines
    glove_r = thickness + 8
    pygame.draw.circle(surface, GLOVE, (tip_x, tip_y), glove_r)
    for k in range(3):
        kx = tip_x + int((glove_r - 3) * math.cos(rad + math.radians(-30 + k * 30)))
        ky = tip_y + int((glove_r - 3) * math.sin(rad + math.radians(-30 + k * 30)))
        pygame.draw.line(surface, GLOVE_LINE, (tip_x, tip_y), (kx, ky), 1)
    pygame.draw.circle(surface, GLOVE_LINE, (tip_x, tip_y), glove_r, 2)
 
    # Optional small label near tip
    if label:
        font = pygame.font.SysFont("Arial", 12)
        txt  = font.render(label, True, BLACK)
        surface.blit(txt, txt.get_rect(center=(tip_x, tip_y - glove_r - 8)))
 
 
def draw_clock(surface: pygame.Surface, cx: int, cy: int, r: int) -> None:
    """Render the full clock for the current moment."""
    now  = datetime.datetime.now()
    mins = now.minute
    secs = now.second
 
    # Smooth angles (include sub-second fraction for seconds)
    us      = now.microsecond / 1_000_000
    sec_ang = (secs + us) * 6          # 360° / 60
    min_ang = (mins + secs / 60) * 6   # smooth minute hand too
 
    draw_mickey_face(surface, cx, cy, r)
 
    # LEFT hand  = seconds (thinner, longer, red-ish)
    draw_glove_hand(surface, cx, cy, sec_ang,
                    length=int(r * 0.80), thickness=4,
                    colour=(180, 30, 30), label="S")
 
    # RIGHT hand = minutes (thicker, shorter, white)
    draw_glove_hand(surface, cx, cy, min_ang,
                    length=int(r * 0.62), thickness=7,
                    colour=(230, 230, 230), label="M")
 
    # Centre cap
    pygame.draw.circle(surface, GOLD,  (cx, cy), 10)
    pygame.draw.circle(surface, BLACK, (cx, cy),  5)
 
    # Digital readout below the face
    font_big = pygame.font.SysFont("Courier New", max(22, r // 4), bold=True)
    time_str = now.strftime("%M:%S")
    txt = font_big.render(time_str, True, GOLD)
    surface.blit(txt, txt.get_rect(center=(cx, cy + r + 30)))