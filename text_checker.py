from subprocess import Popen, PIPE
import requests


class TextChecker(object):

    """This class takes a URL and the path to the RomanConvertor program
     and determines the location of Roman numerals by line and word."""
    def __init__(self, online_text_url, path_to_RomanConvertor):
        super(TextChecker, self).__init__()
        self.online_text_url = online_text_url
        self.text_to_check = ""
        self.roman_numeral_locations = {}
        self.get_online_text()

    def get_online_text(self):
        r = requests.get(self.online_text_url)
        if r.status_code != 200:
            raise Exception(
                "Received unexpected status code {}".format(r.status_code)
            )
        if 'text/plain' not in r.headers['content-type']:
            raise Exception(
                "Provided URL {} is not a plain text document".format(
                    self.online_text_url
                )
            )
        self.text_to_check = r.text

    def get_locations_of_roman_numerals(self):
        pipe = Popen(['./RomanConvertor'], stdin=PIPE, stdout=PIPE)
        for line_index, line in enumerate(self.text_to_check.splitlines()):
            for word_index, word in enumerate(line.split()):
                try:
                    if word in ['special', 'stop']:
                        continue
                    pipe.stdin.write(word + "\n")
                    output = pipe.stdout.readline().rstrip()
                    if output != '0':
                        if output not in self.roman_numeral_locations.keys():
                            self.roman_numeral_locations[output] = [
                                "Line {}, word {}".format(
                                    line_index+1, word_index+1
                                )
                            ]
                        else:
                            self.roman_numeral_locations[output].append(
                                "Line {}, word {}".format(
                                    line_index+1, word_index+1
                                )
                            )
                except UnicodeEncodeError:
                    continue
        pipe.terminate()
        return self.roman_numeral_locations


if __name__ == "__main__":
    online_text_url = "http://www.gutenberg.org/files/54610/54610-0.txt"
    path_to_RomanConvertor = "./RomanConvertor"
    text_checker = TextChecker(online_text_url, path_to_RomanConvertor)
    roman_numeral_locations = text_checker.get_locations_of_roman_numerals()
