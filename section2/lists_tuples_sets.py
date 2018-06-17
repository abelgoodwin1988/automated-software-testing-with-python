my_variable = "hello"

grades = [
    77, 80, 90, 95, 100
]
typle_grades = (
    77, 80, 90, 95, 100
)
set_grades = {
    77, 80, 90, 100, 100
}

print(sum(grades) / len(grades))
grades.append(108)
print(sum(grades) / len(grades))
print(set_grades)


your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

print(your_lottery_numbers.union(winning_numbers))

single_typle = ('value',)
print(len(single_typle))

q = tuple(100)

print (q)