def leapYears():
    # Input Start
    start = int(input())

    # Input End
    end = int(input())

    # Count leap years on interval
    leapYear = 0
    while start <= end:
        if start % 4 == 0 and start % 100 != 0 or start % 400 == 0:
            leapYear += 1
            print(start)
        start += 1
    print(f'bissextos: {leapYear}')

leapYears()