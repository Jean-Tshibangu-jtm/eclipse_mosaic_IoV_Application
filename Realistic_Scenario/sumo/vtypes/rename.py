import os

# Récupérer la liste des fichiers dans le dossier actuel
liste_fichiers = os.listdir()

# Parcourir chaque fichier dans la liste
for fichier in liste_fichiers:
    # Vérifier si le fichier se termine par ".vtype.xml"
    if fichier.endswith(".vtype.xml"):
        # Construire le nouveau nom de fichier en remplaçant l'extension
        nouveau_nom = fichier.replace(".vtype.xml", ".rou.xml")
        
        # Renommer le fichier
        os.rename(fichier, nouveau_nom)
        
        # Afficher un message pour indiquer le renommage
        print(f'Le fichier "{fichier}" a été renommé en "{nouveau_nom}".')

print("Renommage terminé.")
