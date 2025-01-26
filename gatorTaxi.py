
# this funciton splits the data and gives list containing the ride details
def split(inputable):
    ridedet = []
    ridedet = [int(i) if i.isdigit() else i for i in inputable[0].split(',')]
    return ridedet


# Main functions that calls all the tree and heap
def startMeter(file1, file2):
    try:
        # opening both the files for input and output
        with open(file2, 'w') as out, open(file1, 'r') as inp:
            for rideD in inp:
                # this will return all non ovrlapping matches of pattern in string, as a list of string
                inputable = re.findall('\((.*?)\)', rideD)

                match rideD[0]:  # Switch case to see which case is to be worked on
                    case "G":  # Case for GetNextMin
                        # deletes th min from the mintree and minN is obtained to delete it from Red Black Tree
                        minN = min.GetMin()
                        if minN:
                            rbt.deleteN(minN[3])
                            out.write(str((minN[0], minN[1], minN[2]))+'\n')
                        else:
                            out.write("No active ride requests\n")

                    case "I":  # Case for Insert
                        # rideN, rideC, tripD = [int(i) if i.isdigit() else i for i in inputable[0].split(',')]
                        rideN, rideC, tripD = split(inputable)
                        rbtN = rbt.insertN(rideN, rideC, tripD)
                        if rbtN != rbt.N:
                            min.insertN(rideN, rideC, tripD, rbtN)
                        else:
                            out.write('Duplicate RideNumber \n')
                            break #As a condition provided, the program will be stopped when a duplicate ride is detected

                    case "P":  # Case for Print
                        range = split(inputable)
                        if len(range) != 1:
                            dis = rbt.Display(range[0], range[1])
                            if len(dis) != 0:
                                out.write(",".join(str(i) for i in dis) + '\n')
                            else:
                                out.write("(0,0,0)\n")
                        else:
                            dis = rbt.find(range[0])
                            if dis != rbt.N:
                                out.write(
                                    str((dis.rideN, dis.rideC, dis.tripD))+'\n')
                            else:
                                out.write("(0,0,0)\n")

                    case "C":  # case for CancelRide
                        rideN = int(inputable[0])
                        dnode = rbt.find(rideN)
                        if dnode == rbt.N:
                            continue
                        else:
                            rbt.deleteN(dnode)
                            min.deleteN(dnode)

                    case "U":  # case for UpdateRide
                        rideN, ntripD = split(inputable)
                        unode = rbt.find(rideN)
                        if unode != rbt.N:
                            rbt.Updation(unode, ntripD)
                            min.Updation(unode, ntripD)

    except IOError:
        print(f'There was a problem reading a file') 


if __name__ == '__main__':
    import re  # regex to use findall to input only data and avoid symbols
    import sys #taking filename from CLI
    # importing the minHeal and RBTree from datastructure
    from AdvanceDS import RBTree, minH
    rbt, min = RBTree(), minH()

    ''' try except to cover all the cases: 
          1: filename not included
          2: filename included but not extention
          3: filename with extention'''

    try:
        file1 = sys.argv[1]
        a = 'txt'
        if (a not in file1):
            startMeter(file1+'.txt', 'output_file.txt')
        elif (a in file1):
            startMeter(file1, 'output_file.txt')
    except IndexError:
        print(
            "File name not included while running: python3 gatorTaxi.py <input file name> ")

