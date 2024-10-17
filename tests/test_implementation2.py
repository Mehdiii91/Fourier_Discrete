import unittest
import sys
import os
# Ajoutez le répertoire parent (projet-algorithme-[votre_nom]) au chemin Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from implementations.implementation2 import FastFourierTransform

class TestFFT(unittest.TestCase):

    def test_fft_simple_signal(self):
        signal = [0.0, 1.0, 0.0, -1.0]
        expected_output = [
            complex(0.0, 0.0),  # X[0]
            complex(0.0, -2.0), # X[1]
            complex(0.0, 0.0),  # X[2]
            complex(0.0, 2.0)   # X[3]
        ]

        fft_instance = FastFourierTransform(signal)
        result = fft_instance.fft()

        tolerance = 1e-5
        for i in range(len(result)):
            self.assertAlmostEqual(result[i].real, expected_output[i].real, delta=tolerance)
            self.assertAlmostEqual(result[i].imag, expected_output[i].imag, delta=tolerance)

    def test_fft_constant_signal(self):
        signal = [1.0, 1.0, 1.0, 1.0]
        expected_output = [
            complex(4.0, 0.0),  # X[0]
            complex(0.0, 0.0),  # X[1]
            complex(0.0, 0.0),  # X[2]
            complex(0.0, 0.0)   # X[3]
        ]

        fft_instance = FastFourierTransform(signal)
        result = fft_instance.fft()

        tolerance = 1e-5
        for i in range(len(result)):
            self.assertAlmostEqual(result[i].real, expected_output[i].real, delta=tolerance)
            self.assertAlmostEqual(result[i].imag, expected_output[i].imag, delta=tolerance)

if __name__ == '__main__':
    unittest.main()
