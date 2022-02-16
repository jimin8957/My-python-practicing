def calculate_change(payment, cost):
    change = payment - cost

    oman = change // 50000
    change -= oman * 50000

    man = change // 10000
    change -= man * 10000

    ocheon = change // 5000
    change -= ocheon * 5000

    cheon = change // 1000

    print("50000원 지폐: {}장".format(oman))
    print("10000원 지폐: {}장".format(man))
    print("5000원 지폐: {}장".format(ocheon))
    print("1000원 지폐: {}장".format(cheon))
    print("")

calculate_change(100000, 33000)

calculate_change(500000, 378000)
