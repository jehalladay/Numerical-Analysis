
def fibonnacci(n): 
    ''' we will write a simple function to compute the n-th fibonnacci number'''

    if n == 0 or n == 1:
        return n
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

