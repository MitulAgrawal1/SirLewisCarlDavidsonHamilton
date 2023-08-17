############################################################################################
## QUESTION - 1 (Write a program to get roll numbers, names and marks of the students of a class and store these details in a file called marks.dat. Process these marks to calculate percentage scored by students and save in the file mentioned. Display the data of the file in an appropriate format to view the complete details of the students.)
############################################################################################


############################################################################################
## QUESTION - 2 (Write a program to copy contents of one file to another file and display the content of the destination file .)
############################################################################################

##source_file = open("source.txt", "r")
##destination_file = open("destination.txt", "w")
##toput = source_file.read()
##destination_file.write(toput)
##source_file.close()
##destination_file.close()
##destination_file = open("destination.txt", "r")
##print(destination_file.read())
##destination_file.close()


############################################################################################
## QUESTION - 3 (Write a program to display the size of a file after removing EOL , leading and trailing white spaces in the file.)
############################################################################################

##source_file = open("source.txt", "r")
##toanalyse = source_file.read()
##toanalyse = toanalyse.replace("\n","")
##toanalyse = toanalyse.strip()
##print(len(toanalyse))

############################################################################################
## QUESTION - 4 (Write a program to display the number of lines in a file after checking the existence of the file in your system .)
############################################################################################

##import os
##txtfile= "destination.txt"
##if os.path.isfile(txtfile):
##    print("File exists")
##else:
##    print("File does not exist")
##lines = 0
##source_file = open("destination.txt", "r")
##for line in source_file: 
##    lines = lines + 1
##print("Number of lines in the file is",lines)

############################################################################################
## QUESTION - 5 (Write a function that accepts two file names and copies all lines that do not start with a lower case letter from the first file into the second.Read the target file .)
############################################################################################

##source_file = open("source.txt", "r")
##destination_file = open("destination.txt", "w")
##for line in source_file: 
##    if line[0].islower() == False:
##        destination_file.write(line)
##    else:
##        continue
##source_file.close()
##destination_file.close()
##destination_file = open("destination.txt", "r")
##print(destination_file.read())
##destination_file.close()

############################################################################################
## QUESTION - 6 (Write a function that accepts a file name and reports the file’s longest line.)
############################################################################################

##source_file = open("source.txt", "r")
##longline = ""
##linelen = 0
##for line in source_file:
##    if len(line) > linelen:
##        linelen = len(line)
##        longline = line
##print(longline)
##print(linelen)

############################################################################################
## QUESTION - 7 (A text file contains alpha-numeric text. Write a program the reads this text file and prints only numbers from this file.)
############################################################################################

##source_file = open("source.txt", "r")
##toprint = ""
##for line in source_file:
##    for i in line:
##        if i.isnumeric() == True:
##            toprint = toprint + i
##        
##print(toprint)

############################################################################################
## QUESTION - 8 (Write a program that copies a text file onto another file barring the lines starting with “@” symbol)
############################################################################################

##source_file = open("source.txt", "r")
##destination_file = open("destination.txt", "w")
##towrite = ""
##for line in source_file:
##    towrite = "@" + line
##    destination_file.write(towrite)

############################################################################################
## QUESTION - 9 (Write a program to count the word “to” and “the” present in the file article.txt)
############################################################################################

##source_file = open("article.txt", "r")
##countto = 0
##countthe = 0
##for line in source_file:
##    a = line.count("to")
##    b = line.count("the")
##    countto = countto + a
##    countthe = countthe + b
##
##print("Number of times 'to' occures in the file article.text is", countto)
##print("Number of times 'the' occures in the file article.text is", countthe)

############################################################################################
## QUESTION - 10 (Write a program to convert case of all the vowels present in a text file)
############################################################################################

##source_file = open("article.txt", "r")
##destination_file = open("destination.txt", "w")
##for line in source_file: 
##    line1 = ""
##    for i in line:
##        if i in "aeiouAEIOU":
##            if i.islower() == True:
##                i = i.upper()
##                print(i)
##            else:
##                i = i.lower()
##        line1 = line1 + i
##    destination_file.write(line1)
##destination_file.close()

        


