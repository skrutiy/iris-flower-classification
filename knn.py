''' This is the class for a knn object '''

import csv
from collections import Counter
import numpy as np

class KNN(object):
    ''' KNN object class '''
    def __init__(self, filepath, k=5):
        ''' instantiates the members of the class '''
        self.k = k
        self.filepath = filepath

    def run_classifier(self, test_data_path):
        ''' runs the classifier, returns predictions '''
        file_train = open(self.filepath)
        csvreader_training = csv.reader(file_train, delimiter=',')
        measurements_train = np.genfromtxt(self.filepath, delimiter=',')
        labels_train = []
        for row in csvreader_training:
            if len(row) != 0:
                labels_train.append(row[4])

        measurements_test = np.genfromtxt(test_data_path, delimiter=',')

        predictions = []

        for row in measurements_test:
            distances = np.full((self.k,), 1000000000000000000000000000000000)
            index = np.full((self.k,), -1)
            for k in range(self.k):
                for i in range(measurements_train.shape[0]):
                    distance = 0
                    if i not in index:
                        for n in range(measurements_train.shape[1]-1):
                            distance += (measurements_train[i][n] - row[n])**2
                        if not all(j <= distance for j in distances):
                            remove_i = np.argmax(distances)
                            index[remove_i] = i
                            distances[remove_i] = distance
            labels = []
            for i in index:
                labels.append(labels_train[i])
            count = Counter()
            for label in labels:
                count[label] += 1
            pred = count.most_common(1)[0][0]
            predictions.append(pred)

        return predictions


def accuracy(predictions, test_data_path):
    ''' method to get the accuracy of the model, returns a float '''
    file_test = open(test_data_path)
    csvreader_testing = csv.reader(file_test, delimiter=',')
    labels_test = []
    for row in csvreader_testing:
        if len(row) != 0:
            labels_test.append(row[4])

    correct = 0
    for i, value in enumerate(predictions):
        if value == labels_test[i]:
            correct += 1

    accur = correct/len(predictions)
    return accur
