Aplication for synchronization of two folders



Description: 

This app takes 3 arguments - path to source folder, path for replica folder, frequency and path for log file. 

Source folder is the model folder. 

Replica folder is replica of source folder, if replica folder doesnt exist, app will create it. If replica folder have something extra inside, what source foldert doestn, it will be deleted. 

Frequency is time in minutes, for repeating the synchronization. 

In path for log will be log file. It is txt file with name 'syncLog'. If file doesnt exist, it will be created by app. Log will not be overwritten after restarting the application but will be added.


How to install and run the project:

For running this project is needed to have installed python and module 'dirsync'.
Run the project in command line by writting 'syncApp.py' and adding the 3 parametres.


Test example:

In this project should be test folder 'test' with folders and files. This command will sync Folder1 and Folder2 and create a log:
'syncApp.py .\test\Folder1 .\test\Folder2 1 .\test'

