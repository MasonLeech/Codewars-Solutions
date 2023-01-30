def number(bus_stops):
    sum = 0 
    n_people = 0 
    for x in bus_stops:
        sum = x[0] - x[1]
        n_people += sum
    return n_people
