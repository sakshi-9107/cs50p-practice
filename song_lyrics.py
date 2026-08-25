"""
Song Lyrics Typewriter Effect (with Audio)
-------------------------------------------
Plays an audio file while printing song lyrics to the terminal
line-by-line, character-by-character, like a typewriter/karaoke effect.

Setup:
    pip install pygame

Replace SONG_TITLE, AUDIO_FILE, and the lyrics list below with your own.
For the timing to line up with the music, set each entry in `lyrics`
to (line_text, start_time_in_seconds).
"""

import time
import sys
import os

try:
    import pygame
except ImportError:
    pygame = None

# ---- CONFIG ----
SONG_TITLE = "HALKA HALKA SONG LYRICS"
AUDIO_FILE = "halka_halka.mp3"   # path to your audio file (mp3/wav/ogg)
TYPING_SPEED = 0.07               # seconds per character (lower = faster)
START_DELAY = 2                   # pause before typing/audio starts

# Each line paired with the second (from playback start) it should begin typing.
# Adjust these timestamps to match the actual song.
lyrics = [
    ("Kisi Ne Na Kiya Hai Jaisa Ishq Tera Mera...", 0),
    ("Me Daudta Aata Hoon Koi Naam Le Jo Tera...", 5),
    ("Kisi Ne Na Kiya Hai Jaisa Ishq Tera Mera...", 10),
    ("Mere Ghamon Ki Raat Ka Tu Ujla Savera...", 15),
]


def type_line(line: str, speed: float = TYPING_SPEED):
    """Print a single line one character at a time."""
    for char in line:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()  # newline after the line finishes


def print_header(title: str, width: int = 60):
    print("=" * width)
    print(f"✨ {title} ✨".center(width))
    print("=" * width)
    print()


def start_audio(path: str):
    """Start playing the audio file in the background. Returns True if playing."""
    if pygame is None:
        print("[!] pygame not installed — run 'pip install pygame' for audio.")
        return False
    if not os.path.exists(path):
        print(f"[!] Audio file not found: {path} — continuing without audio.")
        return False

    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    return True


def main():
    print_header(SONG_TITLE)
    time.sleep(START_DELAY)

    audio_playing = start_audio(AUDIO_FILE)
    playback_start = time.time()

    for line, target_time in lyrics:
        if audio_playing:
            # Wait until it's time for this line, based on audio playback clock
            elapsed = time.time() - playback_start
            wait = target_time - elapsed
            if wait > 0:
                time.sleep(wait)
        type_line(line)

    # Let the audio finish if it's still playing
    if audio_playing:
        while pygame.mixer.music.get_busy():
            time.sleep(0.2)
        pygame.mixer.quit()

    print()
    print("💗")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        if pygame is not None:
            pygame.mixer.quit()
        sys.exit(0)