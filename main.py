with open("data.txt") as fin, open("newdatafile.txt", "w") as fout:
        for line in fin:
            fout.write(line.replace('\t', ','))
