import random

NUM_OF_FACES = 6
NUM_OF_DICES = 5

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
        for dice in self.__hand:
            dice.roll()
        print(self.name,'rolled the dices')
    def show_hand(self):
        dice_to_show = []
        for dice in self.__hand:
            dice_to_show.append(str(dice))
        return dice_to_show
    

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
    print(player1.name,'has:', player1.show_hand())
    player2.roll_dices()
    print(player2.name,'has:', player2.show_hand())
    
    #dices_to_roll = input(len(hand),"dice(s) in the hand. Pick dices to reroll. (type dice's number by comma)").split(',')
    
    
if __name__=='__main__':
    main()   
