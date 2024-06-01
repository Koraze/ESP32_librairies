import os
import fileinput

def replace_tabs_with_spaces(directory, spaces=4, backup=False, extension=(".py", ".json", ".md")):
    print("parametres pris en compte")
    print("- remplacement des tabs par %d espaces" % (spaces))
    print("- création de backup :", backup)
    print("- extensions prises en compte :", extension)
    print("- fichiers cachés pris en compte :", "oui")
    print("\nfichiers parcourus")
    
    backup='.bak' if backup else None
    modified_files = []
    error_files = []
    
    # Parcourir tous les fichiers et sous-dossiers
    for root, dirs, files in os.walk(directory):
        # Ignorer les sous-dossiers commençant par un point
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        # Parcourir les fichiers dans le dossier root
        for file in files:
            if not file.startswith('.') and file.endswith(extension) :
                file_path = os.path.join(root, file)
                # Modifier les fichiers en place
                print(file_path)
                modified = False
                try :
                    with fileinput.FileInput(file_path, inplace=True, backup=backup) as file:
                        for line in file:
                            new_line = line.replace('\t', ' ' * spaces)
                            if new_line != line:
                                modified = True
                            print(new_line, end='')
                        # Si le fichier a été modifié, l'ajouter à la liste
                        if modified:
                            modified_files.append(file_path)
                except :
                    error_files.append(file_path)

    # Afficher les fichiers modifiés
    print()
    if modified_files:
        print("Fichiers modifiés:")
        for file in modified_files:
            print(file)
    else:
        print("Aucun fichier n'a été modifié.")

    # Afficher les fichiers erronés
    print()
    print("Fichiers générant des erreurs:")
    for file in error_files:
        print(file)

if __name__ == "__main__":
    directory = input("Entrez le chemin du dossier à parcourir: ")
    replace_tabs_with_spaces(directory)

