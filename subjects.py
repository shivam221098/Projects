def classes():
    subjects = []
    no_of_subjects = int(input("Enter number of subjects: "))
    for i in range(no_of_subjects):
        subjects.append(input("Enter subjects #" + str(i + 1)))
    for subject in subjects:
        print(subject)


classes()
