import os
import random
from bs4 import BeautifulSoup


# Seed (3, 81.22)
def load_dataset():
    random.seed(3)
    print('Loading sarcastic data set')
    reviews = []
    directory = os.fsencode('sarcastic')
    for file in os.listdir(directory):
        if os.fsdecode(file).endswith('.txt'):
            details = {}
            soup = BeautifulSoup(open('sarcastic/' + os.fsdecode(file), "r").read().replace('\n', ''), 'lxml')
            details['title'] = soup.find('title').text
            details['review'] = soup.find('review').text
            details['rating'] = float(soup.find('stars').text)

            reviews.append(details)
        else:
            continue
    random.shuffle(reviews)
    sarcastic_training = reviews[:300]
    sarcastic_testing = reviews[300:400]
    details = {}
    details['title'] = "Sample test review"
    details['review'] = "So nice book that I won't even consider leaving it for one moment! The writer must have taken his whole life to write this book. JK Rollings should take lessons from this writer!!!"
    details['rating'] = 5.0
    sarcastic_testing[0] = details
	
    print('Length of training set : {}\nLength of testing set : {}\n'.format(len(sarcastic_training),
                                                                             len(sarcastic_testing)))

    print('Loading regular data set')
    reviews = []
    directory = os.fsencode('regular')
    for file in os.listdir(directory):
        if os.fsdecode(file).endswith('.txt'):
            details = {}
            soup = BeautifulSoup(open('regular/' + os.fsdecode(file), "r").read().replace('\n', ''), 'lxml')
            details['title'] = soup.find('title').text
            details['review'] = soup.find('review').text
            details['rating'] = float(soup.find('stars').text)

            reviews.append(details)
        else:
            continue
    random.shuffle(reviews)

    regular_training = reviews[:300]
    regular_testing = reviews[300:400]
    print('Length of training set : {}\nLength of testing set : {}\n'.format(len(regular_training),
                                                                             len(regular_testing)))
    return sarcastic_training, sarcastic_testing, regular_training, regular_testing
