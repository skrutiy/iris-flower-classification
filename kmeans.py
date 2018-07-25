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
        self.centroid1 = [0,0,0,0,"unknown"]
        self.centroid2 = [0,0,0,0,"unknown"]
        self.centroid3 = [0,0,0,0,"unknown"]

    if __name__ == "__main__":
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
            if count==0:
                self.clus1.append(row)
                centroid1[0] = row[0]
                centroid1[1] = row[1]
                centroid1[2] = row[2]
                centroid1[3] = row[3]
                centroid1[4] = row[4]
            elif count==1:
                self.clus2.append(row)
                centroid2[0] = row[0]
                centroid2[1] = row[1]
                centroid2[2] = row[2]
                centroid2[3] = row[3]
                centroid2[4] = row[4]
            elif count==2:
                self.clus3.append(row)
                centroid3[0] = row[0]
                centroid3[1] = row[1]
                centroid3[2] = row[2]
                centroid3[3] = row[3]
                centroid3[4] = row[4]
            else:
                break
            count += 1

            iterate = True

            while iterate:

                csvreader = get_data()

                calculate_clusters(csvreader)

                old_centroid1 = self.centroid1.copy()
                old_centroid2 = self.centroid2.copy()
                old_centroid3 = self.centroid3.copy()

                centroids = update_centroids()

                if (old_centroid1 == centroids[0]) && (old_centroid2 == centroids[1]) && (old_centroid3 == centroids[2]):
                    iterate = False
                else:
                    self.centroid1 = centroids[0].copy()
                    self.centroid2 = centroids[1].copy()
                    self.centroid3 = centroids[2].copy()


    def get_data(self):
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
        for value in data:
            dist1 = (centroid1[0]-value[0])**2 + (centroid1[1]-value[1])**2 + (centroid1[2]-value[2])**2 + (centroid1[3]-value[3])**2
            dist2 = (centroid2[0]-value[0])**2 + (centroid2[1]-value[1])**2 + (centroid2[2]-value[2])**2 + (centroid2[3]-value[3])**2
            dist3 = (centroid3[0]-value[0])**2 + (centroid3[1]-value[1])**2 + (centroid3[2]-value[2])**2 + (centroid3[3]-value[3])**2
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
        1_sum = 0
        2_sum = 0
        3_sum = 0
        4_sum = 0
        for value in self.clus1:
            1_sum += value[0]
            2_sum += value[1]
            3_sum += value[2]
            4_sum += value[3]
        centroid1 = [1_sum/length, 2_sum/length, 3_sum/length, 4_sum/length, "unknown"]

        length = len(self.clus2)
        1_sum = 0
        2_sum = 0
        3_sum = 0
        4_sum = 0
        for value in self.clus2:
            1_sum += value[0]
            2_sum += value[1]
            3_sum += value[2]
            4_sum += value[3]
        centroid2 = [1_sum/length, 2_sum/length, 3_sum/length, 4_sum/length, "unknown"]

        length = len(self.clus3)
        1_sum = 0
        2_sum = 0
        3_sum = 0
        4_sum = 0
        for value in self.clus3:
            1_sum += value[0]
            2_sum += value[1]
            3_sum += value[2]
            4_sum += value[3]
        centroid3 = [1_sum/length, 2_sum/length, 3_sum/length, 4_sum/length, "unknown"]

        return [centroid1, centroid2, centroid3]


