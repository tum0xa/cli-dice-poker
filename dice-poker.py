import random

NUM_OF_FACES = 6
NUM_OF_DICES = 5

State = {0:'Nothing',
        1: 'Pair (1)',
        2: 'Pair (2)',
        3: 'Pair (3)',
        4: 'Pair (4)',
        5: 'Pair (5)',
        6: 'Pair (6)',
        }

NOTHING = 0

PAIR1 = 1
PAIR2 = 2
PAIR3 = 3
PAIR4 = 4
PAIR5 = 5
PAIR6 = 6

TWO_PAIR = 7

SET1 = 10
SET2 = 11
SET3 = 12
SET4 = 13
SET5 = 14
SET6 = 15

STRAIGHT = 16

FULL_HOUSE = 17

CARE1 = 18
CARE2 = 19
CARE3 = 20
CARE4 = 21
CARE5 = 22
CARE6 = 23

POKER = 24



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
        print(self.act_face)
        
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
            print(self.name,'has now', len(self.__hand), 'dices in the hand')
        else:
            print('Nothing to getting')
    
    def roll_dices(self,dice_to_roll):
        
        for dice in self.__hand:
            if self.hand.index(dice) in dices_to_roll:
                dice.roll()
                
    def roll_dices(self):
        self.__state = NOTHING
        for dice in self.__hand:
            dice.roll()
        
        print(self.name,'rolled the dices')
        
    def show_hand(self):
        dice_to_show = []
        for dice in self.__hand:
            dice_to_show.append(str(dice))
        return dice_to_show
        
    def check_hand(self):
        hand = self.show_hand()
        pair = 0
        set_s = False
        self.__state = NOTHING
        
        if hand.count('1') == 2:
            self.__state += PAIR1
            pair += 1
        if hand.count('2') == 2:
            self.__state += PAIR2
            pair += 1
        if hand.count('3') == 2:
            self.__state += PAIR3
            pair += 1
        if hand.count('4') == 2:
            self.__state += PAIR4
            pair += 1
        if hand.count('5') == 2:
            self.__state += PAIR5
            pair += 1
        if hand.count('6') == 2:
            self.__state += PAIR6
            pair += 1
        if hand.count('1') == 3:
            self.__state += SET1
            set_s = True
        elif hand.count('2') == 3:
            self.__state += SET2
            set_s = True
        elif hand.count('3') == 3:
            self.__state += SET3
            set_s = True
        elif hand.count('4') == 3:
            self.__state += SET4
        elif hand.count('5') == 3:
            set_s = True
            self.__state += SET5
        elif hand.count('6') == 3:
            self.__state += SET6
            set_s = True
            
        if hand.count('1') == 4:
            self.__state += CARE1
        elif hand.count('2') == 4:
            self.__state += CARE2
        elif hand.count('3') == 4:
            self.__state += CARE3
        elif hand.count('4') == 4:
            self.__state += CARE4
        elif hand.count('5') == 4:
            self.__state += CARE5
        elif hand.count('6') == 4:
            self.__state += CARE6  
        
        if set_s == True and pair == 1: 
            self.__state += FULL_HOUSE
        
        if set(hand) == ['1','2','3','4','5'] or set(hand) == ['2','3','4','5','6']:
            self.__state += STRAIGHT
            
        if pair == 2:
            self.__state += TWO_PAIR
            
        return self.__state

        
def get_random_dices(num_of_dices,num_of_faces):
    dices = []
    for i in range(0,num_of_dices):
        dice = Dice(num_of_faces)
        dices.append(dice)
    return dices




def main():
    player1 = Player('Andrey')
    player2 = Player('Timofey')
    
    player1.get_dices(get_random_dices(NUM_OF_DICES,NUM_OF_FACES))
    player2.get_dices(get_random_dices(NUM_OF_DICES,NUM_OF_FACES))
    
    # ~ print(player1.name,'has:', player1.show_hand())
    # ~ print(player2.name,'has:', player2.show_hand())
    
    player1.roll_dices()
    print(player1.name,'has:', player1.show_hand(), "State:",player1.check_hand())
    player2.roll_dices()
    print(player2.name,'has:', player2.show_hand(),"State:",player2.check_hand())
    
    #dices_to_roll = input(len(hand),"dice(s) in the hand. Pick dices to reroll. (type dice's number by comma)").split(',')
    
    
if __name__=='__main__':
    main()   
