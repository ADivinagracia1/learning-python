team = ["Andrei", "Jarod", "Matthew", "Junaid", "Mahmoud"]
nums = [4, 5, 16, 23, 15, 42]

print( "--------------List Basics----------------")
print(team[1])
print(team[-5]) #python can access from the back of lists
print(team[-1])
print(team[2:4])
print(team[2:]) # 2nd element and beyond
print(team[:2]) # BEFORE 2nd element

print( "-------------List Functions--------------")
team.append(nums);          print(team)
team.remove(nums);          print(team)
team.append("Jason1");      print(team)
team.insert(1, "Jason2");   print(team)
team.pop();                 print(team) # removes the end of the list
team.sort();                print(team)
team.reverse();             print(team)

team2 = team.copy()
team2 = team        #Wont work, all funtions will be done tto the original list

print(team.index("Junaid"))
print(team.count("Jarod"))