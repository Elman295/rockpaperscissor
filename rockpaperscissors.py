import random # import

print("welcome to elman game")
print("1 for rock")
print("2 for paper")
print("3 for scissor")

"""
      ---------      |        
      |              |        /\      /\          /  \      |\   |
      ----------     |       /  \    /  \        / __ \     | \  |
      |              |      /    \  /    \      /      \    |  \ | 
      ----------     |     /      \/      \    /        \   |   \|


"""

trails=int(input("trials="))
elmanscore=0
youu=0

for i in range(trails):
    enemy = random.randrange(1, 4)
    you = int(input("you="))
    if enemy==1 and you==1:
       print(" you => rock elman=> rock")
       print("equal")
    elif enemy==1 and you==2:
       print(" you => paper and elman => rock")
       print("you won")
       youu+=1
    elif enemy==1 and you==3:
       print("you => scissor elman => rock")
       print("elman won")
       elmanscore+=1
    elif enemy==2 and you==1:
       print("you => rock elman => paper")
       print("elman won")
       elmanscore+=1
    elif enemy==2 and you==2:
       print("you => paper elman => paper")
       print("equal")
    elif enemy==2 and you==3:
       print("you => scissor elman =>paper ")
       print("you won")
       you+=1
    elif enemy==3 and you==1:
       print("you => rock elman => scissor")
       print("you won")
       youu+=1
    elif enemy==3 and you==2:
       print("you =>paper elman=>scissor")
       print("elman won")
       elmanscore+=1
    elif enemy==3 and you==3:
        print("you => scissor elman => scissor")
        print("equal")

print(f" your score is {youu}")
print(f"elman score is {elmanscore}")