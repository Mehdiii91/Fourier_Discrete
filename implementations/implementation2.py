import cmath

class FastFourierTransform:
    def __init__(self, signal):
        self.signal = signal
        self.n = len(signal)

    def fft(self):
        """Exécute la FFT (récursive) et renvoie le résultat."""
        return self._fft_recursive(self.signal)

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
