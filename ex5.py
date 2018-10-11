Start_bottles = 99
Bottles_left = Start_bottles - 1

while Start_bottles != 0:
    print (str(Start_bottles)+(" bottles of beer on the wall, ")+str(Start_bottles)+(" bottles of beer. Takes one down, pass it around, ")+str(Bottles_left)+(" bottles of beer on the wall"))
    Start_bottles=Start_bottles -1
    Bottles_left= Start_bottles-1
    if Start_bottles==1:
        print(str(Start_bottles)+( "bottle of beer on the wall, ")+str(Start_bottles)+(" bottle of beer! So take it down, pass it around, no more bottles of beer on the wall!"))
        break
        


    
"""
if Start_bottles == 1:
    

x=99

for x in range (99):
    print ((x)+" bottles of beer on the wall, ")
"""
