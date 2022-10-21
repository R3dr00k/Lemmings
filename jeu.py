from case import Case
from lemming import Lemming
from carte import Carte
from time import sleep
import signal

class Jeu:
    '''
    classe Jeu contient la carte du type Carte composée de case de type Case ,et la liste des lemmings de type Lemming
    '''
    def __init__(self, filename):
        self.carte = Carte(filename)
        self.lemmings = []
        self.nb_lem_arrives = 0


    def affiche(self):
        print("Carte de la grotte :")
        print(self.carte, end)

    def tour(self):
        lem_to_remove = []

        for lem in self.lemmings:
            if lem.action():
                # si le lem est arrivé
                lem_to_remove.append(lem.id)
                self.nb_lem_arrives += 1

        for lem_name in lem_to_remove:
            for lem in self.lemmings:
                if lem.id == lem_name:
                    self.lemmings.remove(lem)

    def add_lem(self, lem):
        self.lemmings.append(lem)

    def demarrer(self):
        signal.signal(signal.SIGINT, signal_handler)

        jeu = True
        lemming_max = self.carte.free_case() // 3
        round = 0
        nb_lemmings = 0
        while jeu:
            print(f"round : {round}")
            if  round % 3 == 0 and nb_lemmings < lemming_max:
                self.add_lem(Lemming(self.carte.find_entry(), self.carte))
                nb_lemmings += 1

            if self.nb_lem_arrives == lemming_max:
                jeu = False
                print("Tous les lemmings sont arrivés !!")
            else:
                self.tour()
                self.affiche()
                round += 1
                sleep(0.5)


def signal_handler(sig, frame):
    print('Fin du jeu (SIGINT) !')
    sys.exit(0)

if __name__ == '__main__':
    jeu = Jeu("grotte.txt")
    jeu.demarrer()
