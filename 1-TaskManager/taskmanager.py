
tasks = []  # Liste des tâches

def add_task():
    task = input("Entrez une nouvelle tâche : ")
    tasks.append(task)
    print("Tâche ajoutée avec succès !")

def modify_task():
    index = int(input("Entrez l'indice de la tâche à modifier : "))
    if index >= 0 and index < len(tasks):
        new_task = input("Entrez la nouvelle tâche : ")
        tasks[index] = new_task
        print("Tâche modifiée avec succès !")
    else:
        print("Indice de tâche invalide !")

def delete_task():
    index = int(input("Entrez l'indice de la tâche à supprimer : "))
    if index >= 0 and index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Tâche '{deleted_task}' supprimée avec succès !")
    else:
        print("Indice de tâche invalide !")

def show_tasks():
    print("Liste des tâches :")
    for index, task in enumerate(tasks):
        print(f"{index}. {task}")

def main():
    while True:
        print("\nBienvenu dans votre Gestionnaire de tâche:")
        print("1. Ajouter une tâche")
        print("2. Modifier une tâche")
        print("3. Supprimer une tâche")
        print("4. Afficher les tâches")
        print("5. Quitter")

        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            add_task()
        elif choice == "2":
            modify_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            break
        else:
            print("Choix invalide !")

if __name__ == "__main__":
    main()


