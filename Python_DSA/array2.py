heros=['spider man','thor','hulk','iron man','captain america']


# 1. Length of the list
print("The length of list :",len(heros))


# 2. Add 'black panther' at the end of this list\
heros.append("black panther")
print("After added: ",heros)

#----------More Ways----------

    # heros.insert(5,"black panther")
    # print(heros)
    # heros.extend(["Black panther","Tiger"])
    # print(heros)
    # heros  = heros +["Black panther"]
    # print(heros)
    
    
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros.remove("black panther")
print("After removing :",heros)
heros.insert(3,"black panther")
print("Add after hulk",heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ["doctor strange"]  #slice and replace
print(heros)


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)