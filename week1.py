#1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
    #Find the total number of characters in the file and save to the variable num.


    #ANSWER :

    fname=open('travel_plans.txt','r')

    x=fname.read()
    num=0
    for i in x:
        num=num+1
    fname.close()



#2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
    # Find the total number of words in the file and assign this value to the variable num_words.


    #ANSWER :

    fname=open('emotion_words.txt','r')

    x=fname.readlines().split()
    num_words=0
    for i in x:
        num_words=num_words+1
    fname.close()



#3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.


    #ANSWER:

    fname=open('school_prompt.txt','r')

    x=fname.readlines()
    num_lines=0
    for i in x:
        num_lines=num_lines+1
    fname.close()



#4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.


   #ANSWER:

   fname=open('school_prompt.txt','r')

   beginning_chars=fname.read(30)



#5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.


    #ANSWER :

    fname=open('school_prompt.txt','r')

    three=[]
    three=[line.split()[2] for line in fname]
    print (three)



#5.  Create a list called emotions that contains the first word of every line in emotion_words.txt.


    #ANSWER :

    fname=open('emotion_words.txt','r')

    emotions=[]
    emotions=[line.split()[0] for line in fname]
    print(emotions)



#6. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.


    #ANSWER:

    fname=open('travel_plans.txt','r')

    first_chars=fname.read(33)



#7. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.


    #ANSWER :

    fname=open('school_prompt.txt','r')

    x=fname.read().split()
    p_words=[word for word in x if 'p' in word]
