user1=input("name1")
user2=input("name2")
user1_answer=input("%s"%user1)
user2_answer=input("%s"%user2)
def compare(u1,u2):
    if u1 == u2:
        return("tie")
    elif u1 == 'rock':
        if u2 =='scissor':
            return("rock wins")
        else:
            return("paper wins")
    elif u1 == 'scissor':
        if u2 == 'paper':
            return ("scissor wins")
        else:
            return ("rock wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            return ("paper wins")
        else:
            return ("scissor wins")
    else:
        return("invalid input")
        sys.exit()
        print(compare(user1_answer,user2_answer))