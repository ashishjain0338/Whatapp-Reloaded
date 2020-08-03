from bin import methods
import os
try:
    os.mkdir('Output')
except:
    pass
print("To convert a new txt file(Exported form Whatsapp) to Json file(In order to see in Webapp),Enter 1\n"
      "To combine two previously created json file(Combining old file with latest one just in case latest file doesnt contain the old file data) of chat to the same person,Enter 2")
choice = int(input("Make your selection \t"))
if(choice == 1):

    # raw_file_path = "Dummy Chat.txt"
    raw_file_path = input("Enter path/name of Exported File:->")
    json_path = "Output/JsonFile.json"
    try:
        fp = open(raw_file_path , "r", encoding='utf8', errors='ignore')
    except:
        print("Unable to open file\n Please Enter correct path")
        exit()

    dateformat  =  methods.CreateJson(raw_file_path , json_path)
    if(dateformat):
        # print("Date need to be formatted")
        methods.DateFormat(json_path)
    print("JSON FILE HAS BEEN CREATED IN OUTPUT FOLDER\n NOW CREATING REST FILES")
    print("Members Constituing the Chat are",methods.GetNames(json_path))
    methods.Summary(json_path,"Output/summary.json")
    print("Summary file created")
    methods.Calender(json_path,"Output/calender.json")
    print("Calender file created")
elif(choice == 2):

    # old_file_path = "part1.json"
    # latest_path = "part2.json"
    old_file_path = input('Enter the path/name of the old file:->')
    try:
        file = open(old_file_path , 'r')
    except:
        print('Invalid File path')
        exit(101)
    latest_file_path = input('Enter the path/name of the latest file:->')
    try:
        file = open(latest_file_path, 'r')
    except:
        print('Invalid File path')
        exit(101)
    json_path = 'Output/JsonFile.json'
    methods.Combine(old_file_path,latest_file_path,'Output/JsonFile.json')
    print("JSON FILE HAS BEEN CREATED IN OUTPUT FOLDER\n NOW CREATING REST FILES")
    print("Members Constituing the Chat are", methods.GetNames(json_path))
    methods.Summary(json_path, "Output/summary.json")
    print("Summary file created")
    methods.Calender(json_path, "Output/calender.json")
    print("Calender file created")

