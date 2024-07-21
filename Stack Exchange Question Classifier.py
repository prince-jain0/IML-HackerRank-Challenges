import json
import sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

if sys.version_info[0] >= 3: 
    raw_input = input

transformer = HashingVectorizer(stop_words='english')

_train = []
train_label = []

with open('training.json') as f:
    num_train_samples = int(f.readline())
    for _ in range(num_train_samples):
        data = json.loads(f.readline())
        _train.append(data['question'] + "\r\n" + data['excerpt'])
        train_label.append(data['topic'])

train = transformer.fit_transform(_train)

svm = LinearSVC()
svm.fit(train, train_label)

_test = []
num_test_samples = int(raw_input("Enter the number of test samples: "))

for _ in range(num_test_samples):
    data = json.loads(raw_input())
    _test.append(data['question'] + "\r\n" + data['excerpt'])

test = transformer.transform(_test)

test_label = svm.predict(test)
for label in test_label:
    print(label)
