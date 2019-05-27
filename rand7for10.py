# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

#Analysis:  since rand7 is less than 10, we have to run ran7 at least twice.  if we use coordinates, we will have 49 samples, and 9 discarded.  <1/5.  
#if we use x+y, 4 out of 10 will be discarded.  coordinates is better.


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        import random   

        random10 =50
        while random10 > 40:
            x = random.randint(1,7)
            y = random.randint(1,7)
            #x = rand7()
            #y = rand7()
            random10 = (x-1) * 7 + y

        return (random10 - 1) % 10 + 1
