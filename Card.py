import json

class Card:
    def __init__(self, id, cardlib):
        self.name = ""
        self.id = id
        self.getCard(id,cardlib)

    def getCard(self,id,cardlib):
        jcard = None
        for card in cardlib:
            if card["cardID"] == id:
                jcard = card
                break
        try:
            self.name = jcard["name"]
        except:
            print("invalid card id")
    


