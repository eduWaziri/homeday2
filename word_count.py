def words(word):
    new_words_array = [] #to store new list with strings converted to int

    # loop through this list - check for numbers...
    for theword in (word.strip()).split():#apparently not defining separater also checks for white space and new lines
       if theword.isdigit():
           new_int = int(theword)
           new_words_array.append(new_int)
           #print type(int(theword))
       else:
           new_words_array.append(theword)

    result_dict = dict( [(i, new_words_array.count(i)) for i in set(new_words_array)])

    #counts = Counter(new_words_array)

    #return counts
    return result_dict