import re

nut_ = ("peanut", "almond", "cashew", "nut")
dairy_ = ("milk", "cheese", "butter", "dairy")
gluten_ = ("bread", "gluten")


###################test cases
# result = shoppingsort([("zx", "mexico", ("tomato", "beef")), ("ax", "mexico", ("tomato", "beef")), ("cx", "mexico", ("bread", "meat"))], "", 0, 0, 0)
# result = shoppingsort([("burger", "mexico", ("tomato", "beef")), ("burger", "ax", ("tomato", "beef")), ("hot dog", "mexico", ("bread", "meat"))], "burg", 0, 0, 1)
# sorts a list of data elements in format ((foodname,country,(list of ingredients...)...), search query string, allergens as a 1 or 0 representing true or false,,,
def shoppingsort(datalist, search, nut, dairy, gluten):
    datacount = 0
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
        if match == 0:
            datalist.pop(datacount)
        datacount += 1
    datalist.sort()
    return datalist


#result = shoppingsort([("Zx", "mexico", ("tomato", "beef")), ("Ax", "mexico", ("tomato", "beef")), ("Cx", "mexico", ("bread", "meat"))], "", 0, 0, 0)
#result = shoppingsort([("good burger", "mexico", ("tomato", "beef")), ("bad burger", "ax", ("tomato", "beef")), ("hot dog", "mexico", ("bread", "meat"))], "burg", 0, 0, 1)
#print(result)


# data=[(foodname,country,(ingredients...)),(),()...]
def tuptostring(tup):
    ret = ""
    for ing in tup:
        ret += ing + " "

    return ret


def datatostring(data):
    ret = ""
    for rec in data:
        ret += rec[0] + " from " + rec[1] + "\n\tIngredients: " + tuptostring(rec[2]) + "\n\n"
    return ret

# print(datatostring([("beef","mexico",("meat", "mystery meat")),("hamburger","USA",("bread","meat","chesse"))]))
