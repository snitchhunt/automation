import random
from faker import Factory
from random import randint

fake = Factory.create('en_AU')

class MobilePerson:
    def __init__(self, email_address=None):
        self.called_numbers = []
        # We store all locations this person ever been
        self.locations = []
        if email_address:
            self.email_address = email_address
        else:
            self.email_address = fake.email()
        self.IMEI = self.getImei(14)
        self.phone_number = fake.phone_number()
        self.address = fake.address().replace('\n', ' ')
        self.name = fake.name()
        # Add phone numbers this user ever called
        for i in range(randint(1, 200)):
            phone_number = fake.phone_number()
            self.called_numbers.append(phone_number)
        # Locations this person has ever been
        for i in range(randint(20, 200)):
            location = fake.street_name()
            self.locations.append(location)

    def luhn_residue(self, digits):
        """ Lunh10 residue value """
        s = sum(d if (n % 2 == 1) else (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)[d]
                for n, d in enumerate(map(int, reversed(digits))))
        return (10 - s % 10) % 10

    def getImei(self, N):
        part = ''.join(str(random.randrange(0,9)) for _ in range(N-1))
        res = self.luhn_residue('{}{}'.format(part, 0))
        return '{}{}'.format(part, -res%10)

    def generate_lines(self):
        lines = []
        # Generate dial logs this person ever contacted
        for called_number in self.called_numbers:
            # Generate a random amount of calls for each dialled person
            for i in range(randint(1, 30)):
                    date = fake.date_time_between(start_date="-2y", end_date="now", tzinfo=None)
                    line = [
                        self.IMEI,
                        self.phone_number,
                        random.choice(self.called_numbers),
                        random.choice(self.locations),
                        '{:%d/%m/%Y %H:%M:%S}'.format(date),
                        randint(5, 3600)
                    ]
                    lines.append(line)
        return lines

    def get_subscriber_data(self):
        date = fake.date_time_between(start_date="-5y", end_date="-2y", tzinfo=None)
        line = [
            self.IMEI,
            self.phone_number,
            self.name,
            self.address,
            self.email_address,
            date
        ]
        return line
