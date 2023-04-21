import random

class Lotteri:

    def __init__(self):

        self.listvinster = [
            "Solstol",
            "Svettig strumpa",
            "Gethorn",
            "Leksaks Polisbil",
            "Skateboard",
            "Hårspänne",
            "Linjal",
            "2 l Tvål",
            "Mössa",
            "2 kilo gädda"
            "Pennskrin",
            "Ficklampa",
            "Munkhuve jacka",
            "Snovboard",
            "Skoter RMk 800",
            "Motorcykel",
            "Sockerkaka"
        ]
    
    def get_vinst(self):
        slumptal = random.randint(0, 19)
        return self.listvinster[slumptal]
       