def ReadTitlesCSV(filename):
    items=list()
    with open(filename,"r") as csvf:
        reader = csv.reader(csvf, delimiter=';', quotechar='"')
        for item in reader:
            if item:
                title = dict()
                title['title'] = item[0]
                title['score'] = float(item[1])
                items.append(title)
        csvf.close()
    return items

def NodeStrength(pers):
    score = 0
    print(pers.net_worth)
    if pers.net_worth > 10*10**9:
        score +=4
    elif pers.net_worth > 10**9:
        score+=3
    elif pers.net_worth > 100*10*6:
        score +=2
    elif pers.net_worth > 10*10**6:
        score +=1
    
    if pers.active:
        score +=.5
    
    titles = ReadTitlesCSV("titles.csv")
    for title in titles:
        if title['title'] in pers.positions:
            score += title['score']
    
    
    return score

def Test():
    pers = Person("Test Person")
    pers.set_net_worth(10**10)
    pers.set_active = True
    pers.add_position("CEO")
    pers.add_institution("Columbia")

    print(NodeStrength(pers))
    #ReadTitlesCSV("titles.csv")
