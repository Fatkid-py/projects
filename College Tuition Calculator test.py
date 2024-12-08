# College Tuition Calculator

# Total number of credits needed to graduate 
credit_hours_total = 125

# Sets cost per credit hour at $ per credit hour.
cost_per_hour = input("Enter Cost per Credit Hour: $") 
cost_per_hour = int(cost_per_hour)
print(cost_per_hour)

# Years of attendance
years = ['2025', '2026', '2027', '2028']


# Creates lsit of all semesters.
semesters = [['Spring', 15, 2025], ['Summer', 0, 2025], ['Fall', 16, 2025],
             ['Spring', 15, 2026], ['Summer', 12, 2026], ['Fall', 15, 2026],
             ['Spring', 15, 2027], ['Summer', 0, 2027], ['Fall', 9, 2027],
             ['Spring', 6, 2028], ['Summer', 0, 2028], ['Fall', 0, 2028],
             ['Fall', 15, 2024]]

# Sets the index locations of "Spring" by year in the semesters list
spring25_semester = semesters[0] 
spring26_semester = semesters[3]
spring27_semester = semesters[6]
spring28_semester = semesters[9]

# Sets the index locations of "Fall" by year in the semesters list
fall24_semester = semesters[-1]
#print(fall24_semester)
fall25_semester = semesters[2]
fall26_semester = semesters[5]
fall27_semester = semesters[8]
fall28_semester = semesters[11]

# Sets the index locations of "Summer" by year in the semesters list
summer25_semester = semesters[1]
summer26_semester = semesters[4]
summer27_semester = semesters[7]
summer28_semester = semesters[10]

# Sets the index location of Spring credit hours integer by year in the semesters list
spring25_credits = semesters[0][1]
spring26_credits = semesters[3][1]
spring27_credits = semesters[6][1]
spring28_credits = semesters[9][1]

# Sets the index location of Fall credit hours integer in the semesters list
fall24_credits = semesters[-1][1]
fall25_credits = semesters[2][1]
fall26_credits = semesters[5][1]
fall27_credits = semesters[8][1]
fall28_credits = semesters[11][1]

# Sets the index location of Summer credit hours integer in the semesters list
summer25_credits = semesters[1][1]
summer26_credits = semesters[4][1]
summer27_credits = semesters[7][1]
summer28_credits = semesters[10][1]

# Self explanitory... | Cost for Fall 2024 semester.
cost_per_semester_fall24 = cost_per_hour * int(fall24_credits)
print('\nFall 2024: ')
print('$' + str(cost_per_semester_fall24))
print('\n')

# Self explanitory... | Cost for Spring 2025 semester.
cost_per_semester_spring25 = cost_per_hour * spring25_credits
print('\nSpring 2025: ')
print('$' + str(cost_per_semester_spring25))
print('\n')

# Self explanitory... | Cost for Spring 2026 semester.
cost_per_semester_spring26 = cost_per_hour * spring26_credits
print('\nSpring 2026: ')
print('$' + str(cost_per_semester_spring26))
print('\n')

# Self explanitory... | Cost for Spring 2027 semester.
cost_per_semester_spring27 = cost_per_hour * spring27_credits
print('\nSpring 2027: ')
print('$' + str(cost_per_semester_spring27))
print('\n')

# Self explanitory... | Cost for Spring 2028 semester.
cost_per_semester_spring28 = cost_per_hour * spring28_credits
print('\nSpring 2028: ')
print('$' + str(cost_per_semester_spring28))
print('\n')

# Self explanitory... | Cost for Fall 2025 semester.
cost_per_semester_fall25 = cost_per_hour * fall25_credits
print('\nFall 2025: ')
#Need to remember how to transform an int to str 
print('$' + str(cost_per_semester_fall25))
print('\n')

# Self explanitory... | Cost for Fall 2026 semester.
cost_per_semester_fall26 = cost_per_hour * fall26_credits
print('\nFall 2026: ')
#Need to remember how to transform an int to str 
print('$' + str(cost_per_semester_fall26))
print('\n')

# Self explanitory... | Cost for Fall 2027 semester.
cost_per_semester_fall27 = cost_per_hour * fall27_credits
print('\nFall 2027: ')
#Need to remember how to transform an int to str 
print('$' + str(cost_per_semester_fall27))
print('\n')

# Self explanitory... | Cost for Summer 2025 semester.
cost_per_semester_summer25 = cost_per_hour * summer25_credits
print('Summer 2025:')
if summer25_credits == 0.0:print('Summer Break!! YAY!')
else:print('$' + str(cost_per_semester_summer25))
print('\n')


# Self explanitory... | Cost for Summer 2026 semester.
cost_per_semester_summer26 = cost_per_hour * summer26_credits
print('Summer 2026:')
if summer26_credits == 0.0:print('Summer Break!! YAY!')
else:print('$' + str(cost_per_semester_summer26))
print('\n')

# Self explanitory... | Cost for Summer 2027 semester.
cost_per_semester_summer27 = cost_per_hour * summer27_credits
print('Summer 2027:')
if summer27_credits == 0.0:print('Summer Break!! YAY!')                                                                    
else:print('$' + str(cost_per_semester_summer27))
print('\n')

# Self explanitory... | Cost for Summer 2028 semester.
cost_per_semester_summer28 = cost_per_hour * summer28_credits
print('Summer 2028:')
if summer28_credits == 0.0:print('Summer Break!! YAY!')
else:print('$' + str(cost_per_semester_summer28))
print('\n')

# What the f**k am I doing right now, this is torture. One thousandth of the way there.
year1_cost = cost_per_semester_fall24 + cost_per_semester_summer25 + cost_per_semester_spring25
year2_cost = cost_per_semester_fall25 + cost_per_semester_summer26 + cost_per_semester_spring26                                               
year3_cost = cost_per_semester_fall26 + cost_per_semester_summer27 + cost_per_semester_spring27
year4_cost = cost_per_semester_fall27 + cost_per_semester_summer28 + cost_per_semester_spring28
total_cost = year1_cost + year2_cost + year3_cost +year4_cost

print('Your total balance for your Freshman year is approximately:'), print('$' + str(year1_cost))
print("\n")
print('Your total balance for your Sophomore year is approximately:'), print('$' + str(year2_cost))
print("\n")
print('Your total balance for your Junior year is approximately:'), print('$' + str(year3_cost))
print("\n")
print('Your total balance for your Senior year is approximately:'), print('$' + str(year4_cost))
print('\n')
print('Your total balance is approximately:'), print('$' + str(total_cost))