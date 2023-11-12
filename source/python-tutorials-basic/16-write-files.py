'''
open( "filename.txt", "__" )
r  = read
w  = write
a  = append (add more at the end of the file)
r+ = read and write
'''

#Appending file
my_file = open("lesson15.txt", "a")
my_file.write("\nCreed - I don't know")
my_file.close()

#Write file (override)
my_file = open("lesson16.txt", "a")
my_file.write("\nJim - Salesman \nDwight - Salesman \nPam - Receptionist")
my_file.close()