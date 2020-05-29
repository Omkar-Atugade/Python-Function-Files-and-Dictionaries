#1. Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.


    #ANSWER :


        letters = "alwnfiwaksuezlaeiajsdl"
        sorted_letters=sorted(letters, reverse=True)



#2. Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.



    #ANSWER :



        animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
        animals_sorted=sorted(animals)



#3. The dictionary, medals, shows the medal count for six countries during the Rio Olympics.
    #Sort the country names so they appear alphabetically.
    #Save this list to the variable alphabetical.



    #ANSWER :



        medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

        alphabetical=sorted(medals)



#4. Given the same dictionary, medals, now sort by the medal count.
    #Save the three countries with the highest medal count to the list, top_three.


    #ANSWER :



        medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

        top_there=[]
        def g(k,d):
            return d[k]
        ks=medals.keys()

        top_three=sorted(ks,key=lambda x :g(x,medals), reverse=True)[:3]
