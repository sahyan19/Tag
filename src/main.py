import turtle
from move import*

def main():
    file = "../data/test.txt"
    path = readPath(file)
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Tage your name")
    curseur = turtle.Turtle()
    curseur.color("white")
    for i in range(len(path)):
        if path[i][0] == 'f':
            forward(curseur, int(path[i][1]))
        elif path[i][0] == 'l':
            turnLeft(curseur, int(path[i][1]))
        elif path[i][0] == 'r':
            turnRight(curseur, int(path[i][1]))
    
    wn.mainloop()

if __name__ == "__main__":
    main()