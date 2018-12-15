def rows(n):                    #row function
    i = 0
    ii = 0
    m = []  #row divider array
    l = []  #column divider array
    while i < n:
        m.append(' ---')        #add in row dividers
        i += 1
    while ii <= n:      #add in column dividers
        l.append('|')
        ii += 1
    print ''.join(m)    #join together to remove ''
    print '   '.join(l)

def end(n):
    i = 0
    m = []
    while i < n:
        m.append(' ---')
        i += 1
    print ''.join(m)

    
def board():
    i = 0
    ii = 0
    n = input('What size game board would you like to make? ')
    while i < n:    #recursive row function
        rows(n)
        i += 1
    end(n)  #cap it
   
    

board()
