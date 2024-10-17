import cmath
import time

class FastFourierTransform:
    def __init__(self, signal):
        self.signal = signal
        self.n = len(signal)

    def fft(self):
        """Exécute la FFT (récursive) et renvoie le résultat, avec mesure du temps d'exécution."""
        start_time = time.time()  # Démarrer le chronomètre
        result = self._fft_recursive(self.signal)
        end_time = time.time()  # Arrêter le chronomètre
        execution_time = end_time - start_time
        print(f"Signal de taille {self.n} - Temps d'exécution pour FFT : {execution_time} secondes")  # Afficher la taille du signal et le temps
        return result

    def _fft_recursive(self, signal):
        N = len(signal)

        if N == 1:
            return signal

        # Séparation des échantillons pairs et impairs
        even = self._fft_recursive(signal[0::2])
        odd = self._fft_recursive(signal[1::2])

        # Calcul des coefficients de Fourier
        combined = [0] * N
        for k in range(N // 2):
            # Calcul de l'exponentielle complexe (twiddle factor)
            t = cmath.exp(-2j * cmath.pi * k / N) * odd[k]
            combined[k] = even[k] + t
            combined[k + N // 2] = even[k] - t

        return combined

# Tester différents signaux de taille variable
if __name__ == "__main__":
    signals = [
        [1, 2, 3, 4, 5],  # Signal simple (taille 5)
        [0.0, 1.0, 0.0, -1.0],  # Signal sinusoïdal basique (taille 4)
        [cmath.sin(2 * cmath.pi * i / 10) for i in range(100)],  # Signal sinusoïdal (taille 100)
        [1 for _ in range(500)],  # Signal constant (taille 500)
        [0] * 499 + [1] + [0] * 500  # Impulsion (taille 1000)
    ]

    for i, signal in enumerate(signals):
        print(f"\nTest du signal {i + 1} (taille {len(signal)})")  # Afficher la taille du signal
        fft_instance = FastFourierTransform(signal)
        fft_result = fft_instance.fft()
