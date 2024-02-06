def bubble(lista): # intial the val of the list i wanna to sort
    index = len(lista) - 1 # index val
    state = False #state to start the loop

    while not state: # while not True (not sorted)
        state = True # change the state 
        for i in range(0, index): # loop over evrey element
            if lista[i] > lista[i + 1]: # if element is bigger than the element +1
                state = False # its not sorted
                lista[i], lista[i + 1] = lista[i + 1], lista[i] # change them
    print (lista)            
    
bubble([2,4,1,3,2,1,7,0,9,11,5,0])