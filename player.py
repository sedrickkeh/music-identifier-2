import pygame
import unidecode

def check_correct(guess, ans):
    if guess.lower() == unidecode.unidecode(ans.lower()):
        return True
    if guess.lower() == unidecode.unidecode(ans.lower()).replace('-', ' '):
        return True
    return False

def play_music(pygame, midi_filename):
  '''Stream music_file in a blocking manner'''
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    clock.tick(30) # check if playback has finished

def stop_music(pygame, ans, piece):
    print("\nEnter answer:")
    while True:
        guess = input()
        if guess == "q":
            print(f"The correct answer was: {ans}")
            print(f"The piece is {piece}")
            break
        elif check_correct(guess, ans):
            print("Correct!")
            print(f"The piece is {piece}")
            break
        else:
            print("X")
    pygame.mixer.music.stop()