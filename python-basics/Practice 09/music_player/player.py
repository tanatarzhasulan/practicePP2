"""
player.py — Playlist & playback management layer.
Wraps pygame.mixer so main.py stays clean.
"""
 
import os
import pygame
 
 
class MusicPlayer:
    """Manages a playlist and pygame.mixer playback."""
 
    SUPPORTED = {".mp3", ".wav", ".ogg", ".flac"}
 
    def __init__(self, music_dir: str = "music") -> None:
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self.music_dir  = music_dir
        self.tracks: list[str] = []      # full file paths
        self.index:  int  = 0
        self.playing: bool = False
        self.paused:  bool = False
        self._load_tracks()
 
    # ── Playlist ───────────────────────────────────────────────────────────
    def _load_tracks(self) -> None:
        """Scan music_dir and collect supported audio files."""
        if not os.path.isdir(self.music_dir):
            os.makedirs(self.music_dir, exist_ok=True)
        self.tracks = sorted(
            os.path.join(self.music_dir, f)
            for f in os.listdir(self.music_dir)
            if os.path.splitext(f)[1].lower() in self.SUPPORTED
        )
        self.index = 0
 
    def reload(self) -> None:
        self._load_tracks()
 
    # ── Playback controls ──────────────────────────────────────────────────
    def play(self) -> bool:
        """Start / resume playback of the current track. Returns True on success."""
        if not self.tracks:
            return False
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused  = False
            self.playing = True
            return True
        try:
            pygame.mixer.music.load(self.tracks[self.index])
            pygame.mixer.music.play()
            self.playing = True
            self.paused  = False
            return True
        except pygame.error:
            return False
 
    def stop(self) -> None:
        pygame.mixer.music.stop()
        self.playing = False
        self.paused  = False
 
    def pause(self) -> None:
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused  = True
            self.playing = False
 
    def next_track(self) -> bool:
        if not self.tracks:
            return False
        self.index = (self.index + 1) % len(self.tracks)
        was_playing = self.playing or self.paused
        self.stop()
        if was_playing:
            return self.play()
        return True
 
    def prev_track(self) -> bool:
        if not self.tracks:
            return False
        self.index = (self.index - 1) % len(self.tracks)
        was_playing = self.playing or self.paused
        self.stop()
        if was_playing:
            return self.play()
        return True
 
    # ── State helpers ──────────────────────────────────────────────────────
    def update(self) -> None:
        """Call once per frame: auto-advance when a track ends."""
        if self.playing and not self.paused:
            if not pygame.mixer.music.get_busy():
                self.next_track()
 
    @property
    def track_count(self) -> int:
        return len(self.tracks)
 
    @property
    def current_name(self) -> str:
        if not self.tracks:
            return "— no tracks —"
        return os.path.basename(self.tracks[self.index])
 
    @property
    def position_ms(self) -> int:
        """Current playback position in milliseconds (0 if stopped)."""
        if self.playing:
            return int(pygame.mixer.music.get_pos())   # ms since play()
        return 0
 
    @property
    def status(self) -> str:
        if self.paused:
            return "PAUSED"
        if self.playing:
            return "PLAYING"
        return "STOPPED"
 
    @property
    def volume(self) -> float:
        return pygame.mixer.music.get_volume()
 
    def set_volume(self, v: float) -> None:
        pygame.mixer.music.set_volume(max(0.0, min(1.0, v)))