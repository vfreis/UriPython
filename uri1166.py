def rentDebt():

    # Input Debt
    debt = int(input())

    #Input Payment
    payment = int(input())

    # Counter
    count = 1

    # Debt Payment Plan
    while debt > 0:
        print(f'pagamento: {count}')
        print(f'antes = {debt}')
        debt -= payment
        if debt < 0:
            debt = 0
        print(f'depois = {debt}')
        print('-----')
        count += 1
            

rentDebt()