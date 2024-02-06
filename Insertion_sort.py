def insertion_sort(lista):  # Define the function
    indexing = range(1, len(lista))  # Define the range of indices to iterate over (excluding the first one)
    for i in indexing:  # Loop over every element of the list except the first one
        val_to_sort = lista[i]  # Variable to save every element in the list
        while lista[i - 1] > val_to_sort and i > 0:  # If the element is bigger than its previous element
            lista[i], lista[i - 1] = lista[i - 1], lista[i]  # Swap them
            i -= 1  # Decrement i to move to the previous index in the list
    return lista

# Check the insertion_sort function
print(insertion_sort([2, 85, 498, 513, 21, 0, 12, 1, 156]))
