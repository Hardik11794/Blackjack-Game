class Cards:
   
    def __init__(self,suits,rank):
        self.suits = suits
        self.rank = rank
   
    def __str__(self):
       return " %s of %s " %(self.suits,self.rank)




