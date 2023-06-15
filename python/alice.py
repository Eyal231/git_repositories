

def fix_story_to_lower(the_original_story):
    new_clean_story = the_original_story.lower()
    return(new_clean_story)

def clean_story_arrays(new_clean_story):
        i = [0]
        
        after_check = []
        for words_check in new_clean_story:
            tmp_word_to_check = words_check
            
            #print(new_clean_story)         
            if (str(tmp_word_to_check)).isalpha() == True:
                    after_check.append(tmp_word_to_check)
            else:
                    for letter in str(tmp_word_to_check)[:]:
                     # for check_letters in str(letter):
                         i = tmp_word_to_check
                         f = ()
                         #while(True):
                         for letter in i:
                            if letter.isalpha() == True:
                                f.append(letter)
                            else:
                                if letter.isalpha() == True:
                                    after_check.append(i)
                         #tmp_word_to_check = left_letters
                        #else:
                         #after_check.append('') 
        return(after_check)        
    # print(after_clean_arryas, end='')

l1 = '''These [1] =  operations rely on the "Amortized" part of "Amortized Worst Case". Individual actions may take surprisingly long, depending on the history of the container.

[2] = Popping the intermediate element at index k from a list of size n shifts all elements after k by one slot to the left using memmove. n - k elements have to be moved, so the operation is O(n - k). The best case is popping the second to last element, which necessitates one move, the worst case is popping the first element, which involves n - 1 moves. The average case for an average value of k is popping the element the middle of the list, which takes O(n/2) = O(n) operations.

[3] = For these operations, the worst case n is the maximum size the container ever achieved, rather than just the current size. For example, if N objects are added to a dictionary, then N-1 are deleted, the dictionary will still be sized for N objects (at least) until another insertion is made.'''
 # input("please insert your story to fix:")

new_clean_story = fix_story_to_lower(l1)
print((new_clean_story) + 'end')

after_lower_letters = new_clean_story.split(' ')
after_clean_arryas =  clean_story_arrays(after_lower_letters)
print(after_clean_arryas)

