email = input()
command = input()

while command != 'Complete':
    if command == 'Make Upper':
        email = email.upper()
        print(email)
    elif command == "Make Lower":
        email = email.lower()
        print(email)
    elif "GetDomain" in command:
        command = command.split()
        count = int(command[1])
        last_word = ""
        for index in range(len(email)-count, len(email)):
            last_word += email[index]
        print(last_word)
    elif command == "GetUsername":
        username = ''
        if "@" in email:
            for letter in email:
                if letter != "@":
                    username += letter
                else:
                    break
            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif "Replace" in command:
        command = command.split()
        new_mail = ''
        for letter in email:
            if letter == command[1]:
                new_mail += "-"
            else:
                new_mail += letter
        print(new_mail)
    elif command == "Encrypt":
        encrypted_email = ""
        for index in range(len(email)):
            encrypted_email += str(ord(email[index]))
            if index < len(email) - 1:
                encrypted_email += " "
        print(encrypted_email)
    command = input()

