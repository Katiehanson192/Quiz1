
'''
Create a Weapon Class definition according to the following specs:

Attributes:

name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

'''

import random

class WeaponClass:
    def __init__(self, weaponName, bullNum, Fast, distance, stat):
        self.__name = weaponName
        self.__bullets = bullNum
        self.__speed = Fast
        self.__range = distance
        self.__status = 'Active'

    def get_Weapon_name(self):
        return self.__name

    def set_bull_number(self, bullNum):
        self.__bullets = random.randint(10,100000)

    def get_Number_bullet(self):
        return self.__bullets

    def get_fast(self):
        return self.__speed
    
    def get_distance(self):
        return self.__range

    def get_Weapon_stat(self):
        return self.__status
    
    def fire_bullet(self, bullNum):
        if self.__bullets > 0:
            self.__bullets -1
        else:
            self.__status = 'Inactive'





