class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

        def send():
            self.is_sent = True

        def get_info():
            print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


command = input().split()
while command != 'Stop':
    Email.__init__(sender=command[0], receiver=command[1], content=command[2])
    Email.send()
    Email.get_info()