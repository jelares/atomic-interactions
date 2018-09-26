from math import floor


class Atom:
    """"Atom object to be used in simulations"""
    def __init__(self, atom_num=1, elec_num=1, neut_num=0):
        self.atom_num = atom_num
        self.elec_num = elec_num
        self.neut_num = neut_num
        self.elec_mat, self.elec, self.qlevel = self.set_elec(elec_num)
        self.charge = atom_num - elec_num
        self.mass = atom_num + neut_num

    def set_elec(self, elec_num):
        elec_mat = [[0 for x in range(14)] for y in range(19)]
        elec = ""
        qlevel = 0
        if elec_num > 0:

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "1s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[0][1] is 0):
                elec_mat[0][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "2s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[1][1] is 0):
                elec_mat[1][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            i = 0
            elec += "2p" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[2][5] is 0) and (elec_mat[2][4] is 0):
                elec_mat[2][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i/2

            i = 1
            while (elec_num > 0) and (elec_mat[2][5] is 0):
                elec_mat[2][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "3s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[3][1] is 0):
                elec_mat[3][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            i = 0
            elec += "3p" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[5][5] is 0) and (elec_mat[5][4] is 0):
                elec_mat[5][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[5][5] is 0):
                elec_mat[5][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "4s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[6][1] is 0):
                elec_mat[6][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            i = 0
            elec += "3d" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[4][8] is 0) and (elec_mat[4][9] is 0):
                elec_mat[4][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[4][9] is 0):
                elec_mat[4][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            i = 0
            elec += "4p" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[9][5] is 0) and (elec_mat[9][4] is 0):
                elec_mat[9][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[9][5] is 0):
                elec_mat[9][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "5s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[10][1] is 0):
                elec_mat[10][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            i = 0
            elec += "4d" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[8][8] is 0) and (elec_mat[8][9] is 0):
                elec_mat[8][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[8][9] is 0):
                elec_mat[8][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            i = 0
            elec += "5p" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[13][5] is 0) and (elec_mat[13][4] is 0):
                elec_mat[13][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[13][5] is 0):
                elec_mat[13][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "6s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[14][1] is 0):
                elec_mat[14][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            i = 0
            elec += "4f" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[7][13] is 0) and (elec_mat[7][12] is 0):
                elec_mat[7][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[7][13] is 0):
                elec_mat[7][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i/2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            i = 0
            elec += "5d" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[12][8] is 0) and (elec_mat[12][9] is 0):
                elec_mat[12][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[12][9] is 0):
                elec_mat[12][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i / 2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            i = 0
            elec += "6p" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[16][5] is 0) and (elec_mat[16][4] is 0):
                elec_mat[16][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[16][5] is 0):
                elec_mat[16][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i / 2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            qlevel += 1 if elec_num > 0 else 0

            i = 0
            elec += "7s" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[17][1] is 0):
                elec_mat[17][i] = 1
                i += 1
                elec_num -= 1
            elec += (str(i) + " ") if i > 0 else ""

            i = 0
            elec += "5f" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[11][13] is 0) and (elec_mat[11][12] is 0):
                elec_mat[11][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[11][13] is 0):
                elec_mat[11][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i / 2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            i = 0
            elec += "6d" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[15][8] is 0) and (elec_mat[15][9] is 0):
                elec_mat[15][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[15][9] is 0):
                elec_mat[15][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i / 2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

            i = 0
            elec += "7p" if elec_num > 0 else ""
            while (elec_num > 0) and (elec_mat[18][5] is 0) and (elec_mat[18][4] is 0):
                elec_mat[18][i] = 1
                i += 2
                elec_num -= 1
            nxt_add = i / 2

            i = 1
            while (elec_num > 0) and (elec_mat[18][5] is 0):
                elec_mat[18][i] = 1
                i += 2
                elec_num -= 1
            nxt_add += floor(i / 2)
            elec += (str(int(nxt_add)) + " ") if nxt_add > 0 else "" 

        return elec_mat, elec, qlevel

    def str(self):
        info = (
            "\nAtomic Numer: " + str(self.atom_num) +
            "\nElectron Number: " + str(self.elec_num) +
            "\nNeutron Number: " + str(self.neut_num) +
            "\nAtomic Mass: " + str(self.mass) +
            "\nElectric Charge: " + str(self.charge) +
            "\nEnergy Levels: " + str(self.qlevel) +
            "\n\nElectron Configuration: " + self.elec + "\n")

        info += "\n\nQuantum Level 1 S: "
        for i in range(2):
            info += str(self.elec_mat[0][i])

        info += "\n\nQuantum Level 2 S: "
        for i in range(2):
            info += str(self.elec_mat[1][i])
        info += "\nQuantum Level 2 P: "
        for i in range(6):
            info += str(self.elec_mat[2][i])

        info += "\n\nQuantum Level 3 S: "
        for i in range(2):
            info += str(self.elec_mat[3][i])
        info += "\nQuantum Level 3 D: "
        for i in range(10):
            info += str(self.elec_mat[4][i])
        info += "\nQuantum Level 3 P: "
        for i in range(6):
            info += str(self.elec_mat[5][i])

        info += "\n\nQuantum Level 4 S: "
        for i in range(2):
            info += str(self.elec_mat[6][i])
        info += "\nQuantum Level 4 F: "
        for i in range(14):
            info += str(self.elec_mat[7][i])
        info += "\nQuantum Level 4 D: "
        for i in range(10):
            info += str(self.elec_mat[8][i])
        info += "\nQuantum Level 4 P: "
        for i in range(6):
            info += str(self.elec_mat[9][i])

        info += "\n\nQuantum Level 5 S: "
        for i in range(2):
            info += str(self.elec_mat[10][i])
        info += "\nQuantum Level 5 F: "
        for i in range(14):
            info += str(self.elec_mat[11][i])
        info += "\nQuantum Level 5 D: "
        for i in range(10):
            info += str(self.elec_mat[12][i])
        info += "\nQuantum Level 5 P: "
        for i in range(6):
            info += str(self.elec_mat[13][i])

        info += "\n\nQuantum Level 6 S: "
        for i in range(2):
            info += str(self.elec_mat[14][i])
        info += "\nQuantum Level 6 D: "
        for i in range(10):
            info += str(self.elec_mat[15][i])
        info += "\nQuantum Level 6 P: "
        for i in range(6):
            info += str(self.elec_mat[16][i])

        info += "\n\nQuantum Level 7 S: "
        for i in range(2):
            info += str(self.elec_mat[17][i])
        info += "\nQuantum Level 7 P: "
        for i in range(6):
            info += str(self.elec_mat[18][i])

        return info
