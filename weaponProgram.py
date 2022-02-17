from turtle import distance

from numpy import number
import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
Wn = open('weapons.csv', 'r')




# create a csv object from the file object
weapons_file = csv.reader(Wn, delimiter = ',')


#skip the header row
next(weapons_file)



#create an empty dictionary named 'weapons_dict'
weapons_dict = {}



#use a for loop to iterate through every row of the csv file
for line in weapons_file:
    #use variables for name,speed and range (optional)
    name = line[0]
    speed = line[1]
    dist = line[2]

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    

    # append the name and bullet count to 'weapons_dict'
    data = w.WeaponClass(name, speed,distance)
    data.set_bull_number()
    weapons_dict[name] = speed, dist, data.get_Number_bullet()
    
    # print out the name of the weapon using the appropriate method of the object 
    print('Weapon name: ',name)
    # print out the speed of the weapon using the appropriate method of the object
    print('Weapon speed: ',speed)
    # print out the range of the weapon using the appropriate method of the object
    print('Weapon range: ',dist)
    # print out the number of bullets of the weapon using the appropriate method of the object
    print('Number of bullets: ', data.get_Number_bullet())

    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    for number in range(data.get_Number_bullet()):
        # call the appropriate method to fire a bullet
        data.fire_bullet()
        # print out the bullet count every time the weapon is fired
        print(data.get_Number_bullet(), end='\r')
    


#using a loop print out the name and number of bullets from the dictionary
for key in weapons_dict:
    #print(weapons_dict)
    print(key)
    print(data.get_Number_bullet())

#print(weapons_dict)



    


    



