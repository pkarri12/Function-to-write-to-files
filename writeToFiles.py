#Defining a funtion to write to files
#Gave two parameters to the function
#one for data that has to be put into the file
#one for the name of the file

def writeToFiles(textInput, fileName):
	f = open(fileName, mode = "w")
	f.write(textInput)
	return
#Calling the function to write a file named hello
#and put the text "Hello World!" in the text file

writeToFiles("Hello World!", "C:\\Users\\devipriya.patel\\Desktop\Python\\hello.txt")

