#                                         𝕷𝖔𝖔𝖕𝖘🙌🙌
# for loop
for i in range(10):
    print(i)
#range(10) ->0-9
for i in range (0,9):
    print(i)
#range(0,9) -> 0-8
    
color = ("blue" , "green", "red", "black")
for i in color:
    print(i)

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for i in log_file:
    if "ERROR" in i:
        print(i)


#while loop
count = 0
while count<10:
    print(count)
    count= count+1

# break Statement
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

# continue Statement
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)


