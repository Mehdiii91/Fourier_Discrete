import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Ajouter le répertoire parent au chemin Python pour accéder aux implémentations
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementations.implementation2 import FastFourierTransform  # Importer la classe FastFourierTransform

class FFTVisualizer:
    def __init__(self, fft_result):
        self.fft_result = fft_result
        self.n = len(fft_result)
        self.fig, self.axs = plt.subplots(3, 1, figsize=(8, 6))

    def visualize(self):
        """Visualise les résultats de la FFT sous forme de graphiques statiques."""
        real_part = [x.real for x in self.fft_result]
        imag_part = [x.imag for x in self.fft_result]
        magnitude = [abs(x) for x in self.fft_result]

        frequencies = np.arange(len(self.fft_result))

        # Partie réelle
        self.axs[0].stem(frequencies, real_part, use_line_collection=True)
        self.axs[0].set_title("Partie réelle des fréquences")
        self.axs[0].set_xlabel("Fréquences")
        self.axs[0].set_ylabel("Amplitude (réelle)")

        # Partie imaginaire
        self.axs[1].stem(frequencies, imag_part, use_line_collection=True, linefmt='r', markerfmt='ro')
        self.axs[1].set_title("Partie imaginaire des fréquences")
        self.axs[1].set_xlabel("Fréquences")
        self.axs[1].set_ylabel("Amplitude (imaginaire)")

        # Magnitude
        self.axs[2].stem(frequencies, magnitude, use_line_collection=True, linefmt='g', markerfmt='go')
        self.axs[2].set_title("Magnitude des fréquences")
        self.axs[2].set_xlabel("Fréquences")
        self.axs[2].set_ylabel("Magnitude")

        plt.tight_layout()
        plt.show()

# utilisation
def run_fft_visualization(signal):
    fft_instance = FastFourierTransform(signal)
    fft_result = fft_instance.fft()
    visualizer = FFTVisualizer(fft_result)
    visualizer.visualize()  
