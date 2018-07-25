''' This is the class for a kmeans object '''

import csv
import random

class KMeans(object):
    ''' Kmeans object class '''
    def __init__(self, filepath):
        ''' instantiates the members of the class '''
        self.clus1 = []
        self.clus2 = []
        self.clus3 = []
        self.centroid1 = [0, 0, 0, 0, "unknown"]
        self.centroid2 = [0, 0, 0, 0, "unknown"]
        self.centroid3 = [0, 0, 0, 0, "unknown"]
        self.filepath = filepath

    def run_classifier(self):
        ''' runs the classifier '''
        file = open(self.filepath)
        lines = file.readlines()
        file.close()

        random.shuffle(lines)

        file = open('data/mixeddata.data')
        file.writelines(lines)
        file.close()

        csvfile1 = open('data/mixeddata.data')
        csvreader = csv.reader(csvfile1, delimiter=',')

        count = 0
        for row in csvreader:
            if count == 0:
                self.clus1.append(row)
                self.centroid1[0] = row[0]
                self.centroid1[1] = row[1]
                self.centroid1[2] = row[2]
                self.centroid1[3] = row[3]
                self.centroid1[4] = row[4]
            elif count == 1:
                self.clus2.append(row)
                self.centroid2[0] = row[0]
                self.centroid2[1] = row[1]
                self.centroid2[2] = row[2]
                self.centroid2[3] = row[3]
                self.centroid2[4] = row[4]
            elif count == 2:
                self.clus3.append(row)
                self.centroid3[0] = row[0]
                self.centroid3[1] = row[1]
                self.centroid3[2] = row[2]
                self.centroid3[3] = row[3]
                self.centroid3[4] = row[4]
            else:
                break
            count += 1

            iterate = True

            while iterate:

                csvreader = self.get_data()

                self.calculate_clusters(csvreader)

                old_centroid1 = self.centroid1.copy()
                old_centroid2 = self.centroid2.copy()
                old_centroid3 = self.centroid3.copy()

                centroids = self.update_centroids()

                if (old_centroid1 == centroids[0]) and (old_centroid2 == centroids[1]) and (old_centroid3 == centroids[2]):
                    iterate = False
                else:
                    self.centroid1 = centroids[0].copy()
                    self.centroid2 = centroids[1].copy()
                    self.centroid3 = centroids[2].copy()

            # add here - what happens when classification is over

    def get_data(self):
        ''' shuffles the data and creates the csv reader for the file '''
        file = open(self.filepath)
        lines = file.readlines()
        file.close()

        random.shuffle(lines)

        file = open('data/mixeddata.data')
        file.writelines(lines)
        file.close()

        csvfile1 = open('data/mixeddata.data')
        csvreader = csv.reader(csvfile1, delimiter=',')

        return csvreader

    def calculate_clusters(self, data):
        ''' method to create the clusters '''
        for value in data:
            dist1 = (self.centroid1[0]-value[0])**2 + (self.centroid1[1]-value[1])**2 + (self.centroid1[2]-value[2])**2 + (self.centroid1[3]-value[3])**2
            dist2 = (self.centroid2[0]-value[0])**2 + (self.centroid2[1]-value[1])**2 + (self.centroid2[2]-value[2])**2 + (self.centroid2[3]-value[3])**2
            dist3 = (self.centroid3[0]-value[0])**2 + (self.centroid3[1]-value[1])**2 + (self.centroid3[2]-value[2])**2 + (self.centroid3[3]-value[3])**2
            distances = [dist1, dist2, dist3]
            minimum = min(distances)
            if minimum == dist1:
                self.clus1.append(value)
            elif minimum == dist2:
                self.clus2.append(value)
            else:
                self.clus3.append(value)

    def update_centroids(self):
        ''' method used to update the centroid values '''
        length = len(self.clus1)
        sums = [0, 0, 0, 0]

        for value in self.clus1:
            sums[0] = sums[0] + value[0]
            sums[1] = sums[1] + value[1]
            sums[2] = sums[2] + value[2]
            sums[3] = sums[3] + value[3]
        centroid1 = [sums[0]/length, sums[1]/length, sums[2]/length, sums[3]/length, "unknown"]

        length = len(self.clus2)
        sums = [0, 0, 0, 0]
        for value in self.clus2:
            sums[0] = sums[0] + value[0]
            sums[1] = sums[1] + value[1]
            sums[2] = sums[2] + value[2]
            sums[3] = sums[3] + value[3]
        centroid2 = [sums[0]/length, sums[1]/length, sums[2]/length, sums[3]/length, "unknown"]

        length = len(self.clus3)
        sums = [0, 0, 0, 0]
        for value in self.clus3:
            sums[0] = sums[0] + value[0]
            sums[1] = sums[1] + value[1]
            sums[2] = sums[2] + value[2]
            sums[3] = sums[3] + value[3]
        centroid3 = [sums[0]/length, sums[1]/length, sums[2]/length, sums[3]/length, "unknown"]

        return [centroid1, centroid2, centroid3]
