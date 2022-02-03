import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from piecelist import get_piece
from player import play_music, stop_music
import keyboard 
import threading

# mixer config
freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.set_volume(0.8)

if __name__ == "__main__":
    print("Welcome! Guess the composer or type q to go to the next song. CMMD+c to quit.")
    while True:
        piece = get_piece()
        midi_filename = piece[0]

        t1 = threading.Thread(target=play_music, args=(pygame, piece[0],))
        t2 = threading.Thread(target=stop_music, args=(pygame, piece[1], piece[2],))
    
        t1.start()
        t2.start()
    
        t1.join()
        t2.join()
    