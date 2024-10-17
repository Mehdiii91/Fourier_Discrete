import sys
import os
import subprocess
import numpy as np  

# Ajouter les chemins pour accéder aux fichiers importés
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'implementations')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'visualisations')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

# Importation des fichiers d'implémentation
from implementation1 import dft
from implementation2 import FastFourierTransform
from visualisation1 import run_dft_visualization
from visualisation2 import run_fft_visualization


# Fonction pour exécuter les tests directement
def run_tests():
    # Exécuter test_implementation1.py
    print("Exécution de test_implementation1.py...")
    subprocess.run(["python", "tests/test_implementation1.py"])
    
    # Exécuter test_implementation2.py
    print("Exécution de test_implementation2.py...")
    subprocess.run(["python", "tests/test_implementation2.py"])

# Menu principal
def main():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Exécuter l'implémentation DFT (implementation1.py)")
        print("2. Exécuter l'implémentation FFT (implementation2.py)")
        print("3. Visualiser les résultats de la DFT (visualisation1.py)")
        print("4. Visualiser les résultats de la FFT (visualisation2.py)")
        print("5. Lancer les tests unitaires (test_implementation1.py et test_implementation2.py)")
        print("6. Quitter")
        
        choix = input("Entrez votre choix : ")
        
        if choix == '1':
            # Implémentation DFT après sélection
            signal = np.sin(2 * np.pi * np.arange(0, 1, 0.01) * 5)  # Signal sinusoïdal
 # Exemple de signal
            dft_result = dft(signal)
            print("\nRésultats de la DFT :")
            for i, freq in enumerate(dft_result):
                print(f"Fréquence {i}: {freq}")
            
        elif choix == '2':
            # Implémentation FFT après sélection
            signal = np.sin(2 * np.pi * np.arange(0, 1, 0.01) * 5)  # Signal sinusoïdal
  # Exemple de signal
            fft_instance = FastFourierTransform(signal)
            fft_result = fft_instance.fft()
            print("\nRésultats de la FFT :")
            for i, freq in enumerate(fft_result):
                print(f"Fréquence {i}: {freq}")

        elif choix == '3':
            signal = np.sin(2 * np.pi * np.arange(0, 1, 0.01) * 5)  # Signal sinusoïdal

            run_fft_visualization(signal)

        elif choix == '4':
            
            signal = np.sin(2 * np.pi * np.arange(0, 1, 0.01) * 5)  # Signal sinusoïdal

            run_fft_visualization(signal)

        elif choix == '5':
            run_tests()

        elif choix == '6':
            print("Quitter le programme.")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
