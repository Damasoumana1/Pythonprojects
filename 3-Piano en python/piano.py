# Fonction pour jouer une note
import msvcrt
import pygame
pygame.mixer.init()
def play_note(note):
    path=f"tunes/{note}.wav"
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

# Dictionnaire des fréquences des notes
FREQUENCIES = {
    'a': 261,  # Do
    's': 293,  # Ré
    'd': 329,  # Mi
    'f': 349,  # Fa
    'g': 392,  # Sol
    'h': 440,  # La
    'j': 493,  # Si
    'k': 523   # Do
}

# Durée de la note en millisecond
duration = 800
# Boucle principale
while True:
    print("Appuyez sur les touches du clavier (a, s, d, f, g, h, j, k) pour jouer du piano.")
    print("Appuyez sur la touche 'q' pour quitter.")

    # Lecture de la touche pressée par l'utilisateur
    key = input().lower()

    if key == 'q':
        break

    play_note(key)
