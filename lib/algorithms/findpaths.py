nodestable = {1: [2, 3, 4], 2: [3, 5], 3: [4, 5], 4: [], 5: [6, 7], 6: [3, 7], 7: []}

def findpaths(labelNodeStart, labelNodeDest):
    print(nodestable)
    def findpath(currentlabel, labelNodeDest, currentpath):
        #print(currentlabel," -?-> ",labelNodeDest,", by ",currentpath)
        if currentlabel == labelNodeDest:
            paths.append(currentpath)
        else :
            for nextnode in nodestable[currentlabel]:
                if nextnode not in currentpath:
                    findpath(nextnode, labelNodeDest, currentpath+[nextnode])
    paths = []
    findpath(labelNodeStart, labelNodeDest, [labelNodeStart])
    return paths

paths = findpaths(1, 7)

for p in paths :
    print(p)
