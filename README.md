# Whatapp-Reloaded
Do you want to preserve a ceratin chat of Whatsapp outside of Whatapp in the same format 
													or
Do you want to see the amount of time you have spent talking to that person.

Whatsapp-Reloaded is a Project to backup and merge Chats along with some additional features like Summary ,Statistics ,Calendar specific to the Chat

## Requirements

	1. Python 3.7.3 or above
	2. Python Modules
			1. simplejson
			2. django
			
## Installation

### 1. Python 3.7.3 or above

1. Download the latest python version [Download](https://www.python.org/downloads/)
2. Install the downloaded file, Make sure to tick the dialogue box when installer provides an option to configure the **PATH** and **PATHEXT** variables 
3. To Check python has been successfully installed or not. Do the following:-
	1. Open Command Line and type the command. 
		``` bash
			python
		```
	2. The version of python would be shown along with opening of python Terminal starting with ">>>" , if the python is successfully installed
4. If Step 3 shows some Error then ,Copy the path of Installed folder (Example:->C:\Program Files\Python 3.8) and paste it in your System Environment Variables.

### 2. Python Modules
1. simplejson
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install simplejson
		```
	3. Download and installation would start automatically
2. django
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install django
		```
	3. Download and installation would start automatically
	
## How to use
### 1. Backing up Chat
#### Step 1
1. Open the chat you want to backup in Whatsapp at your phone.
2. Click on the three vertical dots at the right upper, Then click more and then Click on Export Chat (Without Media).
3. This would create a text file containing all of your messages.

#### Step 2
1. Download my project from Github in a zip file by clicking at the Code(Green button) at https://github.com/ashishjain0338/Whatapp-Reloaded
2. Extract the Downloaded file.
3. Copy the File created in Step 1 Point 3 in the Extracted folder.

#### Step 3
1. Open Command Line and move to the Extracted directory of Step 2 Point 2 by using cd command as
	```
		cd PathOfTheExtractedFolder
	```
2. Then enter the following Command , which would start the Backing up Process
	``` 
		python main.py
	```
3. When the Command Line asks to Make your selection Enter 1 and hit Enter.
4. In the next step, Enter the name (with .txt) of the File of Step 1 Point 3.
	1. If the the above point 4 fails,then you need to Enter the full path of file of Step 1 Point 3.
5. It it says "Summary File Created" or "Calender File Created",then it means that the backing up of process is completed. You can see the backup Three Files in Output Folder named as JsonFile.json,summary.json,calender.json.

### 2. Viewing the Backup File
1. Open Command Line and move to the Extracted directory of Step 2 Point 2 by using cd command as
	```
		cd PathOfTheExtractedFolder
	```
2. Then enter the Command
	``` 
		python manage.py runserver
	```
3. Then open any browser and type
	```
		localhost:8080
	```
	**OR** Instead you can also type the link that would appear at Command line after typing the command at point 2(Example:-> http://127.0.0.1:8000/)
	
	**NOTE** :->The above process would view the Chats only that exist in the Output Folder as JsonFile.json,summary.json,calender.json which was the result of *Backing Up 	Chat*. So make sure that these files do exist in the Output folder with same names.


### 3. Merging Two Chats
Lets say you have taken a backup of your Chat at a particular date using this project and have deleted all the previous messages from the Whatsapp after backup, and after that you continued texting the same person which results in new messsages which are not backed up yet, If you want to backup these new messages,Then this section is for you.

1. First you need to have the JsonFile of both your *Old Chat* and *New Chat* .
	1. If the Chat/data which is shown as *Viewing the *
