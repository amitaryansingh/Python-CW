import pdb
pdb.set_trace()
def isleap(year):
    return year%400 == 0 and year%100 == 0 and year%4 == 0

if __name__ == '__main__':
    isleap()
