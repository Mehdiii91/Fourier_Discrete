import cmath  
import math

def dft(x):
    """
    Calcul de la Transformation de Fourier Discrète (DFT) avec complexité O(n^2)
    
    :param x: Liste des échantillons du signal dans le domaine temporel (input signal)
    :return: Liste des coefficients dans le domaine fréquentiel (output signal)
    """
    N = len(x)  
    X = []      

    
    for k in range(N):
        sum_real = 0
        sum_imag = 0
    
        for n in range(N):
            
            angle = -2 * math.pi * k * n / N
            sum_real += x[n] * math.cos(angle)  # Partie réelle
            sum_imag += x[n] * math.sin(angle)  # Partie imaginaire
        
        # On stocke le résultat X[k] sous forme de nombre complexe
        X.append(complex(sum_real, sum_imag))
    
    return X

#utilisation
signal = [0.0, 1.0, 0.0, -1.0]  
frequencies = dft(signal)


for k, freq in enumerate(frequencies):
    print(f"Fréquence {k}: {freq}")
