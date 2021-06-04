from django.core.mail import EmailMessage

import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class Util:
    @staticmethod #Python @staticmethod decorator is used to label a class method as a static method, which means that it can be called without instantiating the class first. It simply defines a normal function that is logically contained in the class for readability purposes. Here, we do not need to pass the class instance as the first argument via self, unlike other class functions.
    def send_email(data):
        
        email = EmailMessage(
            subject=data['email_subject'],
            body = data['email_body'],
            to = [data['to_email']]
        )
        EmailThread(email).start()