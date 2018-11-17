'''
Calculate and print the total sales for the week from the data provided.
Print out a string of the form "This week's total sales: xxx",
where xxx will be the actual total of all the numbers.
You’ll need to change the type of the input data in order
to calculate that total.
'''


if __name__ == '__main__':
    mon_sales = "121"
    tues_sales = "105"
    wed_sales = "110"
    thurs_sales = "98"
    fri_sales = "95"
    weekly_sales = [mon_sales , tues_sales, wed_sales, thurs_sales, fri_sales]
    print("This week\'s total sales: " + str(sum([int(day_sale) for day_sale in weekly_sales])))
