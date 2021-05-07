
def almost_there(num):
    """if abs(100-num) <= 10 or abs(200-num) <= 10:
        print('WOW')
    else:
        print('No')"""

    return abs(100-num) <= 10 or abs(200-num) <= 10

#print(almost_there(150))

def has_33(*nums):

    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
    

#print(has_33(1,5,3,85,3,3))

def paper_doll(text):
    result = ''

    for x in text:
        result += x*3
   
    return result

#print(paper_doll('November'))

def blackjack(a,b,c):
    
    
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return "BUST"

#print(blackjack(9,9,11))

def spy_game(arr):

    code = [0,0,7,'x']

    for num in arr:
        if num == code[0]:
            code.pop(0)
    
    return len(code) == 1
        

print(spy_game([1,2,3,0,0,1,2,7]))
    

        
