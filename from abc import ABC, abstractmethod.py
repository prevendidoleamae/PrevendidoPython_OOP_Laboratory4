from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):

    def send(self, message):
        print(str.format("Sending Email: {0}", message))


class SMSNotification(Notification):

    def send(self, message):
        print(str.format("Sending SMS: {0}", message))

class AppNotification(Notification):

    def send(self, message):
        print(str.format("Sending App Notification: {0}", message))

email = EmailNotification()
sms = SMSNotification()
app = AppNotification()


email.send("Classes will resume tomorrow.")
sms.send("Please submit your assignments.")
app.send("School announcement: Exam schedule is available.")