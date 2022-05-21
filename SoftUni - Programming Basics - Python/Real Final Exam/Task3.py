slojnost = int(input())
zavurtqnost = int(input())
stranici = int(input())
category = ''

if slojnost >= 80 and zavurtqnost >= 80 and stranici >= 8:
    category = "Legacy"
elif slojnost >= 80 and zavurtqnost <= 10:
    category = 'Master'
elif slojnost <= 10:
    category = "Elementary"
elif slojnost <= 30 and stranici <= 1:
    category = 'Easy'
elif zavurtqnost >= 50 and stranici >= 2:
    category = 'Hard'
else:
    category = "Regular"

print(category)
