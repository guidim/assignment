PK
     [UMQ��jW  W     main.py#Exercise1

my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
my_list.sort()
numbers = my_list[:2] + my_list[-2:]
suma = sum(numbers)
print(suma)

#Exercise2

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

user = input("Enter a name: ")
sc = names.index(user)
print(scores[sc])

#Exercise3

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]
scores.sort()
max_score = scores[-1:]
print(max_score)

students = scores.count(99)
print(students)

#Exercise4

month_days = list()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',  'October', 'November', 'December']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_days = [months, days]
print(months_days)

#Exercise5

winter = months_days[0][:3], months_days[1][:3]
spring = months_days[0][3:6], months_days[1][3:6]
summer = months_days[0][6:9], months_days[1][6:9]
autumn = months_days[0][9:12], months_days[1][9:12]
print(winter)
print(spring)
print(summer)
print(autumn)

#Exercise6

summer_days = sum(months_days[1][6:9])
print("Summer days last: ", summer_days, "days")

PK 
     [UMQ��jW  W                   main.pyPK      5   |    