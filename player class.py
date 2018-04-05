import csv
with open("/Users/Alli/Downloads/combine.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    heights = []
    weights = []
    for row in readCSV:
        height = row[7]
        weight = row[8]

        heights.append(height)
        weights.append(weight)



class Player(object):
    def __init__(self):
        self.height = 0
        self.weight = 0
    def fill(self,playerheight,playerweight):
        self.height = playerheight
        self.weight = playerweight
def main():
    for x in range(len(heights)):
        playername = "p" + str(x)
        playername = Player
        playername.fill(playername,heights[x],weights[x])

main()
