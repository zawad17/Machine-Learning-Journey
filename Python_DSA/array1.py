#----------Q1---------------
#1. In Feb, how many dollars you spent extra compare to January?


listOfExpense = [2200, 2350, 2600, 2130, 2190]
print(f"In Feb,Extra compare to Jan: {listOfExpense[1]-listOfExpense[0]}")

#----------Q2---------------
#2. Find out your total expense in first quarter (first three months) of the year.

sum = 0 #define sum is 0
for i in listOfExpense[:3]:
    sum = sum+i
print("Total expense :",sum)

#----------Q3---------------
#3. Find out if you spent exactly 2000 dollars in any month

for index, value in enumerate(listOfExpense [0:4]):  ## need index and value use enumerate 
    if (value==2000):
        print(f"{value} Found in index no {index}")  
        break
else :
    print("2000 is Not found")
        
#----------Q4---------------
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
     
listOfExpense.append(1980)
print("After adding june:",listOfExpense)

#----------Q5---------------
# 5. You returned an item that you bought in a month of April and
#    got a refund of 200$. Make a correction to your monthly expense list
#    based on this

listOfExpense[3] = listOfExpense[3]-200
corrected_list = listOfExpense
print("After correct the expense of april month:",corrected_list)