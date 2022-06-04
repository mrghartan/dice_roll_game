
import random
def dice_roll(game_steps, game_players,win_no="max"):
    '''game_steps= how many times to roll a dice
    game_players= Number of players playing the game
    win_no(by default=Max)= set a winning no if not set nothing max wins'''
    df={}
    df['players']=[]
    df['dice_roll_history']=[]
    df['position_history']=[]
    df['max_count']=[]
    df["winner"]=[]
    for j in range(1,game_players+1):
        dice_lsit=[]
        dice_sum=[]
        for i in range(game_steps):
            dice_lsit.append(random.randint(1,6))
            x=sum(dice_lsit)
            dice_sum.append(x)
            
        


            
        df['dice_roll_history'].append(dice_lsit)
            
        df['players'].append(["player_"+str(j)])
        
        df['position_history'].append(dice_sum)
        df['max_count'].append([x])
        df['winner'].append(0)
    if win_no=="max":
        df['winner'][df['max_count'].index((max(df['max_count'])))]=1
    elif df["max_count"].count(win_no)==1 :
        df["winner"][df['max_count'].index([win_no])]=1
    return df
# print(dice_roll(game_steps,game_players))
def main():
    print("Number of rounds")
    game_steps=int(input())
    print("number of players")
    game_players=int(input())
    print("want to assign winning number type y else n")
    want_to_assign_win_no=input()
    if want_to_assign_win_no.lower()=='y':
        print('winning Number')
        win_no=int(input())
    else:
        win_no="max"
    dc=dice_roll(game_steps, game_players,win_no)
    print(dc)
    print(dc['players'][dc['winner'].index(1)])
if __name__=='__main__':
    main()
    

