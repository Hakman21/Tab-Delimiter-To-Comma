import winsound
import time

open("data.txt", "a").close()

def replace():

    with open("data.txt") as fin, open("newdatafile.txt", "w") as fout:
        for line in fin:
            fout.write(line.replace('\t', ','))

def start(password):

    auth = input("Enter password: ")

    if auth == password:
        view = replace()
    elif auth != password:
        print("Erasing data...")
        time.sleep(1)
        print("Locking account...")
        time.sleep(1)
        print("Contacting authorities...")
        time.sleep(3)
        print("Authorities contacted...")
        time.sleep(2)
        print("The police are on their way...")
        while True:
            winsound.Beep(14000, 3000)

password = "a"
ball = start(password)