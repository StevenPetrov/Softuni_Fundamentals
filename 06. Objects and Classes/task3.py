class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_info = []
while True:
    command = input()
    if command == 'Stop':
        break
    else:
        emails_info.append(command)

send_info = list(map(int, input().split(', ')))

for x in emails_info:
    if emails_info.index(x) in send_info:
        x = x.split()
        email = Email(x[0], x[1], x[2])
        email.send()
        print(email.get_info())
    else:
        x = x.split()
        email = Email(x[0], x[1], x[2])
        print(email.get_info())
