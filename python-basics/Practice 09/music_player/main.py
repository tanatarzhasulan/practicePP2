"""
Music Player — main.py
Keyboard-driven music player built with pygame.
 
Controls
────────
  P   Play / Pause
  S   Stop
  N   Next track
  B   Back (previous) track
  +   Volume up
  -   Volume down
  R   Reload playlist from ./music/
  Q   Quit
"""
 
import sys
import math
import pygame
from player import MusicPlayer
 
# ── Constants ──────────────────────────────────────────────────────────────
W, H   = 620, 440
FPS    = 30
MUSIC_DIR = "music"
 
# Colour palette
BG       = ( 18,  18,  28)
PANEL    = ( 28,  28,  45)
BORDER   = ( 60,  60, 100)
ACCENT   = (100, 180, 255)
ACCENT2  = (255, 120,  80)
WHITE    = (240, 240, 240)
GREY     = (140, 140, 160)
DARK     = ( 10,  10,  20)
GREEN    = ( 80, 220, 120)
RED_C    = (220,  80,  80)
YELLOW   = (255, 210,  60)
 
 
def fmt_ms(ms: int) -> str:
    s = ms // 1000
    return f"{s // 60:02d}:{s % 60:02d}"
 
 
def draw_rounded_rect(
    surf: pygame.Surface,
    colour: tuple,
    rect: pygame.Rect,
    radius: int = 12,
    border: int = 0,
    border_colour: tuple = (0, 0, 0),
) -> None:
    pygame.draw.rect(surf, colour, rect, border_radius=radius)
    if border:
        pygame.draw.rect(surf, border_colour, rect, border, border_radius=radius)
 
 
def draw_waveform_bar(
    surf: pygame.Surface,
    cx: int,
    cy: int,
    width: int,
    playing: bool,
    frame: int,
) -> None:
    """Animated waveform bars when playing."""
    n_bars  = 20
    bar_w   = 8
    gap     = (width - n_bars * bar_w) // (n_bars - 1)
    x_start = cx - width // 2
    for i in range(n_bars):
        if playing:
            phase  = frame * 0.18 + i * 0.55
            h_bar  = int(10 + 28 * abs(math.sin(phase)))
        else:
            h_bar  = 4
        colour = ACCENT if playing else BORDER
        bx = x_start + i * (bar_w + gap)
        pygame.draw.rect(surf, colour,
                         (bx, cy - h_bar, bar_w, h_bar * 2),
                         border_radius=3)
 
 
def draw_volume_bar(surf: pygame.Surface, rect: pygame.Rect, vol: float) -> None:
    draw_rounded_rect(surf, DARK, rect, 5, 1, BORDER)
    filled = rect.copy()
    filled.width = int(rect.width * vol)
    if filled.width > 0:
        draw_rounded_rect(surf, ACCENT2, filled, 5)
    # knob
    kx = rect.left + int(rect.width * vol)
    pygame.draw.circle(surf, WHITE, (kx, rect.centery), 8)
    pygame.draw.circle(surf, ACCENT2, (kx, rect.centery), 6)
 
 
def draw_ui(
    screen: pygame.Surface,
    player: MusicPlayer,
    fonts: dict,
    frame: int,
    message: str,
) -> None:
    screen.fill(BG)
 
    # ── Top header bar ────────────────────────────────────────────────────
    header = pygame.Rect(0, 0, W, 56)
    draw_rounded_rect(screen, PANEL, header, 0, 1, BORDER)
    title = fonts["title"].render("🎵  Mickey's Music Player", True, ACCENT)
    screen.blit(title, title.get_rect(center=(W // 2, 28)))
 
    # ── Waveform / visualiser ─────────────────────────────────────────────
    draw_waveform_bar(screen, W // 2, 108, 340, player.playing, frame)
 
    # ── Now-playing panel ─────────────────────────────────────────────────
    np_rect = pygame.Rect(40, 130, W - 80, 80)
    draw_rounded_rect(screen, PANEL, np_rect, 12, 2, BORDER)
 
    status_col = {
        "PLAYING": GREEN,
        "PAUSED" : YELLOW,
        "STOPPED": RED_C,
    }.get(player.status, GREY)
 
    status_txt = fonts["mono"].render(f"[ {player.status} ]", True, status_col)
    screen.blit(status_txt, (np_rect.x + 16, np_rect.y + 10))
 
    track_txt = fonts["track"].render(player.current_name, True, WHITE)
    screen.blit(track_txt, (np_rect.x + 16, np_rect.y + 40))
 
    idx_txt = fonts["small"].render(
        f"Track {player.index + 1} / {player.track_count}", True, GREY
    )
    screen.blit(idx_txt, idx_txt.get_rect(right=np_rect.right - 14,
                                           top=np_rect.y + 12))
 
    # ── Progress / time ───────────────────────────────────────────────────
    pos_ms  = player.position_ms
    pos_txt = fonts["mono"].render(f"Elapsed: {fmt_ms(pos_ms)}", True, GREY)
    screen.blit(pos_txt, (np_rect.x + 16, np_rect.bottom + 10))
 
    # Simple progress bar (elapsed; resets each track load)
    prog_rect = pygame.Rect(np_rect.x, np_rect.bottom + 32, np_rect.width, 8)
    draw_rounded_rect(screen, DARK, prog_rect, 4, 1, BORDER)
    # show up to 3 minutes (180 000 ms) full bar
    ratio = min(pos_ms / 180_000, 1.0) if pos_ms else 0
    if ratio > 0:
        fill = prog_rect.copy()
        fill.width = max(8, int(prog_rect.width * ratio))
        draw_rounded_rect(screen, ACCENT, fill, 4)
 
    # ── Volume bar ────────────────────────────────────────────────────────
    vol_label = fonts["small"].render("VOL", True, GREY)
    screen.blit(vol_label, (44, 265))
    vol_rect = pygame.Rect(90, 260, W - 140, 16)
    draw_volume_bar(screen, vol_rect, player.volume)
 
    # ── Controls legend ───────────────────────────────────────────────────
    ctrl_rect = pygame.Rect(40, 295, W - 80, 88)
    draw_rounded_rect(screen, PANEL, ctrl_rect, 12, 2, BORDER)
 
    controls = [
        ("P", "Play/Pause"),
        ("S", "Stop"),
        ("N", "Next"),
        ("B", "Back"),
        ("+", "Vol+"),
        ("-", "Vol-"),
        ("R", "Reload"),
        ("Q", "Quit"),
    ]
    cols, rows = 4, 2
    cw = (ctrl_rect.width - 24) // cols
    for i, (key, label) in enumerate(controls):
        col, row = i % cols, i // cols
        kx = ctrl_rect.x + 12 + col * cw
        ky = ctrl_rect.y + 10 + row * 38
        # Key badge
        badge = pygame.Rect(kx, ky, 28, 26)
        draw_rounded_rect(screen, ACCENT2, badge, 6)
        k_txt = fonts["key"].render(key, True, DARK)
        screen.blit(k_txt, k_txt.get_rect(center=badge.center))
        # Label
        l_txt = fonts["small"].render(label, True, WHITE)
        screen.blit(l_txt, (kx + 34, ky + 4))
 
    # ── Status message ────────────────────────────────────────────────────
    if message:
        msg_txt = fonts["small"].render(message, True, YELLOW)
        screen.blit(msg_txt, msg_txt.get_rect(center=(W // 2, 398)))
 
    # ── Empty-playlist hint ───────────────────────────────────────────────
    if player.track_count == 0:
        hint = fonts["small"].render(
            "Drop MP3/WAV/OGG files into  ./music/  then press R", True, RED_C
        )
        screen.blit(hint, hint.get_rect(center=(W // 2, 418)))
 
 
def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Mickey's Music Player")
    clock  = pygame.time.Clock()
 
    player = MusicPlayer(MUSIC_DIR)
 
    fonts = {
        "title": pygame.font.SysFont("Arial",      20, bold=True),
        "track": pygame.font.SysFont("Arial",      15),
        "mono":  pygame.font.SysFont("Courier New",14),
        "small": pygame.font.SysFont("Arial",      13),
        "key":   pygame.font.SysFont("Arial",      14, bold=True),
    }
 
    frame   = 0
    message = "Welcome! Press P to play." if player.track_count else ""
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.stop()
                pygame.quit()
                sys.exit()
 
            if event.type == pygame.KEYDOWN:
                k = event.key
 
                if k == pygame.K_q:
                    player.stop()
                    pygame.quit()
                    sys.exit()
 
                elif k == pygame.K_p:
                    if player.playing:
                        player.pause()
                        message = "Paused."
                    else:
                        ok = player.play()
                        message = f"Playing: {player.current_name}" if ok \
                                  else "No tracks found!"
 
                elif k == pygame.K_s:
                    player.stop()
                    message = "Stopped."
 
                elif k == pygame.K_n:
                    player.next_track()
                    message = f"→ {player.current_name}"
 
                elif k == pygame.K_b:
                    player.prev_track()
                    message = f"← {player.current_name}"
 
                elif k in (pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS):
                    player.set_volume(player.volume + 0.1)
                    message = f"Volume: {int(player.volume * 100)}%"
 
                elif k in (pygame.K_MINUS, pygame.K_KP_MINUS):
                    player.set_volume(player.volume - 0.1)
                    message = f"Volume: {int(player.volume * 100)}%"
 
                elif k == pygame.K_r:
                    player.reload()
                    message = f"Playlist reloaded — {player.track_count} tracks."
 
        player.update()
        draw_ui(screen, player, fonts, frame, message)
        pygame.display.flip()
        clock.tick(FPS)
        frame += 1
 
 
if __name__ == "__main__":
    main()