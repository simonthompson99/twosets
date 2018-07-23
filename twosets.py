from xerox import paste,copy
from numpy import unique,in1d
from re import split

def getClipboardData():
    #p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    #retcode = p.wait()
    #data = p.stdout.read()
    #return data.decode()
    return paste()

def setClipboardData(data):
    #p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    #p.stdin.write(data)
    #p.stdin.close()
    #retcode = p.wait()
    copy(data)

def hello():
    print("-" * 61)
    print("#-" * 13 + " TWOSETS " + "#-" * 13)
    print("-" * 61)

def splitData(string, delim):
    l = split(delim, string)
    return list(filter(None, [o.strip(' \r\n\t"') for o in l]))

def prListHead(data, nrows):
    print('\n'.join(data[0:nrows]))
    print('...')

def getSet():
    n = input("Copy set to the clipboard and tell me the name: ")
    d = getClipboardData()
    l = splitData(d,'\r|\n')
    print(n + " looks like:")
    prListHead(l, 5)
    return([n,l])

def setCompare(s1, s2):
    all = unique(s1[1] + s2[1])
    inone = in1d(all, s1[1])
    intwo = in1d(all, s2[1])
    inboth = inone & intwo
    print("Number of unique ids: " + str(len(all)))
    print("Number missing from " + s1[0] + ": " + str(len(all) - sum(inone)))
    print("Number missing from " + s2[0] + ": " + str(len(all) - sum(intwo)))
    print("Number in both sets: " + str(sum(inboth)))
    return [list(all), arrToStr(inone), arrToStr(intwo), arrToStr(inboth)]

def exportArray(arr):
    l = zip(arr[0], arr[1], arr[2], arr[3])
    s = 'id\tin '+one[0]+'\tin '+two[0]+'\tin both\n'+'\n'.join(['\t'.join(i) for i in l])
    setClipboardData(s)
    print("Table written to clipboard")

def arrToStr(arr):
    return [str(i) for i in list(arr)]

while True:
    hello()
    one = getSet()
    two = getSet()
    final = setCompare(one, two)
    exportArray(final)

#inone = [i in one[1] for i in all]
#intwo = [i in two[1] for i in all]
#inboth = [i in one[1].intersection(two[1]) for i in all] 
#
#inonestr = [str(i) for i in inone]
#intwostr = [str(i) for i in intwo]
#inbothstr = [str(i) for i in inboth]
#

#out = [header] + list(zip(all, inonestr, intwostr, inbothstr))
#celljoiner = "\t".join
#rowjoiner = "\r".join
#exp = rowjoiner([celljoiner(cells) for cells in out])
#
#setClipboardData(exp.encode())
