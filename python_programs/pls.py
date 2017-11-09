books = ["GEN","EXO","GEN"]
notbooks = ["LEV","PSA"]
toknwords = []
ntoknwords = ["GEN","EXO"]
availablelan = ["GEN","EXO","LEV","NUM","PSA","JOL"]
b = set(books) - set(availablelan)
c =set(notbooks) - set(availablelan)
print b
print c
if  not b and not c:
    if books:
        for bkn in books:
            toknwords.append(bkn)
        stoknwords = set(toknwords)
        print (list(stoknwords))
