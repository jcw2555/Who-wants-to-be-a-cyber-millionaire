"""
Goes through the complete_millionaire.tsv file. It checks for any abnormal entries. If any are found, it will put that entry into another file.
"""

#turns list into a string to write into the suspicious entries file
def makeString(list, row):
    newstr = str(row) + ": \t "
    for i in list:
        newstr += i
        newstr += " "

    return newstr



def main():
    tsv = open("cybermillionaire/util/complete_millionaire.tsv", "r")
    alert = open("cybermillionaire/util/susEntries.txt", "w+")

    lines = tsv.readline()
    # gets rid of header line in file
    count = 1
    lines = tsv.readline()
    while (lines):
        # print("lines: " , lines);
        lineList = lines.split("\t")

        for i in range(len(lineList)):
            if(i == 6):
                if(int(lineList[i]) < 0 or int(lineList[i]) > 20):
                    alert.write(makeString(lineList, count))
            else:
                for letter in lineList[i]:
                    if (letter == ';' or letter == "'" or letter == '<'):    #checks for semi-colon or apostrophe
                        alert.write(makeString(lineList, count))
                        break;

        lines = tsv.readline()
        count +=1


main()



