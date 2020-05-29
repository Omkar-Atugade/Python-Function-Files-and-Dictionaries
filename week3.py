#1. Write a function called int_return that takes an integer as input and returns the same integer.


    #ANSWER:


    def int_return(x):
        return x

    int_return(10)



#2. Write a function called add that takes any number as its input and returns that sum with 2 added.


    #ANSWER :


    def add(x):
        return x+2
    add(4)



#3. Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.


    #ANSWER :


    def change(x):
        y=x+"Nice to meet you!"
        return y

    change("omkar")



#4. Write a function, accum, that takes a list of integers as input and returns the sum of those integers.


    #ANSWER :


    def accum(lst):
        tot=0
        for i in lst:
            tot=tot+i
        return tot
    lst=[2,1,3,4,5]



#5. Write a function, length, that takes in a list as the input.
    #If the length of the list is greater than or equal to 5, return “Longer than 5”.
    # If the length is less than 5, return “Less than 5”.



    #ANSWER :


    def length (lst):
        if len(lst)>=5:
            return "Longer than 5"
        else:
            return "Less than 5"

    length([])




#6. You will need to write two functions for this problem.
    #The first function, divide that takes in any number and returns that same number divided by 2.
    #The second function called sum should take any number, divide it by 2, and add 6.
    #It should return this new number.
    #You should call the divide function within the sum function.
    #Do not worry about decimals.


    #ANSWER :


    def divide(x):
        return x//2
    def sum(x):
        q=divide(x)
        t=q+6
        return t
    print (sum(2))



#7. Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.


    #ANSWER :

    olympics="Beijing","London","Rio","Tokyo"



#8. The list below, tuples_lst, is a list of tuples.
    # Create a list of the second elements of each tuple and assign this list to the variable country.



    #ANSWER :



        tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

        country=['China','England','Brazil','Japan']




#9. With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.



    #ANSWER :


        olymp = ('Rio', 'Brazil', 2016)

        city, country, year=olymp



#10. Define a function called info with five parameters: name, gender, age, bday_month, and hometown.
     #The function should then return a tuple with all five parameters in that order.



     #ANSWER :


        def info(name,gender,age,bday_month, hometown):
            return(name,gender,age,bday_month, hometown)
        info('Omkar','m',20,'feb','mumbai')



#11. Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics.
     # Create a list, num_medals, that contains only the number of medals for each country.
     #You must use the .items() method. Note: The .items() method provides a list of tuples.
     #Do not use .keys() method.


     #ANSWER :



            gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
            num_medals=[]
            for i in gold.items():
                print(i)
                num_medals=[i]
