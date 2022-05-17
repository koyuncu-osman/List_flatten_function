# List flatten function
a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def list_flatten(flatten):
    list_flatten = []
    for a in flatten:
        if type(a) is list:
            for b in a:
                if type(b) is list:
                    for c in b:
                        if type(c) is list:
                            for d in c:
                                list_flatten.append(d)                        
                        else:
                            list_flatten.append(c)
                else:
                    list_flatten.append(b)
        else:
            list_flatten.append(a)
    return list_flatten
print(list_flatten(a))

# Reversing Function
b = [[1, 2], [3, 4], [5, 6, 7]]
def reverse(x):
    list = x [::-1]
    list_1 = []
    for i in list:
        list_2 = i[::-1]
        list_1.append(list_2)
    return list_1
print(reverse(b))