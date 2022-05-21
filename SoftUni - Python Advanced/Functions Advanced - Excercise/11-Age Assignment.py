def age_assignment(*args, **kwargs):
    dic = {}
    for arg in args:
        for name, age in kwargs.items():
            if arg[0] == name:
                dic[arg] = age

    return dic


print(age_assignment("Peter", "George", G=26, P=19))

