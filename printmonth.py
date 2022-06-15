#Program asks the user for a month name and start day and then prints the calendar for that month in a 6 row by 7 column grid.
#Ignoring issues of leap years, assume February has 28 days.

def main():
    
    # Obtain month name and number of days in the month
    month=input("Enter the month ('January', ..., 'December'):\n")
    
    if month=='September' or month=='April' or month=='June' or month=='November':
        days=30
    elif month=='February': # Ignoring leap years
        days=28
    elif month=='January' or month=='March' or month=='May' or month=='July' or month=='August' or month=='October' or month=='December':
        days=31
    else:
        days=-1 # Sentinal value to detect invalid input
    
    # Obtain start day and calculate start number for the grid
    start_day=input("Enter the start day ('Monday', ..., 'Sunday'):\n")
    
    if start_day=='Monday': 
        start=1
    elif start_day=='Tuesday':
        start=0
    elif start_day=='Wednesday':
        start=-1
    elif start_day=='Thursday':
        start=-2
    elif start_day=='Friday':
        start=-3
    elif start_day=='Saturday':
        start=-4
    else:
        start=-5
    
    # Print month name and column headings
    print(month)
    print('Mo Tu We Th Fr Sa Su')
    
    # Print dates
    for row in range(start, start+42, 7):
        if row>0 and row<=days:
            if row < 10:
                print(' ', end='')
            print(row, end='')
        else:
            print('  ', end='')
        for column in range(row+1, row+7):
            print(' ', end='')
            if column>0 and column<=days:
                if column < 10:
                    print(' ', end='')
                print(column, end='')
            else:
                print('  ', end='')
        print()
        
main()    
