with open('passbook.txt') as pb:
    transaction= pb.read().splitlines()
    print(transaction)
    total_deposit = 0
    total_withdrawal = 0

    for passbook_user_entry in transaction:
        user_entry = passbook_user_entry.split(':')
        print(user_entry)
        if user_entry[0] == 'D':
            total_deposit = total_deposit + int(user_entry[1])
        else:
            total_withdrawal = total_withdrawal + int(user_entry[1])

    print(total_withdrawal, total_deposit)
    amount_left = total_deposit - total_withdrawal
    print(amount_left)

