#Task 1
# #1
# try:
#    def get_keys_with_value_true(dict):
#       return [key for key, value in dict.items() if value is True]

#    dict = {
#       "a": True,
#       "b": False,
#       "c": True
#    }

#    result = get_keys_with_value_true(dict)
#    print(result)

# except ValueError:
#    print('error')

# #2
# try:
#    def get_unique_elements(list):
#       return [item for item in list if list.count(item) == 1]

#    input_list = input()
#    list = [int(num) for num in input_list.split(',')]

#    result = get_unique_elements(list)
#    print(result)

# except ValueError:
#    print('error')

# #3
# try:
#    def get_date_in_format(date):
#       year, month, day = map(int, date.split('.'))
#       formatted_date = f"{day:02d}.{month:02d}.{year}"
#       return formatted_date

#    input_date = input("Введите дату в формате 'год.месяц.день': ")

#    formatted_date = get_date_in_format(input_date)
#    print(formatted_date)
# except ValueError:
#    print('error')

# #4
# try:
#    def get_elements_with_no_more_than_two_occurrences(list):
#       return [item for item in set(list) if list.count(item) == 2]
#    input_list = input("Введите список чисел через запятую: ")
#    list = [int(num) for num in input_list.split(',')]

#    result = get_elements_with_no_more_than_two_occurrences(list)
#    print(result)

# except ValueError:
#    print('error')

# #5
# try:
#    def get_words_from_string(input_string):
#       words = input_string.split()
#       return words

#    input_word = input("Введите строку: ")

#    result = get_words_from_string(input_word)
#    print(result)
# except ValueError:
#    print('error')

# #Task 2
# #6
# try:
#    def get_unique_elements_with_count(list):
#       count = {}
#       for item in list:
#          if item in count:
#             count[item] += 1
#          else:
#             count[item] = 1

#       return count

#    input_list = input()
#    list = [int(num) for num in input_list.split(',')]

#    result = get_unique_elements_with_count(list)
#    print(result)
# except ValueError:
#    print('error')

# #7
# try:
#    def is_prime(num):
#       if num < 2:
#          return False
#       for i in range(2, int(num ** 0.5) + 1):
#          if num % i == 0:
#             return False
#       return True


#    def get_prime_numbers(n):
#       prime_list = []

#       for num in range(2, n + 1):
#          if is_prime(num):
#             prime_list.append(num)

#       return prime_list

#    input_num = input()
#    n = int(input_num)

#    result = get_prime_numbers(n)
#    print(result)
# except ValueError:
#    print('error')

# #8
# try:
#    def is_prime(num):
#       if num <= 1:
#          return False
#       if num <= 3:
#          return True
#       if num % 2 == 0 or num % 3 == 0:
#          return False
#       i = 5
#       while i * i <= num:
#          if num % i == 0 or num % (i + 2) == 0:
#             return False
#          i += 6
#       return True

#    def get_prime_numbers_in_list(list):
#       return [num for num in list if is_prime(num)]

#    input_list = input("Введите список чисел через запятую: ")
#    list = [int(num) for num in input_list.split(',')]

#    result = get_prime_numbers_in_list(list)
#    print(result)

# except ValueError:
#    print('error')

# #9
# try:
#    from datetime import datetime

#    def get_difference_between_dates(date1, date2):
#       date1_obj = datetime.strptime(date1, "%Y.%m.%d")
#       date2_obj = datetime.strptime(date2, "%Y.%m.%d")

#       date_diff = abs((date2_obj - date1_obj).days)

#       return date_diff

#    date1 = input()
#    date2 = input()

#    result = get_difference_between_dates(date1, date2)
#    print(result)

# except ValueError:
#    print('error')

#Task 3
#10
# try:
#    def is_perfect_number(num):
#       if num <= 1:
#          return False

#       divisors_sum = 1
#       for i in range(2, int(num ** 0.5) + 1):
#          if num % i == 0:
#             divisors_sum += i
#             if i != num // i:
#                divisors_sum += num // i

#       return divisors_sum == num


#    def get_perfect_numbers(numbers):
#       perfect_numbers = []
#       for num in numbers:
#          if is_perfect_number(num):
#             perfect_numbers.append(num)
#       return perfect_numbers

#    numbers = [6, 28, 12, 496, 8, 15]
#    perfect_nums = get_perfect_numbers(numbers)
#    print(perfect_nums)
# except KeyError:
#    print("error")

# #11
# try:
#    def is_perfect_square(num):
#       return int(num**0.5) ** 2 == num

#    def is_expression_true(expression):
#       list = [int(num) for num in expression.split(',')]
#       return all(is_perfect_square(num) for num in list)

#    input_nums = input()

#    result = is_expression_true(input_nums)
#    print(result)

# except ValueError:
#    print('error')

# #12
# try:
#    def display_shopping_list(shopping_list, sort_by_price=False):
#       if sort_by_price:
#          shopping_list = sorted(shopping_list, key=lambda x: x["price"])
#       return shopping_list

#    shopping_list = []

#    while True:
#       input_name = input("Name of product (type 'no'to end the task): ")
#       if input_name.lower() == 'no':
#          break
#       try:
#          input_price = float(input("Price: "))
#       except ValueError:
#          print("Enter the num")
#          continue

#       shopping_list.append({"name": input_name, "price": input_price})

#       add_more = input("Wanna add another one? (yes/no): ")
#       if add_more.lower() != 'yes':
#          break

#    result = display_shopping_list(shopping_list)
#    print(result)
# except ValueError:
#    print('error')

# #13
# try:
#    def get_words_starting_with_vowel(words):
#       vowel_words = [word for word in words if word[0].lower() in ['a', 'e', 'i', 'o', 'u']]
#       return vowel_words

#    input_words = input("Words separated by comma: ")
#    words_list = input_words.split(',')

#    result = get_words_starting_with_vowel(words_list)
#    print(result)
# except ValueError:
#    print('error')