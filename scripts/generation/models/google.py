import random
import csv
import uuid
from random import randint
from faker import Factory
from datetime import datetime, timedelta
from random_words import RandomWords

google_search_queries = open("data/query_keywords.txt", 'r').read().splitlines()

class SearchQueries:
    def __init__(self):
        self.data = []
        self.ip_addresses = []
        user_agents = []
        fake = Factory.create('en_AU')
        rw = RandomWords()
        for i in range(randint(1, 15)):
            ip_address = fake.ipv4(network=False)
            self.ip_addresses.append(ip_address)
        for i in range(randint(2,8)):
            user_agents.append(fake.user_agent())
        # Generate fake query history
        for i in range(randint(1, 500)):
            # Use real Google Trends keywords in 20% of cases
            if randint(1, 100) < 20:
                q = random.choice(google_search_queries)
            else:
                q = ' '.join(rw.random_words(count=randint(1,4)))
            search_query = {
                # Choose a random IP address
                'ip_address': random.choice(self.ip_addresses),
                # Select random date
                'date': fake.date_time_between(start_date="-2y", end_date="now", tzinfo=None),
                # Generate random keywords
                'search_query': q,
                'user_agent': random.choice(user_agents),
            }
            self.data.append(search_query)

    def get_ip_addresses(self):
        return self.ip_addresses

class GoogleUser:
    def __init__(self, output="google_query_log.csv"):
        self.output = output
        fake = Factory.create('en_AU')
        # Is this an anonim user (i.e. is the user logged into Google)?
        self.anonymous = random.choice([True, False])
        self.profile = {}
        self.profile['id'] = str(uuid.uuid4())
        if not self.anonymous:
            profile = fake.profile(fields=None)
            self.profile['username'] = profile.get('username')
            self.profile['email'] = profile.get('username') + '@gmail.com'
            if randint(1, 100) < 80:
                self.profile['name'] = profile.get('name')
                if randint(1, 100) < 20:
                    self.profile['job'] = profile.get('job')
                    self.profile['company'] = profile.get('company')
                if randint(1, 100) < 30:
                    self.profile['address'] = profile.get('residence')
        self.search_queries = SearchQueries()

    @property
    def ip_addresses(self):
        ip_addresses = self.search_queries.get_ip_addresses()
        return ip_addresses

    def generate_lines(self):
        lines = []
        for q in self.search_queries.data:
            address = self.profile.get('address')
            if self.profile.get('address'):
                address = address.replace('\n', ' ')
            line = [
                self.profile.get('id'),
                self.profile.get('name'),
                self.profile.get('username'),
                self.profile.get('email'),
                address,
                self.profile.get('job'),
                self.profile.get('company'),
                q.get('search_query'),
                q.get('ip_address'),
                randint(1024, 65535),
                #q.get('date'),
                '{:%d/%m/%Y %H:%M:%S}'.format((q.get('date'))),
                q.get('user_agent')
            ]
            lines.append(line)
        return lines
