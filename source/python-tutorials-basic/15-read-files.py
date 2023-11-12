'''
open( "filename.txt", "__" )
r  = read
w  = write
a  = append (add more at the end of the file)
r+ = read and write
'''

my_file = open("lesson15.txt", "r")

#GET INFO FROM FILE ==============
print(my_file.readable())       #Checks if file an be read from
#print(my_file.read())           #Outputs file
#print(my_file.readline())       #reads first line
#print(my_file.readline())       #reads next line

#print(my_file.readlines())      #reads lines of file and stores in array
for line in my_file.readlines():
    print(line)                  #readline via for loop

my_file.close()