open("data.txt", "a").close()

def replace():

    with open("data.txt") as fin, open("newdatafile.txt", "w") as fout:
        for line in fin:
            fout.write(line.replace('\t', ','))

hello = True
while hello == True:
            
    start = input("Start? y/n: ")
    
    if start == "y":
        hola = replace()
        hello = False
    elif start == "n":
        hello = False
    else:
        print(f"Invalid Input, please try again. ")
