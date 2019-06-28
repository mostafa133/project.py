# project.pytable = [["_ ", "_ ", "_ "],["_ ", "_ ", "_ "],["_ ", "_ ", "_ "]]

table[0] = ["_ ", "_ ", "_ "]
table[1]= ["_ ", "_ ", "_ "]
table[2] = ["_ ", "_ ", "_ "]
print(table[0] , table[1] , table[2])

while True:
    col =int(input("{press enter col"))
    row =int(input("{press enter row"))
    while col < 0 or col > 2 or row > 2 or row < 0:
        col =int(input("{press enter col"))
        row =int(input("{press enter row"))
    if table[row][col] == '_':
        break
    else:
        print("not empty")
