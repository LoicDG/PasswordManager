# Password Manager

   Ce gestionnaire de mot de passes hors-ligne est un programme en python qui vise à être utilisé en tant que batch file (.bat)
   SQLite est la base de donnée utilisée pour enregistrer les utilisateurs ainsi que les mots de passes
   Les mots de passes sont encryptés avant d'être stockés et chaque utilisateur a une clé d'encryption unique
   Pour créer un batch file, copiez collez le texte qui suit dans un fichier texte en remplaçant "path_to_your_directory" 
     par le chemin d'accès au fichier du programme, puis enregistrez le en ajoutant .bat à la fin, ainsi que remplacer, si nécessaire,
     le nom du virtual environment (ici venv)
     
    @ECHO off
    cd /d path_to_your_directory
    call venv\Scripts\activate
    python MainCLI.py "PwManager.db"

  assurez vous d'avoir python 3.7+ d'installé et d'utiliser un virtual environment
  
  voici le lien du site officiel de Python: https://www.python.org/

  Ce projet a été réalisé dans le cadre du GeekFest 2023 organisé par Bell, puis amélioré par la suite
