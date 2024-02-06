def quicksort(lista): # define the function
    lenght = len(lista) # define the lenght
    if lenght < 1: # if the list is one item return it 
        return lista #........
    else : 
        pivot = lista.pop() # take the last item to compare it 
    items_greater = [] # intialize the var for greater than our pivot 
    items_smaller = [] # ...................... for smaller 

    for i in lista: # loop in evrey item in the list 
        if i < pivot : # if it smaller than pivot put it on items smaller 
            items_smaller.append(i)
        else:
            items_greater.append(i) # vica versa
    return quicksort(items_smaller) + [pivot] + quicksort(items_greater) # merge them 

print(quicksort([2,4,5,3,1,96,8,351,8,463521,35,12,11,1,0])) # test