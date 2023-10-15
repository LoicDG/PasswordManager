# Password Manager

   Ce gestionnaire de mot de passes hors-ligne est un programme en python qui vise à être utilisé en tant que batch file (.bat)
   SQLite est la base de donnée utilisée pour enregistrer les utilisateurs ainsi que les mots de passes
   Les mots de passes sont encryptés avant d'être stockés et chaque utilisateur a une clé d'encryption unique
   Pour créer un batch file, copiez collez le texte qui suit dans un fichier texte en remplaçant "path_to_your_directory" 
     par le chemin d'accès au fichier du programme, puis enregistrez le en ajoutant .bat à la fin
     
    @ECHO off
    cd /d path_to_your_directory
    call venv\Scripts\activate
    python MainCLI.py "PwManager.db"

  assurez vous d'avoir python 3.7+ d'installé
  
  voici le lien du site officiel de Python: https://www.python.org/
