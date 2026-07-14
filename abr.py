"""
==========================================================================
 Arbre Binaire de Recherche (ABR) - Parcours, Recherche et Améliorations
==========================================================================
Projet : Structures de données
Langage : Python (POO, aucune bibliothèque externe de structure de données)

Fonctionnalités implémentées :
    - Insertion
    - Recherche (itérative)
    - Parcours infixe   (gauche, racine, droite)   -> ordre croissant
    - Parcours préfixe  (racine, gauche, droite)
    - Parcours postfixe (gauche, droite, racine)
    - Parcours par niveau (largeur / BFS) -- amélioration
    - Suppression d'un noeud (3 cas)      -- amélioration
    - Hauteur de l'arbre                  -- amélioration
    - Comptage du nombre de noeuds        -- amélioration
    - Recherche du minimum / maximum      -- amélioration
    - Vérification d'équilibre (AVL-like) -- amélioration
    - Affichage graphique en mode texte   -- amélioration
==========================================================================
"""

from collections import deque


class Noeud:
    """Représente un noeud de l'arbre binaire de recherche."""

    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

    def __repr__(self):
        return f"Noeud({self.valeur})"


class ArbreBinaireRecherche:
    """Arbre Binaire de Recherche (ABR) implémenté en POO, sans bibliothèque externe."""

    def __init__(self):
        self.racine = None
        self.nb_noeuds = 0

    # ------------------------------------------------------------------
    # INSERTION
    # ------------------------------------------------------------------
    def inserer(self, valeur):
        """Insère une valeur dans l'arbre (ignore les doublons)."""
        if self.racine is None:
            self.racine = Noeud(valeur)
            self.nb_noeuds += 1
            return True

        courant = self.racine
        while True:
            if valeur == courant.valeur:
                return False  # doublon : on n'insère pas
            elif valeur < courant.valeur:
                if courant.gauche is None:
                    courant.gauche = Noeud(valeur)
                    self.nb_noeuds += 1
                    return True
                courant = courant.gauche
            else:
                if courant.droite is None:
                    courant.droite = Noeud(valeur)
                    self.nb_noeuds += 1
                    return True
                courant = courant.droite

    # ------------------------------------------------------------------
    # RECHERCHE
    # ------------------------------------------------------------------
    def rechercher(self, valeur):
        """Retourne True si la valeur est présente dans l'arbre, sinon False."""
        courant = self.racine
        while courant is not None:
            if valeur == courant.valeur:
                return True
            elif valeur < courant.valeur:
                courant = courant.gauche
            else:
                courant = courant.droite
        return False

    # ------------------------------------------------------------------
    # PARCOURS INFIXE (gauche - racine - droite) => ordre croissant
    # ------------------------------------------------------------------
    def parcours_infixe(self):
        resultat = []

        def _parcours(noeud):
            if noeud is not None:
                _parcours(noeud.gauche)
                resultat.append(noeud.valeur)
                _parcours(noeud.droite)

        _parcours(self.racine)
        return resultat

    # ------------------------------------------------------------------
    # PARCOURS PRÉFIXE (racine - gauche - droite)
    # ------------------------------------------------------------------
    def parcours_prefixe(self):
        resultat = []

        def _parcours(noeud):
            if noeud is not None:
                resultat.append(noeud.valeur)
                _parcours(noeud.gauche)
                _parcours(noeud.droite)

        _parcours(self.racine)
        return resultat

    # ------------------------------------------------------------------
    # PARCOURS POSTFIXE (gauche - droite - racine)
    # ------------------------------------------------------------------
    def parcours_postfixe(self):
        resultat = []

        def _parcours(noeud):
            if noeud is not None:
                _parcours(noeud.gauche)
                _parcours(noeud.droite)
                resultat.append(noeud.valeur)

        _parcours(self.racine)
        return resultat

    # ------------------------------------------------------------------
    # AMÉLIORATION 1 : PARCOURS PAR NIVEAU (largeur / BFS)
    # ------------------------------------------------------------------
    def parcours_largeur(self):
        if self.racine is None:
            return []
        resultat = []
        file = deque([self.racine])
        while file:
            noeud = file.popleft()
            resultat.append(noeud.valeur)
            if noeud.gauche:
                file.append(noeud.gauche)
            if noeud.droite:
                file.append(noeud.droite)
        return resultat

    # ------------------------------------------------------------------
    # AMÉLIORATION 2 : SUPPRESSION (3 cas classiques)
    # ------------------------------------------------------------------
    def supprimer(self, valeur):
        self.racine, supprime = self._supprimer_recursif(self.racine, valeur)
        if supprime:
            self.nb_noeuds -= 1
        return supprime

    def _supprimer_recursif(self, noeud, valeur):
        if noeud is None:
            return noeud, False

        if valeur < noeud.valeur:
            noeud.gauche, supprime = self._supprimer_recursif(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droite, supprime = self._supprimer_recursif(noeud.droite, valeur)
        else:
            supprime = True
            # Cas 1 : feuille (aucun enfant)
            if noeud.gauche is None and noeud.droite is None:
                return None, True
            # Cas 2 : un seul enfant
            if noeud.gauche is None:
                return noeud.droite, True
            if noeud.droite is None:
                return noeud.gauche, True
            # Cas 3 : deux enfants -> on remplace par le successeur
            # (le plus petit noeud du sous-arbre droit)
            successeur = noeud.droite
            while successeur.gauche is not None:
                successeur = successeur.gauche
            noeud.valeur = successeur.valeur
            noeud.droite, _ = self._supprimer_recursif(noeud.droite, successeur.valeur)

        return noeud, supprime

    # ------------------------------------------------------------------
    # AMÉLIORATION 3 : HAUTEUR DE L'ARBRE
    # ------------------------------------------------------------------
    def hauteur(self):
        def _hauteur(noeud):
            if noeud is None:
                return -1
            return 1 + max(_hauteur(noeud.gauche), _hauteur(noeud.droite))

        return _hauteur(self.racine)

    # ------------------------------------------------------------------
    # AMÉLIORATION 4 : NOMBRE DE NOEUDS
    # ------------------------------------------------------------------
    def compter_noeuds(self):
        return self.nb_noeuds

    # ------------------------------------------------------------------
    # AMÉLIORATION 5 : MIN / MAX
    # ------------------------------------------------------------------
    def minimum(self):
        if self.racine is None:
            return None
        courant = self.racine
        while courant.gauche is not None:
            courant = courant.gauche
        return courant.valeur

    def maximum(self):
        if self.racine is None:
            return None
        courant = self.racine
        while courant.droite is not None:
            courant = courant.droite
        return courant.valeur

    # ------------------------------------------------------------------
    # AMÉLIORATION 6 : VÉRIFICATION D'ÉQUILIBRE (style AVL)
    # Un arbre est équilibré si, pour chaque noeud, la différence de
    # hauteur entre les sous-arbres gauche et droit est <= 1.
    # ------------------------------------------------------------------
    def est_equilibre(self):
        def _verifier(noeud):
            if noeud is None:
                return True, -1
            eq_g, h_g = _verifier(noeud.gauche)
            eq_d, h_d = _verifier(noeud.droite)
            equilibre = eq_g and eq_d and abs(h_g - h_d) <= 1
            hauteur = 1 + max(h_g, h_d)
            return equilibre, hauteur

        equilibre, _ = _verifier(self.racine)
        return equilibre

    # ------------------------------------------------------------------
    # AMÉLIORATION 7 : AFFICHAGE GRAPHIQUE EN MODE TEXTE (console)
    # ------------------------------------------------------------------
    def afficher(self):
        """Affiche l'arbre de façon lisible dans la console (vue pivotée à 90°,
        la racine à gauche, le sous-arbre droit en haut)."""
        def _afficher(noeud, prefixe="", est_racine=True, est_gauche=False):
            if noeud is None:
                return
            _afficher(noeud.droite, prefixe + ("    " if est_racine else ("│   " if est_gauche else "    ")), False, False)
            if est_racine:
                print(str(noeud.valeur))
            else:
                connecteur = "└── " if est_gauche else "┌── "
                print(prefixe + connecteur + str(noeud.valeur))
            _afficher(noeud.gauche, prefixe + ("    " if est_racine else ("    " if est_gauche else "│   ")), False, True)

        if self.racine is None:
            print("(arbre vide)")
        else:
            _afficher(self.racine)


# ==========================================================================
# Point d'entrée : petite démonstration si le fichier est exécuté seul
# ==========================================================================
if __name__ == "__main__":
    arbre = ArbreBinaireRecherche()
    valeurs = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

    for v in valeurs:
        arbre.inserer(v)

    print("Arbre construit à partir de :", valeurs)
    print()
    arbre.afficher()

    print("\nParcours infixe   :", arbre.parcours_infixe())
    print("Parcours préfixe  :", arbre.parcours_prefixe())
    print("Parcours postfixe :", arbre.parcours_postfixe())
    print("Parcours largeur  :", arbre.parcours_largeur())

    print("\nRecherche de 40 :", arbre.rechercher(40))
    print("Recherche de 99 :", arbre.rechercher(99))

    print("\nHauteur de l'arbre :", arbre.hauteur())
    print("Nombre de noeuds   :", arbre.compter_noeuds())
    print("Minimum            :", arbre.minimum())
    print("Maximum            :", arbre.maximum())
    print("Arbre équilibré ?  :", arbre.est_equilibre())

    print("\nSuppression de 30 (deux enfants)...")
    arbre.supprimer(30)
    arbre.afficher()
    print("Parcours infixe après suppression :", arbre.parcours_infixe())


# ---------------------------------------------------------------------
# Documentation ajoutee par Tahiana - parcours postfixe, largeur, affichage
# ---------------------------------------------------------------------
# parcours_postfixe() : parcourt gauche -> droite -> racine.
#   Utilise notamment pour supprimer un arbre en memoire ou evaluer
#   des expressions arithmetiques representees sous forme d'arbre.
# parcours_largeur() : parcours par niveau (BFS) avec une file (deque).
# afficher() : affichage graphique de l'arbre en mode texte dans la console.
