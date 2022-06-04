game_steps=5
game_players=5
win_no="max"
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
print(dice_roll(game_steps,game_players))
