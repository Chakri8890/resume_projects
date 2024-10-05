'''1)Given a text and a wildcard pattern, implement wildcard pattern matching algorithm thatfinds if wildcard pattern is matched with text. The matching should cover the entire text (notpartial text).The wildcard pattern c an include the characters ‘?’ and ‘*’

‘?’ – matches any single character ‘*’ – Matches any sequence of characters (including the empty sequence) python'''


def wild_card(text,pattern):
    dp = [[False]* (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[0][0] = True

    for j in range(1,len(pattern)+1):
        if pattern[j-1] == '*':
            dp[0][j] = dp[0][j-1]
        
    for i in range(1,len(text)+1):
        for j in range(1,len(pattern)+1):
            if pattern[j-1] in {text[i-1],'?'}:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
    return dp[len(text)][len(pattern)] 

res = wild_card('hello','*')
print(res)


'''2)print the pattern 
                1
               3 2
              6 5 4
              6 5 4
               3 2
                1
'''

rows = 3
for i in range(0,rows+1):
    print(' ' *(rows-i),end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
print()
#for i in range():


'''
1)Accenture-August-24-2024
Replace the characters ch1 as ch2 and viceverse'''

def string(ch1,ch2):
    print(ch1)
    print(ch2)
    temp = ch1
    ch1 = ch2
    ch2 = temp
    print(ch1)
    print(ch2)
string('a','p')
print()


def functionn(str,ch1,ch2):
    temp = str.replace(ch1,'@')  #   @pples
    temp = temp.replace(ch2,ch1)  #  p@@les
    res = temp.replace('@',ch2)   #  paales
    print(res)
functionn('apples','a','p')        #output : paales
                    #OR

def function2(str,ch1,ch2):
    result = []
    for char in str:
        if char == ch1:
            result.append(ch2)
        elif char == ch2:
            result.append(ch1)
        else:
            result.append(char)
    final = ''.join(result)
    return final
print(function2('apples','a','p'))          #output : paales


'''2) I Need to return the count of second highest number in the given number/array'''

num = 375849        #second highest is: 4 , it returned 2 times so,o/p is: 2
digits = [int(digit) for digit in str(num)]
# highest = digits[0]
print(digits)
for i in range(len(digits)):
    for j in range(i+1,len(digits)):
        if digits[i] < digits[j]:
            lowest = digits[i]
        elif digits[i]>digits[j]:
            medi=digits[i]
            print('h',medi)


# num = 1
# digits = [int(digit) for digit in str(num)]
# print("Digits:", digits)
# highest = digits[0]
# for i in range(0, len(digits)):
    # for j in range(i+1, len(digits)):  # Ensure j starts from i+1 to avoid comparing the same index
        # if digits[i] < digits[j]:
            # highest = digits[j]  # Update highest when a larger digit is found
# 
# print("Highest digit:", highest)


num = 238453
list1 = [int(digit) for digit in str(num)]
maxi = list1[0]
for digit in list1:
    if digit > maxi:
        maxi = digit
print('maxi is',maxi)


'''to find the second highest number,
step i)store all the numbers in an array except first-highest number
step ii)store all the numbers in an array except first-highest number---this is the second highest number
                                    or
step i)delete first-highest number
step ii)print the highest number-----i,e second highest number
'''

numbers = 156348972         #second highest numberis 8
list2 = [int(digit) for digit in str(numbers)]
maximum = list2[0]
for num in list2:
    if num > maximum:
        maximum = num
list2.remove(maximum)

sec_high = list2[0]
for digit in list2:
    if digit > sec_high:
        sec_high = digit
print('Remaining list of int after removing first-largest integer is:',list2)
print('second highest is',sec_high)