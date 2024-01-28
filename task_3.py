#short Game
#Welcome to Treasure Island.
#User Enter his/her Path
path=input("Enter your Path left or Right:")
if path == "left":
    #if path is left then move further otherwise fall
    choose=input(" Choose swim or wait :")
    #user choose swim or wait 
    if choose=="wait":
        #if choose wait move further otherwise Attacked
        door=input("Choose Door color : ")
        #User choose door color 
        if door=="yellow":
            #if door color is yellow then you win otherwise Burned, Eaten or Game over 
            print("You Win!")
        elif door=="red":
            print("Burned by fire.Game Over")
        elif door=="rlue":
            print("Eaten by beasts.Game Over")
        else:
            print("Game Over!")
            
    else:
        print("Attacked by trout.Game Over!")
        
else :
    print("Fall into a hole.Game Over")


























# print('''Welcome to Treasure Island
# Your mission is to find the treasure''')
# path=input("enter your path L or R")
# if path =="left":
#     select=input("choose swim or wait")
#     if select=="wait":
#         door_color=input("choose door color")
#         if door_color=="yellow":print("you win")   
#         elif door_color=="red":print("burned by fire Game over")    
#         elif door_color=="blue":print("entered by beasts Game over")
#         else:print("game over")
#     else:print("attacked by trout game over")
# else:print("fail into the whole and game over")




