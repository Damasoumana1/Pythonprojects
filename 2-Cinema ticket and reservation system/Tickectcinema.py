
import datetime

# Liste des films disponibles
films = [
    {"titre": "Avengers: Endgame", "heure": datetime.datetime(2023, 7, 19, 18, 0)},
    {"titre": "Spider-Man: No Way Home", "heure": datetime.datetime(2023, 7, 19, 20, 30)},
    {"titre": "Black history", "heure": datetime.datetime(2023, 7, 19, 22, 0)},
    {"titre":"Mission Impossible","heure": datetime.datetime(2023,7,19,22,30)},
    {"titre":"Sarafina Apartheid in south Africa","heure": datetime.datetime(2023,7,19,22,35)},
    {"titre":"Woman king ","heure": datetime.datetime(2023,7,19,23,00)}
    
]

# Fonction pour afficher les films disponibles
def afficher_films():
    print("Films disponibles :")
    for i, film in enumerate(films):
        heure = film["heure"].strftime("%H:%M")
        print(f"{i+1}. {film['titre']} - Heure : {heure}")

# Fonction pour réserver des billets
def reserver_billets(film_index, nombre_billets):
    if film_index < 0 or film_index >= len(films):
        print("Index de film invalide.")
        return

    film = films[film_index]
    heure = film["heure"].strftime("%H:%M")

    print(f"Vous avez réservé {nombre_billets} billet(s) pour le film '{film['titre']}' à {heure}.")

# Fonction principale
def main():
    print("Bienvenue chez DAMA système de réservation de billets de cinéma !")

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Afficher les films disponibles")
        print("2. Réserver des billets")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            afficher_films()
        elif choix == "2":
            afficher_films()
            film_index = int(input("Sélectionnez le numéro du film : ")) - 1
            nombre_billets = int(input("Combien de billets voulez-vous réserver ? "))
            reserver_billets(film_index, nombre_billets)
        elif choix == "0":
            print("Merci d'avoir utilisé notre système de réservation de billets de cinéma. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution du programme
if __name__ == "__main__":
    main()


