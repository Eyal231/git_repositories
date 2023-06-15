import re

def fix_story_to_lower(the_original_story):
    new_clean_story = the_original_story.lower()
    x = re.findall(r'\b[a-z]+\b', new_clean_story)
    return x

l1 = '''the" "Amortized" part "Amortized Worst Case" These [1] =  operations rely on the "Amortized" part of
 "Amortized Worst Case". Individual actions may take surprisingly long, depending on the history of the container.
[2] = Popping the intermediate element at index k from a list of size n shifts all elements after k 
by one slot to the left using memmove. n - k elements have to be moved, so the operation is O(n - k). 
The best case is popping the second to last element, which necessitates one move, the worst case is popping 
the first element, which involves n - 1 moves. The average case for an average value of k is popping the 
element the middle of the list, which takes O(n/2) = O(n) operations.
[3] = For these operations, the worst case n is the maximum size the container ever 
achieved, rather than just the current size. For example, if N objects are added to a
 dictionary, then N-1 are deleted, the dictionary will still be sized for N objects (at least) u
 ntil another insertion is made.'''

fix_story = fix_story_to_lower(l1)
print(fix_story)
