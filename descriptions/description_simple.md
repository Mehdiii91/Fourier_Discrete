La Transformation de Fourier discrète (DFT) est un outil mathématique qui permet de décomposer un signal complexe (comme une onde sonore ou une image) en une combinaison de plusieurs ondes plus simples (des sinusoïdes).

Imagine ceci :
Lorsque tu écoutes une chanson, tu entends des sons différents comme des voix, des guitares, des basses, et des tambours. Même si tout cela est mélangé en un seul signal, la DFT te permet de décomposer ce signal en ses différents éléments. Elle te dit quelles sont les fréquences présentes (les notes jouées), et avec quelle intensité (l'amplitude de ces notes).

En termes simples :
Entrée : Tu as un signal, qui est une série de nombres représentant une onde dans le temps.
Sortie : La DFT va te donner un ensemble de fréquences et leur puissance dans le signal. Ces fréquences correspondent aux différentes ondes qui, combinées, donnent le signal d'origine.
Exemple :
Si tu as une simple onde sonore (comme un “do” au piano), la DFT peut te dire que cette onde est composée de plusieurs sinusoïdes. Certaines fréquences seront très fortes (les notes dominantes), tandis que d’autres seront plus faibles (les harmoniques).

Comment ça marche ?
L'algorithme prend ton signal (par exemple une liste de nombres) et, pour chaque fréquence possible, il calcule à quel point cette fréquence est présente dans le signal. Il utilise des calculs basés sur des fonctions sinusoïdales pour y arriver. C’est un peu comme un chef d’orchestre qui écoute tous les instruments et te dit exactement quelle note est jouée par chaque instrument et avec quelle intensité.

En résumé, la DFT te permet de passer d’un signal dans le temps à un signal dans les fréquences. Cela aide beaucoup dans les domaines comme la musique, le traitement d'image, et bien plus encore, car comprendre quelles fréquences sont présentes peut révéler beaucoup d’informations cachées dans un signal.