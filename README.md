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
3. Copy the File created in Step 1 in the Extracted folder.

#### Step 3
1. Open Command Line and move to the directory of Step 2 by using cd command as
	```
		cd PathOfTheExtractedFolder
	```
2.Then enter the Command
	``` 
		python main.py
	```


