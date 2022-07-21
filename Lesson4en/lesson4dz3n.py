def filter_function(func,iteration):
    a = []
    for i in range(len(iteration)):
        if func(iteration[i]) == True:
            a.append(iteration[i])
    return a
func = lambda x: type(x) == str
iteration = [5, 20, "alex", 2.5, "bob"]
print(filter_function(func, iteration))