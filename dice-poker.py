import random
import os

NUM_OF_FACES = 6
NUM_OF_DICES = 5

NOTHING = 0
PAIR = 2
SET = 3
CARE = 4
POKER = 5
STRAIGHT = 100
FULL_HOUSE = 23


sym_dices = { 1: '⚀',
              2: '⚁',  
              3: '⚂',
              4: '⚃',
              5: '⚄',
              6: '⚅',
            }


class Dice:
    """
    Class Dice
    """
    def __init__(self,num_faces):
        self.__num_faces = num_faces
        self.roll()
        
    def __str__(self):
        return str(self.act_face)
        
    def roll(self):
        self.__act_face = random.randint(1,self.__num_faces)
    
    def draw(self):
        print(sym_dices.get(self.act_face),end = ' ')
        
    @property
    def act_face(self):
        return self.__act_face


class Player:
    """
    Class Player
    """
    
    def __init__(self,name):
        self.name = name
        self.__hand = []
        # ~ self.__hand = {1:0,2:0,3:0,4:0,5:0,6:0}
        self.__state = NOTHING
        
    def __str__(self):
        return self.name + self.__hand
    
    def get_dices(self,dices):
        if dices:
            self.__hand = dices
            # ~ print(self.name,'has now', len(self.__hand), 'dices in the hand')
        else:
            # ~ print('Nothing to getting')
            pass
    
    def get_state(self):
        return self.__state
            
    def set_state(self,state):
        self.__state = state
        

                
    # ~ def roll_dices(self):
        # ~ self.__state = NOTHING
        # ~ for dice in self.__hand:
            # ~ dice.roll()
    
    def roll_dices(self,dices_to_roll=None):
        if dices_to_roll==None:
            self.__state = NOTHING
            for dice in self.__hand:
                dice.roll()
        else:
            for dice in self.__hand:
                if self.__hand.index(dice) in dices_to_roll:
                    dice.roll()
        # ~ print(self.name,'rolled the dices')
        
    def show_hand(self):
        dice_to_show = []
        for dice in self.__hand:
            dice_to_show.append(str(dice))
        return dice_to_show
            
    def draw_hand(self):
        for dice in self.__hand:
            dice.draw()
        print('')
        
def check_hand(hand):
    state = {}
    result = NOTHING
    
    for i in range(1,7):
        state.update({i:hand.count(str(i))})
        
    # ~ print(state)
    
    
    if list(state.values()).count(1) == 5:
        tmp = []
        for key in state:
            if state.get(key) != NOTHING:
                tmp.append(key)
        if set(tmp) == {1,2,3,4,5} or set(tmp) == {2,3,4,5,6}:
            result += STRAIGHT
    elif POKER in state.values():
        result += POKER*1000
    
    elif CARE in state.values():
        result += CARE*100
    
    elif PAIR in state.values() and SET in state.values():
        result += FULL_HOUSE*100
        
    else:
        if PAIR in state.values():
            for key in state:
                if state.get(key)==PAIR:
                    result+=key+PAIR
                    
        if SET in state.values():
            for key in state:
                if state.get(key)==SET:
                    result+=key+SET*10
                
    
    return result

        
def get_random_dices(num_of_dices,num_of_faces):
    dices = []
    for i in range(0,num_of_dices):
        dice = Dice(num_of_faces)
        dices.append(dice)
    return dices


def main():
    num_of_players = int(input("Сколько игроков за столом? - " ))
    players = []
    first_player = 0
    for i in range(num_of_players):
        player_name = input("Как зовут игрока №" + str(i + 1) + "? - ")
        player = Player(player_name)
        print(player.name, "садится за стол.")
        players.append(player)
        
    input("Чтобы начать игру нажмите 'Enter'. ")
        
    for player in players:
        player.get_dices(get_random_dices(NUM_OF_DICES,NUM_OF_FACES))
        print(player.name, "берет кости в руку.")   
    
    try:
        first_player = int(input("Кто кидает кости первым? Введите число от \
1 до " + str(num_of_players) + ". Для случайного выбора нажмите 'Enter' без ввода числа. "))
    except ValueError:
        first_player = random.randint(1,num_of_players)
        
    print(players[first_player-1].name, "первым кидает кости.")

    
    if first_player != 1:
        for i in range(num_of_players):
            player = players[i] 
            if i < first_player-1:
                players.append(players[i])
                players.pop(i)
    
    for player in players:
        input(player.name +"! Чтобы кинуть кости нажми 'Enter'. ")
        print(player.name, " кидает кости.")
        player.roll_dices()
        print("Результат броска: ", end='')
        player.draw_hand()
        
    # round 1
    dices_to_reroll = []
    for player in players:
        dices_to_reroll = input(player.name + " какие кости будешь перебрасывaть. Напиши порядкове номера через запятую: - ")
        player.roll_dices(dices_to_roll=dices_to_reroll.split(','))
        print("Результат броска: ", end='')
        player.draw_hand()
    
    # ~ print(player1.name,'has:', player1.show_hand())
    # ~ print(player2.name,'has:', player2.show_hand())

    # ~ input("Press 'Enter' to roll dice")
    
    # ~ while stage != END:
        # ~ kb = input("Next step?")
        # ~ if kb == 'q':
            # ~ break
        # ~ else:
            # ~ os.system('clear')
            # ~ player1.roll_dices()
            # ~ player1.set_state(check_hand(player1.show_hand()))
            # ~ print(player1.name,'has:', player1.show_hand(), "State:",player1.get_state())
            # ~ player2.roll_dices()
            # ~ player2.set_state(check_hand(player2.show_hand()))
            # ~ print(player2.name,'has:', player2.show_hand(),"State:",player2.get_state())
        
        
    
    #dices_to_roll = input(len(hand),"dice(s) in the hand. Pick dices to reroll. (type dice's number by comma)").split(',')
    
    
if __name__=='__main__':
    main()   
