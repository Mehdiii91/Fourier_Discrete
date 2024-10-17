import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Ajoutez le répertoire parent (projet-algorithme-[votre_nom]) au chemin Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation1 import dft  # Assurez-vous d'importer votre fonction dft correctement

signal = [0.0, 1.0, 0.0, -1.0]
result = dft(signal)

# Extraire les parties réelle, imaginaire et la magnitude
real_part = [x.real for x in result]
imag_part = [x.imag for x in result]
magnitude = [abs(x) for x in result]

#  espace de fréquences pour les abscisses
frequencies = np.arange(len(result))

# Créer les graphiques
plt.figure(figsize=(12, 8))

# Partie réelle
plt.subplot(3, 1, 1)
plt.stem(frequencies, real_part, use_line_collection=True)
plt.title("Partie réelle des fréquences")
plt.xlabel("Fréquences")
plt.ylabel("Amplitude (réelle)")

# Partie imaginaire
plt.subplot(3, 1, 2)
plt.stem(frequencies, imag_part, use_line_collection=True, linefmt='r', markerfmt='ro')
plt.title("Partie imaginaire des fréquences")
plt.xlabel("Fréquences")
plt.ylabel("Amplitude (imaginaire)")

# Magnitude
plt.subplot(3, 1, 3)
plt.stem(frequencies, magnitude, use_line_collection=True, linefmt='g', markerfmt='go')
plt.title("Magnitude des fréquences")
plt.xlabel("Fréquences")
plt.ylabel("Magnitude")

# espacement entre les graphiques
plt.tight_layout()

plt.show()
