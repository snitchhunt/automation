import csv
import os
from models.google import GoogleUser
from models.emailperson import EmailPerson
from models.mobileperson import MobilePerson
from random import randint

fname = {}
headers = {}

output_dir = "output/"
fname['google_query_log'] = output_dir + "google_query_log.csv"
fname['email_metadata_log'] = output_dir + "email_metadata_log.csv"
fname['phone_metadata_log']= output_dir + "phone_metadata_log.csv"
fname['phone_subscriber_info'] = output_dir + "phone_subscriber_info.csv"
fname['subject_lines'] = "data/subjects.txt"

headers['google_query_log'] = [
    "user_id",
    "full_name",
    "username",
    "email",
    "address",
    "job_title",
    "company_name",
    "search_query",
    "source_ip_address",
    "source_tcp_port",
    "date",
    "user_agent"
]

headers['email_metadata_log'] = [
    "source_ip_address",
    "source_tcp_port",
    "email_sender",
    "email_recipient",
    "email_subject",
    "date",
    "size"
]

headers['phone_subscriber_info'] = [
    "subscriber_imei",
    "subscriber_phone_number",
    "subscriber_name",
    "subscriber_address",
    "subscriber_email_address",
    "register_date"
]

headers['phone_metadata_log']  = [
    "subscriber_imei",
    "subscriber_phone_number",
    "dialled_number",
    "cell_tower_location",
    "date",
    "duration"
]

def open_csv_file(fname):
    f = open(fname, 'w')
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    return writer

def generate_logs(n, headers=False):
    writer = {}
    subject_lines = open(fname['subject_lines'], 'r').read().splitlines()
    # Open CSV files
    writer['google_query_log'] = open_csv_file(fname.get('google_query_log'))
    writer['email_metadata_log'] = open_csv_file(fname.get('email_metadata_log'))
    writer['phone_metadata_log'] = open_csv_file(fname.get('phone_metadata_log'))
    writer['phone_subscriber_info'] = open_csv_file(fname.get('phone_subscriber_info'))
    # Write headers if allowed
    if headers:
        writer['google_query_log'].writerow(headers.get('google_query_log'))
        writer['email_metadata_log'].writerow(headers.get('email_metadata_log'))
        writer['phone_metadata_log'].writerow(headers.get('phone_metadata_log'))
        writer['phone_subscriber_info'].writerow(headers.get('phone_subscriber_info'))
    # Writing user data
    for i in range(n):
        print("Generating user ({}/{}) ...".format(i + 1, n))
        # Generate Google user
        google_user = GoogleUser()
        # Generate emailer user
        # Link 20% of Google searches to the email logs
        if randint(1, 100) < 20:
            email_person = EmailPerson(google_user.ip_addresses)
        else:
            email_person = EmailPerson()
        # 10% that a person on the mobile subscriber list is on other metadata
        # logs as well
        if randint(1, 100) < 10:
            # TODO: Need to pass the email address here
            mobile_user = MobilePerson(email_person.get_email_address())
        else:
            mobile_user = MobilePerson()
        # Write Google query logs to file
        for line in google_user.generate_lines():
            writer['google_query_log'].writerow(line)
        # Write email logs to file
        for line in email_person.generate_lines(subject_lines):
            writer['email_metadata_log'].writerow(line)
        # Write phone call log metadata
        for line in mobile_user.generate_lines():
            writer['phone_metadata_log'].writerow(line)
        # Write subscriber info
        subscriber_info = mobile_user.get_subscriber_data()
        writer['phone_subscriber_info'].writerow(subscriber_info)

if __name__ == '__main__':
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    n = int(input('Users to generate: '))
    generate_logs(n)
    print("Done.")
