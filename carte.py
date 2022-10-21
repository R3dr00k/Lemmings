from case import Case

class Carte:
    '''
    [Definition]
    La classe carte lit dans un fichier le labyrinthe et le stocke dans un tableau à double entrées.
    '''
    
    def __init__(self, filename):
        self.grotte = []
        count = 0
        with open(filename, "r") as f:
            for line in f.readlines():
                self.grotte.append([])

                for char in line:
                    if char != '\n':
                        self.grotte[count].append(Case(char))
                count += 1

    def find_entry(self, char='E'):
        for i in range(len(self.grotte)):
            for j in range(len(self.grotte[i])):
                if self.grotte[i][j] == char:
                    return (j, i)
        print("Aucun point d'entrée trouvé !")
        exit(0)

    def free_case(self):
        count = 0
        for line in self.grotte:
            for c in line:
                if c.case == ' ':
                    count += 1
        return count

    def get(self, x, y):
        return self.grotte[y][x]

    def libre(self, x, y):
        if self.get(x, y).libre():
            return True
        return False

    def arrivee(self, x, y, lem):
        if self.get(x, y).arrivee(lem):
            return True
        return False

    def inside(self, index, ligne):
        if index < 0 or index > len(self.grotte[ligne]) - 1:
            return False
        return True

    def hauteur(self):
        return len(self.grotte)

    def __repr__(self):
        repr = ""
        for line in self.grotte:
            for char in line:
                repr += char.representation()
            repr += '\n'
        return repr
