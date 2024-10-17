import math
import time

def dft(x):
    """
    Calcul de la Transformation de Fourier Discrète (DFT) avec complexité O(n^2)
    
    :param x: Liste des échantillons du signal dans le domaine temporel (input signal)
    :return: Liste des coefficients dans le domaine fréquentiel (output signal)
    """
    N = len(x)
    X = []

    start_time = time.time()  # Démarrer le chronomètre

    for k in range(N):
        sum_real = 0
        sum_imag = 0

        for n in range(N):
            angle = -2 * math.pi * k * n / N
            sum_real += x[n] * math.cos(angle)  # Partie réelle
            sum_imag += x[n] * math.sin(angle)  # Partie imaginaire

        # On stocke le résultat X[k] sous forme de nombre complexe
        X.append(complex(sum_real, sum_imag))

    end_time = time.time()  # Arrêter le chronomètre
    execution_time = end_time - start_time
    print(f"Signal de taille {N} - Temps d'exécution pour DFT : {execution_time} secondes")  # Afficher la taille du signal et le temps

    return X

# Tester différents signaux de taille variable
if __name__ == "__main__":
    signals = [
        [1, 2, 3, 4, 5],  # Signal simple (taille 5)
        [0.0, 1.0, 0.0, -1.0],  # Signal sinusoïdal basique (taille 4)
        [math.sin(2 * math.pi * i / 10) for i in range(100)],  # Signal sinusoïdal (taille 100)
        [1 for _ in range(500)],  # Signal constant (taille 500)
        [0] * 499 + [1] + [0] * 500  # Impulsion (taille 1000)
    ]

    for i, signal in enumerate(signals):
        print(f"\nTest du signal {i + 1} (taille {len(signal)})")  # Afficher la taille du signal
        dft_result = dft(signal)
