def variable_values_assignment_example():
    x = 2
    y = 3
    z = 5
    i, j, k = 7, 8, 9
    print(x, y, z, i, j, k)

'''
Now it's your turn to work with variables. 
The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. 
After each comment write a line of code that implements the instruction.

The current volume of a water reservoir (in cubic metres)
The amount of rainfall from a storm (in cubic metres)

- decrease the rainfall variable by 10% to account for runoff
- add the rainfall variable to the reservoir_volume variable
- increase reservoir_volume by 5% to account for stormwater that flows
  into the reservoir in the days following the storm
- decrease reservoir_volume by 5% to account for evaporation
- subtract 2.5e5 cubic metres from reservoir_volume to account for water
- that's piped to arid regions.
- print the new value of the reservoir_volume variable
'''
def reservoir_calculation():
    reservoir_volume = 4.445e8
    rainfall = 5e6
    rainfall *= 0.9
    reservoir_volume += rainfall
    reservoir_volume *= 1.05
    reservoir_volume *= 0.95
    reservoir_volume -= 2.5e5
    print(reservoir_volume)


if __name__ == '__main__':
    variable_values_assignment_example()
    reservoir_calculation()