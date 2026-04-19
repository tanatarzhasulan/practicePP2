import pygame

# --- CONFIG ---
WIDTH, HEIGHT = 600, 150
PATH = './music_player/music/'

PLAYLIST = [
    'Harmony-of-the-Earth.mp3',
    'scott-buckley-moonlight.mp3',
    'simple-piano-song.mp3',
    'Warm-Memories.mp3'
]

BG_COLOR = (20, 20, 20)
TEXT_COLOR = (0, 255, 180)

# --- INIT ---
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Neon Player')

font = pygame.font.Font(None, 32)


# --- PLAYER CLASS ---
class MusicPlayer:
    def __init__(self):
        self.index = 0
        self.song = PLAYLIST[self.index]
        self.song_surface = None
        self.load_song()

    def load_song(self):
        pygame.mixer.music.load(PATH + self.song)
        pygame.mixer.music.play()
        self.update_text()

    def update_text(self):
        name = self.song.split('.')[0]
        self.song_surface = font.render(name, True, TEXT_COLOR)

    def next(self):
        self.index = (self.index + 1) % len(PLAYLIST)
        self.song = PLAYLIST[self.index]
        self.load_song()

    def prev(self):
        self.index = (self.index - 1) % len(PLAYLIST)
        self.song = PLAYLIST[self.index]
        self.load_song()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()


# --- DRAW UI ---
def draw(player):
    screen.fill(BG_COLOR)

    controls = font.render(
        'P(Pause)  R(Resume)  ←(Prev)  →(Next)',
        True,
        TEXT_COLOR
    )

    screen.blit(player.song_surface, (15, 30))
    screen.blit(controls, (40, HEIGHT - 40))


# --- MAIN LOOP ---
def run():
    clock = pygame.time.Clock()
    player = MusicPlayer()
    running = True

    while running:
        draw(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.pause()

                elif event.key == pygame.K_r:
                    player.resume()

                elif event.key == pygame.K_RIGHT:
                    player.next()

                elif event.key == pygame.K_LEFT:
                    player.prev()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# --- START ---
if __name__ == "__main__":
    run()