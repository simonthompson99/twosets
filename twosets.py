from xerox import paste,copy
from re import split

# get data from clipboard
def getClipboardData():
    return paste()

# send data to clipboard
def setClipboardData(data):
    copy(data)

# make intro to program
def hello():
    print("-" * 61)
    print("#-" * 13 + " TWOSETS " + "#-" * 13)
    print("-" * 61)

# split the data which comes in as a long string with linebreaks into separate list elements
# removes quotes and tabs from either side of string too
def splitData(string, delim):
    l = split(delim, string)
    return list(filter(None, [o.strip(' \r\n\t"\'') for o in l]))

# prints a little preview of a list
def prListHead(data, nrows):
    print('\n'.join(data[0:nrows]))
    print('...')

# gets name and data for a set, splits it, prints top of it, then returns a sorted, unique list of the elements
def getSet():
    n = input("Copy set to the clipboard and tell me the name: ")
    d = getClipboardData()
    l = splitData(d,'\r|\n')
    print(n + " looks like:")
    prListHead(l, 5)
    return([n,sorted(list(set(l)))])

# compares the one of the sets aaginst the meta-set
# since they're sorted we can just step through saying what matches what
# if we find a match in the set then mvoe forward in the set, if not, stay where we were in the list and move 
# forward in the meta-set
def compareTwoSortedLists(all, s1):
    out = []
    s1index = 0
    for allindex in range(0, len(all)):
        if all[allindex] == s1[min(s1index, len(s1) - 1)]:
            out.append(True)
            s1index+=1
        else:
            out.append(False)
    return out

# makes boolean list to a string list
def toStr(lst):
    return [str(i) for i in list(lst)]

# compares two lists and returns some summary stats
# makes single unique list from both lists
# compares each list against meta-list
# returns boolean lists for what is in what
def setCompare(s1, s2):
    all = sorted(list(set(s1[1] + s2[1])))
    inone = compareTwoSortedLists(all, s1[1])
    intwo = compareTwoSortedLists(all, s2[1])
    inboth = [a and b  for a, b in  zip(inone, intwo)]
    print("Number of unique ids: " + str(len(all)))
    print("Number missing from " + s1[0] + ": " + str(len(all) - sum(inone)))
    print("Number missing from " + s2[0] + ": " + str(len(all) - sum(intwo)))
    print("Number in both sets: " + str(sum(inboth)))
    return [all, toStr(inone), toStr(intwo), toStr(inboth)]

# writes out the table from setCompare to clipboard
def exportArray(arr):
    l = zip(arr[0], arr[1], arr[2], arr[3])
    s = 'id\tin '+one[0]+'\tin '+two[0]+'\tin both\n'+'\n'.join(['\t'.join(i) for i in l])
    setClipboardData(s)
    print("Table written to clipboard")


while True:
    hello()
    one = getSet()
    two = getSet()
    final = setCompare(one, two)
    exportArray(final)
