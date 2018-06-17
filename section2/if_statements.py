known_friends = ['John', 'Anna', 'Mary']
people = input("Enter people you know.")

def who_do_you_know(people):
    people_list = people.split(',')
    known_people = list(set(people_list).intersection(set(known_friends)))
    return known_people

known_people = who_do_you_know(people)
known_people_string = ', & '.join(str(person) for person in known_people)
print("You Know {}!".format(known_people_string))
