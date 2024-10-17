import sys
import os

# Ajoutez le répertoire parent (projet-algorithme-[votre_nom]) au chemin Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementations.implementation1 import dft  # Importer la fonction dft depuis implementation1.py

#test unitaire pour un signal simple
def test_dft_simple():
    signal = [0.0, 1.0, 0.0, -1.0]
    resultat_attendu = [
        complex(0.0, 0.0),  # X[0]
        complex(0.0, -2.0),  # X[1]
        complex(0.0, 0.0),  # X[2]
        complex(0.0, 2.0)  # X[3]
    ]
    ### les résultat on éte calculé a la main (via internet)
    result=dft(signal)

    tolerance = 1e-5  # Ajuster la tolérance
    for i in range(len(result)):
        assert abs(result[i].real - resultat_attendu[i].real) < tolerance
        assert abs(result[i].imag - resultat_attendu[i].imag) < tolerance


#test unitaire pour un signal constant
def test_dft_constant():
    signal = [1.0, 1.0, 1.0, 1.0]
    resultat_attendu=[
        complex(4.0, 0.0),  # X[0] : Somme de 4 fois 1.0
        complex(0.0, 0.0),  # X[1]
        complex(0.0, 0.0),  # X[2]
        complex(0.0, 0.0)   # X[3]
    ]
### les résultat on éte calculé a la main (via internet)
    result=dft(signal)

    tolerance = 1e-5  # Ajuster la tolérance
    for i in range(len(result)):
        assert abs(result[i].real - resultat_attendu[i].real) < tolerance
        assert abs(result[i].imag - resultat_attendu[i].imag) < tolerance