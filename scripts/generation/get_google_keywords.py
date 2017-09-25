import requests
import time
import sys

class Keywords:
    def __init__(self, filename="query.dat"):
        self.f = open(filename, 'a')

    def stop(self):
        self.f.close()

    def get_data(self):
        url = 'https://www.google.com/trends/hottrends/visualize/internal/data'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            q = data.get('united_kingdom') + data.get('south_africa') + data.get('united_states') + data.get('australia') + data.get('canada')
        else:
            q = []
        return set(q)

    def write_keywords_to_file(self, data):
        print(data)
        for item in data:
            line = item + "\n"
            self.f.write(line)

if __name__ == '__main__':
    k = Keywords()
    print('Press Ctrl+C to interrupt.')
    while True:
        try:
            print("Getting keywords... ", end="")
            data = k.get_data()
            k.write_keywords_to_file(data)
            print(" got {}, sleeping ...".format(len(data)))
            time.sleep(120)
        except KeyboardInterrupt:
            k.stop()
            print("Bye")
            sys.exit()
