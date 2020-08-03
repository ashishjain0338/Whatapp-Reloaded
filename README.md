# Whatapp-Reloaded
Do you want to preserve a ceratin chat of Whatsapp outside of Whatapp in the same format 
													or
Do you want to see the amount of time you have spent talking to that person.

Whatsapp-Reloaded is a Project to backup and merge Chats along with some additional features like Summary ,Statistics ,Calendar specific to the Chat

The end Result/View would look like the following

1. Here you can view each chat Day wise.
	![day-view](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/View/Day.PNG)


2. In Calender, you can see the amount of time talked each day.
	![calender-view](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/View/Calender.PNG)


3. In Summary, you can see some statistics like Total Messages,Longest Text etc.
	![summary-view](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/View/Summary.jpg)

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
	2. The version of python would be shown along with opening of python Terminal starting with ">>>" , if the python is successfully installed.
	![python install](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/python%20install.PNG)
4. If Step 3 shows some Error then ,Copy the path of Installed folder (Example:->C:\Program Files\Python 3.8) and paste it in your System Environment Variables.

### 2. Python Modules
1. simplejson
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install simplejson
		```
	3. Download and installation would start automatically
	![Simple Json](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/Simplejson.PNG)
2. django
	1. First make sure that Python is installed and your system is connected to internet.
	2. Open Command line and enter the command
		```
			pip3 install django
		```
	3. Download and installation would start automatically
	![Django](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/django.PNG)
	
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
3. When the Command Line asks to "Make your selection" Enter 1 and hit Enter.
4. In the next step, Enter the name (with .txt) of the File of Step 1 Point 3.
	1. If the the above point 4 fails,then you need to Enter the full path of file of Step 1 Point 3.
	![Backing up file](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/Backing%20up%20file.jpg)
5. It it says "Summary File Created" or "Calender File Created",then it means that the backing up of process is completed. You can see the backup Three Files in Output Folder named as JsonFile.json , summary.json , calender.json.

### 2. Viewing the Backup File
1. Open Command Line and move to the Extracted directory of Step 2 Point 2 by using cd command as
	```
		cd PathOfTheExtractedFolder
	```
2. Then enter the Command
	``` 
		python manage.py runserver
	```
	![Running Server](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/starting%20server.PNG)
3. Then open any browser and type
	```
		localhost:8080
	```
	**OR** Instead you can also type the link that would appear at Command line after typing the command at point 2(Example:-> http://127.0.0.1:8000/)
	
	**NOTE** :->The above process would view the Chats only that exist in the Output Folder as JsonFile.json,summary.json,calender.json which was the result of *Backing Up 	Chat*. So make sure that these files do exist in the Output folder with same names.


### 3. Merging Two Chats
Lets say you have taken a backup of your Chat at a particular date using this project and have deleted all the previous messages from the Whatsapp after backup, and after that you continued texting the same person which results in new messsages which are not backed up yet, If you want to backup these new messages,Then this section is for you.

1. First you need to have the JsonFile of both your *Old Chat* and *New Chat* .
	1. If the Chat/data which is shown as *Viewing the Chat* is same as that of *Old Chat*,Then you just need to rename the JsonFile.json in the Output Folder .
		
		If step 1 is not valid,Then you need to create the Backup file by following *Backing Up Chat* Section and then to rename the JsonFile.json in the Output Folder.
	2. For JsonFile of *New Chat* ,you need to create the Backup file by following *Backing Up Chat* Section on your *New Chat Text File* and then to rename the 				JsonFile.json in the Output Folder.
	
	Once you have both JsonFile of Old as well as New Chat ,You can move on to merging them.
2. Open Command Line and move to the Extracted directory by using cd command as
	```
		cd PathOfTheExtractedFolder
	```
3. Then enter the following Command , which would start the Merging up Process
	``` 
		python main.py
	```
4. When the Command Line asks to "Make your selection" Enter 2 and hit Enter.
5. Then enter the Name of the Old Chat Json file (which was renamed in step 1)(Example:->OldChat.json)

	If it fails,then you need to enter the Full Path of the Old Chat Json File.
6. Then enter the Name of the New Chat Json file (which was renamed in step 1)(Example:->NewChat.json)

	If it fails,then you need to enter the Full Path of the New Chat Json File.
	![Merge Chat](https://github.com/ashishjain0338/Whatapp-Reloaded/blob/master/ScreenShots/Misc/Merge%20Chat.jpg)
7. Thats it, Both Chats would  be merged as  Three Files in Output Folder named as JsonFile.json , summary.json , calender.json.You can then View the merged chat using the steps of *Viewing the Chat*.



*This is my first project at Github,I don't know a lot about Contributing but If you Find any error/problem,Let me know ,Thanks for Reading :)*
