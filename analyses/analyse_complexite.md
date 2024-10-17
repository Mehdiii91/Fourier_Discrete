# Analyse de la Complexité des Algorithmes

## Complexité Théorique

- **DFT** : O(n²)
- **FFT** : O(n log n)

## Résultats Empiriques

Les temps d'exécution suivants ont été mesurés pour différents signaux de tailles variées :

| Taille du signal (n) | Temps DFT (s) | Temps FFT (s)       |
|----------------------|---------------|---------------|
| 4 (Signal sinusoïdal basique)                    | 0.0 secondes    | 0.0 secondes   |
| 5 (signal simple)                  | 0.0010151863098144531 secondes     | 0.0010046958923339844 secondes      |
| 100 (Signal sinusoïdal)                 | 0.004016399383544922 secondes  | 0.0 secondes       |
| 500 (Signal constant)                  | 0.08884310722351074 secondes     | 0.001628875732421875 secondes       |
| 1000 (Impulsion)                | 0.38887596130371094 secondes      | 0.003278493881225586 secondes        |

## Conclusion

La FFT est plus rapide que la DFT pour des signaux de taille importante, confirmant la supériorité de la FFT en termes de performances.
