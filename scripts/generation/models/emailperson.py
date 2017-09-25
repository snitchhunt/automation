import random
from faker import Factory
from random import randint

fake = Factory.create('en_AU')

class EmailPerson:
    def __init__(self, ip_addresses=[]):
        # IP addresses this person ever used
        self.ip_addresses = ip_addresses
        # Recipients this person ever
        self.email_recipients = []
        # Generate email address of this person
        self.email_address = fake.user_name() + '@smalllake.com.au'
        # Add email addresses this user ever emailed
        for i in range(randint(10, 100)):
            recipient = fake.email()
            self.email_recipients.append(recipient)
        # Generate IP addresses this person every used
        # But only if we didn't receive IPs in ip_addresses
        if len(ip_addresses) == 0:
            for i in range(randint(1, 15)):
                ip_address = fake.ipv4(network=False)
                self.ip_addresses.append(ip_address)

    def get_email_address(self):
        return self.email_address

    def generate_email_size(self):
        """
        Most of the emails are small but some of them has attachments
        """
        # 10% of emails has attachments
        if randint(1, 100) < 10:
            size = randint(100000, 10000000)
        else:
            size = randint(1024, 10000)
        return size

    def generate_lines(self, subject_lines):
        lines = []
        # Generate email log for each recipient this person ever contacted
        for recipient in self.email_recipients:
            # Generate a random amount of email logs with the recipient
            for i in range(randint(1, 50)):
                date = fake.date_time_between(start_date="-2y", end_date="now", tzinfo=None)
                line = [
                    random.choice(self.ip_addresses),
                    randint(1024, 65535),
                    self.email_address,
                    random.choice(self.email_recipients),
                    random.choice(subject_lines),
                    '{:%d/%m/%Y %H:%M:%S}'.format(date),
                    self.generate_email_size()
                ]
                lines.append(line)
        return lines
