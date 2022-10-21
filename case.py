class Case:
    def __init__(self, case):
        self.case = case
        self.lemming = None

    def representation(self):
        if self.lemming == None:
            return f"{self.case}"
        else:
            return f"{self.lemming}"

    def __eq__(self, c):
        if c == self.case:
            return True
        return False

    def libre(self):
        if self.lemming == None:
            return True
        return False

    def depart(self):
        self.lemming = None

    def arrivee(self, lem):
        if self.case == 'O':
            #print(f"le lemming {lem.id} est arrivé !")
            self.lemming = None
            return True
        else:
            self.lemming = lem
            return False
