# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:20:31 2016

@author: Artur
"""
def switch(x):
    return {
            1:"Paper",
            2:"Rock",
            3:"Scissors"
            }.get(x,'there is no such option')
            

def Firstround(howManyPlayer):
    Scissors =[]
    paper = []
    rock = []
    for x in range(howManyPlayer):
        player_choose = int(input('''Choose one from the following option
        1 - Paper
        2 - Rock
        3 - Scissors
        '''))
        if switch(player_choose) == "Paper" : paper += [switch(player_choose)]
        elif switch(player_choose) == "Scissors" : Scissors += [switch(player_choose)]
        elif switch(player_choose) == "Rock" : rock += [switch(player_choose)]
    print(len(paper),len(rock),len(Scissors))
    Scissor_player = len(Scissors)
    rock_player = len(rock)
    paper_players = len(paper)
    return  compare(paper_players,rock_player,Scissor_player)
    

     
def compare(paper_players,rock_player,Scissor_player):
    
    if Scissor_player >=paper_players and paper_players == 0 : 
        Scissor_player = 0
    elif  rock_player >= Scissor_player and Scissor_player == 0: 
        rock_player = 0
    elif  paper_players >= rock_player and rock_player == 0: 
        paper_players = 0
    else : 
        print("there is Pass so try again")
    return paper_players,rock_player,Scissor_player


    
def main():
    print ('Welcome in my program about game Rock Paper Scissors')  
    HowManyPlayers = int(input('pelase enter how many players will play'))
    first_round = Firstround(HowManyPlayers)
    while  True:
        print('all players pelase which stay choose again ')
        if sum(first_round) == 1 :
            if first_round[0] == 1:
                print('the game is over , paper lose  ')
                break
            elif first_round[1] == 1:
                print('the game is over, rock lose  ')
                break
            elif first_round[2] == 1: 
                print('the game is over, scissor lose  ')
                break
            
        else :
            first_round = Firstround(sum(first_round))

    
if __name__ == "__main__":main()
        
    