"""
Programme principal - Menu interactif de démonstration
Arbre Binaire de Recherche : parcours, recherche et améliorations.

Ce script est destiné à la capture vidéo de démonstration demandée
dans le livrable du projet.
"""

from abr import ArbreBinaireRecherche


def afficher_menu():
    print("\n" + "=" * 55)
    print(" ARBRE BINAIRE DE RECHERCHE (ABR) - MENU PRINCIPAL")
    print("=" * 55)
    print(" 1. Insérer une valeur")
    print(" 2. Rechercher une valeur")
    print(" 3. Supprimer une valeur")
    print(" 4. Parcours infixe   (gauche, racine, droite)")
    print(" 5. Parcours préfixe  (racine, gauche, droite)")
    print(" 6. Parcours postfixe (gauche, droite, racine)")
    print(" 7. Parcours par niveau (largeur)")
    print(" 8. Afficher l'arbre (mode texte)")
    print(" 9. Statistiques (hauteur, nb noeuds, min, max, équilibre)")
    print(" 10. Charger un jeu de valeurs de démonstration")
    print(" 0. Quitter")
    print("=" * 55)


def demander_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def main():
    arbre = ArbreBinaireRecherche()

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            v = demander_entier("Valeur à insérer : ")
            if arbre.inserer(v):
                print(f"-> {v} inséré avec succès.")
            else:
                print(f"-> {v} existe déjà dans l'arbre (non inséré).")

        elif choix == "2":
            v = demander_entier("Valeur à rechercher : ")
            trouve = arbre.rechercher(v)
            print(f"-> {v} {'trouvé' if trouve else 'introuvable'} dans l'arbre.")

        elif choix == "3":
            v = demander_entier("Valeur à supprimer : ")
            if arbre.supprimer(v):
                print(f"-> {v} supprimé avec succès.")
            else:
                print(f"-> {v} n'existe pas dans l'arbre.")

        elif choix == "4":
            print("-> Parcours infixe   :", arbre.parcours_infixe())

        elif choix == "5":
            print("-> Parcours préfixe  :", arbre.parcours_prefixe())

        elif choix == "6":
            print("-> Parcours postfixe :", arbre.parcours_postfixe())

        elif choix == "7":
            print("-> Parcours largeur  :", arbre.parcours_largeur())

        elif choix == "8":
            print()
            arbre.afficher()

        elif choix == "9":
            print(f"-> Hauteur de l'arbre : {arbre.hauteur()}")
            print(f"-> Nombre de noeuds   : {arbre.compter_noeuds()}")
            print(f"-> Minimum            : {arbre.minimum()}")
            print(f"-> Maximum            : {arbre.maximum()}")
            print(f"-> Arbre équilibré ?  : {arbre.est_equilibre()}")

        elif choix == "10":
            demo = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
            for v in demo:
                arbre.inserer(v)
            print(f"-> Jeu de démonstration chargé : {demo}")

        elif choix == "0":
            print("Fin du programme. Au revoir !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
