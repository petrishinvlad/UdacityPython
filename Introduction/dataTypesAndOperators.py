def arithmetic_operations():
    print(1 + 2)
    print(3 * 5)
    print(8 - 7)
    print(126 / 5)
    print(123 % 4)
    print(123 // 4)
    print(3 ** 4)
    print('End of arithmetic operators example')

'''
My electricity bills for the last three months have been $23, $32 and $64. 
What is the average monthly electricity bill over the three month period? 
Write an expression to calculate the mean, and use print() to view the result.
'''
def avetageElectricityBill():
    print('Average electricity bill task')
    print((23 + 32 + 64) /3)
    print('End of task')

'''
In this quiz you're going to do some calculations for a tiler. 
Two parts of a floor need tiling. 
One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. 
Tiles come in packages of 6.
How many tiles are needed?
You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
'''
def calculate():
    print('Tiles calculation task')
    neededTiles = (9 * 7) + (7 * 5)
    print(neededTiles)
    print(102 - neededTiles)
    print('End of task')

if __name__ == '__main__':
    arithmetic_operations()   
    avetageElectricityBill() 
    calculate()
