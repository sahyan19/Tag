import turtle

def readPath(filename: str) -> list[str]:
    """
        Read a text file and create a list containing the data from the file.
        
        parameter:
            filename (str) : containing the path to the file to be read
            
        example :
            filename = "./test.txt"
            readPath(filename)

    
    """
    path = []
    brute = [line.strip() for line in open(filename, 'r')]
    for i in brute:
        path.append(i.split())
    return path


def forward(curseur, distance=0):
    curseur.forward(distance)

def turnLeft(curseur, angle=0):
    curseur.left(angle)
    
def turnRight(curseur, angle=0):
    curseur.right(angle)
    