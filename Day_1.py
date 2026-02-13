

'''Question 1'''

# n = 6
# Arr = [900 ,940, 950, 1100, 1500, 1800]
# Dep = [910, 1200, 1120, 1130, 1900, 2000]
# n = len(Arr)
# platform_required = 0
# min_platform = 0
# i = 0
# j = 0
# while i<n and j<n:
#     if Arr[i] <= Dep[j]:
#         platform_required += 1
#         if platform_required > min_platform:  #This is without using the max function 
#             min_platform = platform_required
#         i += 1
#     else:
#         platform_required -= 1
#         j += 1 
#     # max_platform = max(max_platform, platform_required)  #This is by using the max function
# print("Minimum platform required: ", min_platform)



'''2 nd Question For DSA'''

'''A group of football players are sitting in a circle with jersey numbers 10, 20, 30, 40, 50 and there corresponding seat \
numbers are 10 -> 1, 20 -> 2, 30 -> 3, 40 -> 4, 50 -> 5. The footballers shift there seat positions to the right hand side 
for n, where n is the numbers of shifts. Display seating arrangement of the footballers after n shifts.
*Arrangements of the values in place'''

# jersey = [10, 20, 30, 40, 50]
# # seat = [1, 2, 3, 4, 5]

# # def shift(jersey, left, right):

# n = len(jersey)
# k = 6
# # jersey[:] = [jersey[-1]] + jersey[0:n-1]
# # print(jersey)
# r = k%n     #because for ex if k = 153 we cant shift 153 times as it increase the time complexity hence we take 153%5 = 3
# for _ in range(0, r):
#     e = jersey.pop()
#     jersey.insert(0, e)
# print(jersey)

''' Greedy Methods = gets the best optimal solution (hint: if an array is not sorted then greedy method is "not" optimal hence
we have to sort the array or list in ascending or decending based on the requirements)'''

''' Question 3 : 
currency_notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
if price is 143 then using greedy approach we can give
100 + 20 + 20 + 2 + 1 '''

# currency_notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
# currency_notes.sort(reverse=True)
# n = len(currency_notes)
# total = 143
# payment = []
# for note in currency_notes:
#     while total >= currency_notes:
#         total -= note
#         payment.append(note)
# print(payment)

'''Question 4: Gold and Price Problem  Two Pointers
{7, 3, 2, 1, 6, 11, 8} -> 10 is the profit(because 1 is lowest price of gold and 11 is highest price of the gold then profit will be 11 - 1 = 10 i.e profit)
write a program to accept positive integer list of gold prices and print maximum profit that can be made with 1 buy transaction and 
with one sell transaction'''
#{15,7, 3, 2, 1, 6, 11, 8} -> profit 10
#{7, 4, 9, 1, 3, 2} -> profit 5

# price = [7, 3, 2, 1, 6, 11, 8]
# n = len(price)
# min_price = price[0]
# max_price = 0
# for i in range(n):
#     if price[i] < min_price:
#         min_price = price[i]
#     profit = price[i] - min_price
#     if profit > max_price:
#         max_price = profit

# print(f"Maximum Profit is : {max_price}")

'''Question 5: TO check the two numbers having same frequency or not
ex = n1 = 7889 and n2 = 8987  the frequency of 7 is 1-1 = 0 '''

# n1 = 7889
# n2 = 8987

# #hashTable
# hash_table = [0 for i in range(10)]  #List Comprehension
# while n1 != 0 or n2 != 0:

#     freq_n1 = n1 % 10
#     freq_n2 = n2 % 10

#     hash_table[freq_n1] += 1
#     hash_table[freq_n2] -= 1

#     n1 = n1//10
#     n2 = n2//10

# nofreqmatch = 0
# for x in hash_table:
#     if x != 0:
#         print("No Freq Match")
#         nofreqmatch = 1
#         break
# if nofreqmatch == 0:
#     print("Freq is Match")
# # elif nofreqmatch == 1:
# #     print("No Frequency Match")

# #Time Complexity is O(n)

'''Question 6: Excel Pattern
1 -> A
2 -> B
3 -> C
26 -> Z
27 -> AA
28 -> AB
52 -> AZ
53 -> BA
'''
# # Using Modulo we can solve this questions
# # def number_to_column(n):
# #     result = ""
    
# #     while n > 0:
# #         n -= 1                                          # adjust for 1-based indexing
# #         result = chr(n % 26 + ord('A')) + result        #ord function gives ascii values we will be converting to character by using chr
# #         n //= 26

# #     return result
# # print(number_to_column(52))


'''Question 7:
{([])} -> Balanced
([)]) -> Unbalanced
(){}[] -> Balanced
'''

# # def balanced(s):
# #     paren = 0
# #     curly = 0
# #     square = 0

# #     for char in s:
# #         if char == '(':
# #             paren += 1
# #         elif char == ')':
# #             paren -= 1
# #         elif curly == '{':
# #             curly += 1
# #         elif curly == '}':
# #             curly -= 1
# #         elif square == '[':
# #             square += 1
# #         elif square == ']':
# #             square -= 1
        
# #         if paren < 0 and curly < 0 and square < 0:
# #             return "Unbalanced" 
# #         elif paren == 0 and curly == 0 and square == 0:
# #             return "Balanced"

# # print(balanced("([)]"))

# parenthesis = "([])"
# stack = ["" for i in range(5)]
# top = -1

# for ch in parenthesis:
#     if ch == '{' or ch == '[' or ch == '(':
#         top += 1
#         stack[top] = ch
#     else:
#         if stack[top] == '{' and ch == '}':
#             stack[top] = ""
#             top -= 1

#         if stack[top] == '[' and ch == ']':
#             stack[top] = ""
#             top -= 1
#         if stack[top] == '(' and ch == ')':
#             stack[top] = ""
#             top -= 1

# print(f" Top : {top}")

#Time COmplexity will be o(n)

''' Question 8: 
Remove Duplicate Values from the sorted list
{0, 1, 1, 2, 3}
sp = 0 | fp = 1
if value of sp and fp not matching
sp++
update value of fp on sp
sp = 1 | fp = 1
sp = 1 | fp = 2
if sp value == fp value donot increment sp
sp = 1 | fp = 3
if value of sp and fp not matching
sp++ | update value of fp on sp
sp = 2 | fp = 3
update value of fp on sp
{0, 1, 2, 2, 3}
sp = 2 | fp = 4
sp ++ | update value of fp on sp
sp = 3 | fp = 4
{0, 1, 2, 3, 3}
 '''
# def remove_duplicate(nums):
#     n = len(nums)
#     sp = 0
#     for fp in range(1, n):
#         if nums[sp] != nums[fp]:
#             sp += 1
#             nums[sp] = nums[fp]
#     return nums, sp+1

# nums = [0, 1, 1, 2, 3]
# parr, displayLength = remove_duplicate(nums)
# resultData = [x for x in range(displayLength)]
# print(resultData)


''' Question 9:
[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] 
any given value between 1 to 3999
45 -> XLV
13 -> XIII
By using Greedy Approach which we did earlier
'''

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] 
n = 13
input = 45

romanValue = ""
for v in range(n):
    while input >= values[v]:
        romanValue += symbol[v]
        input -= values[v]
print(f"Roman Numerals : {romanValue}")

