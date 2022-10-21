from carte import Carte

count = 0
class Lemming:
    count = 0
    def __init__(self, pos, carte):
        Lemming.count += 1
        self.x = pos[0]
        self.y = pos[1]
        self.dir = 1
        self.carte = carte
        self.id = f"lemming{Lemming.count}"

    def __str__(self):
        return ">" if self.dir == 1 else "<"

    def action(self):
        if not self.carte.inside(self.x + self.dir, self.y):
            #print("le lemming se ret")
            self.dir = -self.dir

        if self.carte.libre(self.x + self.dir, self.y) and self.carte.get(self.x + self.dir,self.y) != '#':
                est_tombe = False
                self.carte.get(self.x, self.y).depart()
                # on change l'abcisse du lemming
                self.x += self.dir
                if self.carte.arrivee(self.x,self.y, self):
                    return True


                #print(f"Le lemming: {self.id} avance sur la case : ({self.x}, {self.y}) !")

                while self.carte.get(self.x,self.y + 1) == ' ' and self.y + 1 <= self.carte.hauteur() and self.carte.get(self.x,self.y + 1).libre():
                    self.carte.get(self.x,self.y).depart()
                    # on change l'ordonée du lemming
                    self.y += 1
                    if self.carte.arrivee(self.x,self.y, self):
                        return True
                    est_tombe = True

                if est_tombe:
                    #print(f"Le lemming: {self.id} tombe et atterit sur la case : ({self.x}, {self.y}) !")
        else:
            #print(f"Le lemming: {self.id} se retourne")
            self.dir = -self.dir

        return False











