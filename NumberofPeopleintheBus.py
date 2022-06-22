def number(bus_stops):
    sum = 0
    minus = 0
    for i in range(len(bus_stops)):
        sum +=bus_stops[i][0]
        minus +=bus_stops[i][1]
    sum = sum-minus
    return sum

  




print(number([[23,23],[12, 12],[1, 1]]))

