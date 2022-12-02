
class Aide():

    def __init__(self):
        f = open("instructions", "r")
        l = f.readlines()
        f.close()
        for i in l:
            print(i.strip())


