#S.McDonald 11/8/2016
#file_display
#show the contents of the file


#input
#myfile is a file object
myfile = open('numbers.txt', 'r') #open the file for reading


#processing
#read one line from the file
#line1 = myfile.readline()

#use for loops to do file processing one line at a time
for line in myfile:
    print(line)




myfile.close() #call close() method of myfile object


#output
#display the numbers
#print(line1)

