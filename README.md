# Fourier_Discrete






### Explication du contenu :

# Fourier_Discrete

### Explication du contenu :

**Description** :  
Un résumé du projet expliquant brièvement le fonctionnement de la transformée de Fourier.  
Ce projet implémente deux versions de la transformée de Fourier :  
- **Transformée de Fourier Discrète (DFT)** avec une complexité de O(n²),  
- **Fast Fourier Transform (FFT)** avec une complexité de O(n log n).  

Le projet inclut des tests unitaires et des visualisations pour chaque algorithme.

---

**Structure du Projet** :  
Un aperçu rapide des fichiers importants et de leur fonction.



    Fourier_Discrete/
    ├── README.md
    ├── main.py
    ├── descriptions/
    │   └── description_simple.md
    ├── implementations/
    │   ├── implementation1.py
    │   └── implementation2.py
    ├── tests/
    │   ├── test_implementation1.py
    │   └── test_implementation2.py
    ├── visualisations/
    │   └── visualisation.py
    ├── analyses/
    │   └── analyse_complexite.md
    └── ressources/
        └── [données, images, etc.]

**Instructions d'Utilisation:** Comment cloner et exécuter le projet, ainsi qu'une brève explication des fonctionnalités disponibles dans le menu.



---

**Instructions d'Utilisation :**  
Comment cloner et exécuter le projet, ainsi qu'une brève explication des fonctionnalités disponibles dans le menu.

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/Mehdiii91/Fourier_Discrete
   cd Fourier_Discrete


2. **Exécuter le programme : Lancez main.py pour accéder au menu interactif**:
    ```bash
      python main.py

---
**Axes d'amélioration** : 
1. **Prendre le signal en input de l'utilisateur** :
Actuellement, les signaux sont définis en dur dans le code. Une amélioration notable serait de permettre à l'utilisateur de saisir son propre signal ou de charger un fichier contenant un signal (par exemple, un fichier .csv ou .txt).
- Saisie manuelle du signal : Vous pourriez demander à l'utilisateur d'entrer une liste de valeurs ou d'utiliser une interface pour spécifier le signal.
- Utilisation de input() pour récupérer une chaîne de nombres séparés par des virgules que vous convertirez en liste Python comme ceci par exemple:
  ```bash 
  signal_input = input("Entrez les valeurs du signal séparées par des virgules : ")
  Signal = list(map(float, signal_input.split(',')))
- Chargement de signal depuis un fichier : Permettez à l'utilisateur de charger un fichier contenant un signal numérique.
Exemple avec panda:
    ```bash 
    import pandas as pd
    def load_signal_from_file(file_path):
      data = pd.read_csv(file_path)
      signal = data['signal'].tolist() # Suppose que le fichier a une colonne nommée 'signal'
      return signal

### 2. Amélioration du menu avec une bibliothèque Python

Actuellement, le menu du projet est basique et repose sur des entrées `input()`. Une amélioration majeure serait d'utiliser une bibliothèque Python pour rendre l'interface plus interactive et intuitive. Voici quelques pistes pour rendre le menu plus convivial :

- **`curses`** : Cette bibliothèque standard de Python permet de créer des interfaces utilisateur en mode texte (TUI). Avec `curses`, je pourrais ajouter des sélections interactives, des raccourcis clavier et même des couleurs pour améliorer la navigation dans le menu. Cela rendrait l'interface plus ergonomique tout en restant dans le terminal.
  
  Exemple :
  ```python
  import curses

  def menu(stdscr):
      curses.curs_set(0)
      stdscr.clear()
      stdscr.addstr(0, 0, "Sélectionnez une option :")
      stdscr.addstr(2, 0, "1. Exécuter DFT")
      stdscr.addstr(3, 0, "2. Exécuter FFT")
      stdscr.refresh()

  curses.wrapper(menu)


3. **Amélioration des visualisations** :
- Personnalisation des visualisations : Ajouter des options pour personnaliser les graphiques, comme la possibilité de choisir la couleur des courbes, d'ajouter des légendes, ou de changer les échelles (linéaire vs logarithmique).
- Animation des graphiques : Vous pourriez utiliser `matplotlib.animation` pour montrer l'évolution dynamique de la transformée de Fourier en fonction du temps, ce qui rendrait l'analyse plus visuelle.

Ces améliorations rendraient mon projet plus interactif, plus flexible pour les utilisateurs, et ajouteraient des fonctionnalités intéressantes pour l'analyse de signaux. Elles permettraient également de personnaliser l'expérience utilisateur en offrant la possibilité de fournir des signaux en entrée, d'améliorer le menu avec des bibliothèques Python plus intuitives, et d'apporter des visualisations dynamiques et plus détaillées.

## Planning de réalisation du projet:

**Mercredi après-midi (16h-17h) :**
  - Prise de connaissance du projet,
  - Recherche des différentes formules mathématiques de la transformée de Fourier, notamment la discrète (qui est différente de la rapide),
  - Réflexion sur les moyens de réaliser le projet.

**Jeudi matin (9h-12h30) :**
  - Remise en jambes sur les différents exercices LeetCode,
  - Création de l'arborescence du projet sur GitHub,
  - Rédaction du README avec implémentation du planning,
  - Début du codage de l'algorithme en O(n²) dans le fichier `implementation1.py`,
  - Fin de la matinée : l'algorithme en O(n²) est codé dans `implementation1.py` et le premier fichier de test unitaire `test_implementation1.py` est terminé et opérationnel,
  - Mise à jour en fin de matinée : `visualisation1` est opérationnel.

**Jeudi après-midi (13h-17h) :**
  - Réflexion sur la manière de simplifier l'algorithme afin de réduire sa complexité,
  - Décision de passer de l'algorithme de base (DFT) à la FFT (Fourier rapide), car c'est la seule amélioration possible de l'algorithme,
  - Début du codage de l'algorithme en O(n log n) dans le fichier `implementation2.py`,
  - L'algorithme en O(n log n) est codé dans `implementation2.py` et le deuxième fichier de test unitaire `test_implementation2.py` est terminé et opérationnel,
  - `visualisation2` est opérationnel,
  - Création de `main.py` qui permet de lancer chaque fichier distinctement grâce à un menu implémenté directement dans celui-ci,
  - Finalisation du README pour clôturer le projet.

Ce README est suffisamment complet tout en étant concis et clair pour les utilisateurs potentiels.