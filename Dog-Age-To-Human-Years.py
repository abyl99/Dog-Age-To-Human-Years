#define and set variables 
def calculator():
        
#input dog age
    dog_age = input('Input dog age: ')
    try:
    
    #Cast to float
        dog_age = float(dog_age)
        print(dog_age)
    #Calculate dog's age in human years
        if(dog_age >= 0 and dog_age <= 1): #if dog age is between 0 and 1
            human_age = 15 * dog_age
        elif(dog_age > 1 and dog_age <= 2): #if dog age is between 1 and 2
            human_age = 12 * dog_age
        elif(dog_age > 2 and dog_age <= 3): #if dog age is between 2 and 3
            human_age = 9.3 * dog_age
        elif(dog_age > 3 and dog_age <= 4): #if dog age is between 3 and 4
            human_age = 8 * dog_age
        elif(dog_age > 4 and dog_age <= 5): #if dog age is between 4 and 5
            human_age = 7.2 * dog_age
        elif(dog_age >= 5): #if dog's age is greater than 5
            human_age = 7 * dog_age
        print('The given dog age', dog_age, 'is', human_age, 'in human years')
    except:
        print('Invalid, age cannot be negative number')
calculator()
