'''Sliding Window Technique
Sliding Window Technique is a method used to solve problems that involve subarray or substring or window.
{7, 3, 1, 2, 4, 5}
k = 3 //  window  size

Step 1: 7, 3, 1 -> 11

Step 2: 
3, 1, 2 | in : 2 out : 7 ---> 11 + 2 - 7 = 6
1, 2, 4 | in : 4 out : 3 ---> 6 + 4 - 3 = 7
2, 4, 5 | in : 5 out: 1 ---> 7 + 5 - 1

Step 3:
Max Sub-Array Sum = 11 (7+3+1) or (2+4+5)
'''

# nums = [5, 2, -1, 0, 3]
# n = len(nums)
# k = 3
# max_sum = 0

# for i in range(n-k + 1):
#     current_sum = 0
#     for j in range(k):
#         current_sum += nums[i + j]

#     max_sum = max(current_sum, max_sum)

# print(max_sum)

#OR

# nums = [5, 2, -1, 0, 3]
# n = len(nums)
# k = 3

# #Step 1
# maxSum = 0
# windowSum = 0 
# for i in range(k):
#     windowSum += nums[i]
# maxSum = windowSum

# # Step 2: Sliding Window Process
# for j in range(k, n):
#     windowSum = nums[j] - nums[j-k]
#     if windowSum > maxSum:
#         maxSum = windowSum

# #Step 3
# print(f"Max Sum is {maxSum}")

'''Question 2:
nums = [8, 0, 2, 1, 0, 3, 0, 6]
move all zeroes to the right side of the array 
without changing the order of the non zeroes numbers Using Bubble Sort Approach'''

# nums = [8, 0, 2, 1, 0, 3, 0, 6]
# n = len(nums)
# for i in range(n):
#     for j in range(0, n-1-i):  # number of iteratoin keep on reducing
#         if nums[j] == 0 and nums[j+1] != 0:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
# print(nums)

'''Question 3:
Selection Sort'''

# def selection_sort(nums):
#     n = len(nums)
#     for i in range(0, n):
#         min_index = i
#         for j in range(i+1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums
    
# print(selection_sort([5, 1, 3, 2, 7, 5]))

'''Question 4:
Sequence Checking (using sorting techniques such as selection sort or bubble sort)'''
# def selection_sort(nums):
#     n = len(nums)
#     for i in range(0, n):
#         min_index = i
#         for j in range(i+1, n):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums
    
# #Step 2
# def sequence_check(nums):
#     n = len(nums)
#     seqcount = 1
#     maxSeqCount = 0
#     for x in range(n-1):
#         next = nums[x] + 1
#         if next == nums[x+1]:
#             seqcount += 1
#         else:
#             if seqcount > maxSeqCount:
#                 maxSeqCount = seqcount
#             seqcount = 1
#     print(f" Max Seq Count is {maxSeqCount}")
    
# nums = [2, 1, 100, 3, 4, 101, 10, 102]

# sorted_nums = selection_sort(nums)
# print(sorted_nums)
# sequence_check(sorted_nums)

'''Question 5:
n1 = 8958
n2 = 785
Write a program to accept to positive integer values  in process to addition we have to count the carry values
1 1 1  -->  3
9 9 5 8
  7 8 5 (+)
9 7 4 3
'''

# def carry_count(n1, n2):
#     carry = 0
#     count = 0
#     while n1 > 0 or n2 > 0:
#         digit_sum =  (n1%10) + (n2%10) + carry

#         if digit_sum >= 10:
#             carry = 1
#             count += 1
#         else:
#             carry = 0

#         n1 //= 10
#         n2 //= 10
#     return count
# print(carry_count(8958, 785))

'''Question 6: 
Caesar Cipher Algorithm: Encryption and Decryption Technique we can use ACII Values
if message = SBIVM and Key = 1
then S - 1 = R, B - 1 = A, I - 1 = H, V - 1 = U, M - 1 = L'''

# def encrypt(text, s): #s = shift or key
#     result = ""

#     for i in range(len(text)):
#         char = text[i]

#         if (char.isupper()):
#             result += chr((ord(char) + s-65) % 26 + 65)
#         else:
#             result += chr((ord(char) + s - 97) % 26 + 97)

#     return result


# text = "ATTACKATONCE"
# s = 4
# print ("Text  : " + text)
# print ("Shift : " + str(s))
# print ("Cipher: " + encrypt(text,s))

'''Question 7:
Type Casting
'''

# string = "89541"
# total = 0
# for i in string:
#     result = ord(i) - ord('0')
#     total += result
# print(f"Sum of String is {total}")

'''Question 8:
nums = [2, 11, 7, 15]
target = 9
'''
# def twoSum(self, nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#     seen[num] = i


'''Question 9:
1. Display total stock value of the products present on amazon
2. Display product names whose price is greater than average price
'''
ecom_data = {
    "data": {
        "shop_name": "amazon",
        "catagory": [
            {
                "cat_name": "electronics",
                "products": [
                    {"product_name": "iphone", "qty": 23, "price": "53000"},
                    {"product_name": "ipad", "qty": 13, "price": "43000"},
                    {"product_name": "Air pods", "qty": 10, "price": "23000"}
                ]
            },
            {
                "cat_name": "Sports",
                "products": [
                    {"product_name": "cricket bat", "qty": 25, "price": "2000"},
                    {"product_name": "cricket ball", "qty": 10, "price": "500"}
                ]
            }
        ]
    }
}


total_stock_value = 0
total_price = 0
count = 0

for category in ecom_data["data"]["catagory"]:
    for product in category["products"]:
        price = int(product["price"])
        qty = product["qty"]
        
        total_stock_value += price * qty
        total_price += price
        count += 1

print("Total Stock Value:", total_stock_value)

# 2️⃣ Products whose price > average price
average_price = total_price / count
print("Average Price:", average_price)

print("Products with price greater than average:")
for category in ecom_data["data"]["catagory"]:
    for product in category["products"]:
        if int(product["price"]) > average_price:
            print(product["product_name"])
