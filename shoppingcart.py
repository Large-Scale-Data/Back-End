import re
#allergens / preferences tuple of ingredients to exclude 
nut_ = ("peanut", "almond", "cashew", "nut")
dairy_ = ("milk", "cheese", "butter", "dairy")
gluten_ = ("bread", "gluten")
vegitarian_=("meat","beef","pork","poultry","chicken","fish")
#also sets vegitarian and dairy flags on 
vegan_=("egg","honey","mayo")

# sorts a list of data elements in format ((foodname,country,(list of ingredients...)...), search query string, allergens as a 1 or 0 representing true or false,,,
def shoppingsort(datalist, search, nut, dairy, gluten, vegi, vegan):
    dataremovelist = []
    datacount=0
    if vegan == 1:
        dairy = 1
        vegi = 1
    for data in datalist:
        match = 0
        if re.search(r"" + search, data[0], re.IGNORECASE):
            match = 1
            if nut == 1:
                for i in nut_:
                    for ing in data[2]:
                        if re.search(r"" + i, ing, re.IGNORECASE):
                            match = 0
                            break
            if dairy == 1:
                for i in dairy_:
                    for ing in data[2]:
                        if re.search(r"" + i, ing, re.IGNORECASE):
                            match = 0
                            break
            if gluten == 1:
                for i in gluten_:
                    for ing in data[2]:
                        if re.search(r"" + i, ing, re.IGNORECASE):
                            match = 0
                            break
            if vegi == 1:
                for i in vegitarian_:
                    for ing in data[2]:
                        print(data[0],i,ing)
                        if re.search(r"" + i, ing, re.IGNORECASE):
                            match = 0
                            break
            if vegan == 1:
                for i in vegan_:
                    for ing in data[2]:
                        if re.search(r"" + i, ing, re.IGNORECASE):
                            match = 0
                            break
        if match == 0:
            dataremovelist.append(datacount)
        datacount += 1
    adj=0
    for i in dataremovelist:
        datalist.pop(i-adj)
        adj+=1
    datalist.sort()
    return datalist

#tests
#result = shoppingsort([("Zx", "mexico", ("tomato", "beef")), ("Ax", "mexico", ("tomato", "beef","meat")), ("Cx", "mexico", ("bread", "meat")),("tx", "mexico", ("tomato","grass"))], "", 0, 0, 0,1,1)
#result = shoppingsort([("hat","africa",("cloth","dye")),("good burger", "mexico", ("tomato", "beef")), ("bad burger", "ax", ("tomato", "beef", "bread")), ("hot dog", "mexico", ("bread", "meat"))], "burg", 1, 1, 1, 0, 0)
#print(result)


#tup=("","","",...)
def tuptostring(tup):
    ret = ""
    for ing in tup:
        ret += ing + " "

    return ret

# data=[(foodname,country,(ingredients...)),(),()...]
def datatostring(data):
    ret = ""
    for rec in data:
        ret += rec[0] + " from " + rec[1] + "\n\tIngredients: " + tuptostring(rec[2]) + "\n\n"
    return ret
#tests
#print(datatostring([("beef","mexico",("meat", "mystery meat")),("hamburger","USA",("bread","meat","chesse"))]))
#print(datatostring(result))