import math
class cannon:
    def __init__(self,choice,speed,angle,height):
        self.speed = int(speed)
        self.angle = int(angle)
        self.height = int(height)
        self.choice = choice

    
    def shooter(self):
        gravity = 9.81
        if self.choice == 1:
            time = math.sqrt(2*self.height/gravity)
            distance = self.speed * time
            print(f"Distance cannon ball will travel is {distance}")
        elif self.choice == 2:
            speed_horizontal = self.speed * math.cos(math.radians(self.angle))           
            speed_vertical = self.speed * math.sin(math.radians(self.angle))
            peak = speed_vertical / gravity
            distance = speed_horizontal * peak * 2      
            print(f"Distance cannon ball will travel is {distance}")    
        elif self.choice == 3:
            speed_horizontal = self.speed * math.cos(math.radians(self.angle))           
            speed_vertical = self.speed * math.sin(math.radians(self.angle))
            peak = speed_vertical / gravity
            peak_height = math.pow(speed_vertical,2) / (2*gravity)
            total_height = peak_height - self.height
            time = 2*peak
            distance = round(speed_horizontal * time , 2)
            print(f"Distance cannon ball will travel is {distance}")
        else:
            print("Wrong Choice Try Again!!!!!!")

speed = 0
angle = 0
height = 0
choice = 0
repeat = 'y'
while repeat == 'y':
    try:
        print("Choose scenario : ")
        print("1. Scenario 1 : Horizontal cannon")
        print("2. Scenario 2 : Angled cannon towards ship at same level")
        print("3. Scenario 3 : Angled cannon towards ship at lower level, but far away")
        choice1 = int(input("Enter choice : "))

        if choice1 == 1:
            speed = input("Enter Speed of canon ball : ")
            height = input("Enter Height of the cannon above the water : ")
            cannon1 = cannon(choice1,speed,angle,height)
            cannon1.shooter()
        elif choice1 == 2:
            speed = input("Enter Speed of cannon ball : ")
            angle = input("Enter Angle of the cannon when the cannonball leaves the cannon : ")
            cannon1 = cannon(choice1,speed,angle,height)
            cannon1.shooter()
        elif choice1 == 3:
            speed = input("Enter Speed of cannon ball : ")
            height = input("Enter Height of the cannon above the water : ")
            angle = input("Enter Angle of the cannon when the cannonball leaves the cannon : ")
            cannon1 = cannon(choice1,speed,angle,height)
            cannon1.shooter()
        else:
            print("Invalid choice")
        repeat = input("Do you want to continue (y/n) : ")
    except ValueError:
        print("Wrong input try again")