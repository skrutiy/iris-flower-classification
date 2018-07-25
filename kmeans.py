''' This is the class for a kmeans object '''

import csv
import random

class KMeans(object):
    ''' Kmeans object class '''
    def __init__(self):
        ''' instantiates the members of the class '''
        self.clus1 = []
        self.clus2 = []
        self.clus3 = []

    if __name__ == "__main__":
        file = open('data/iris.data')
        lines = file.readlines()
        file.close()

        random.shuffle(lines)

        file = open('data/mixediris.data')
        file.writelines(lines)
        file.close()

        csvfile1 = open('data/mixediris.data')
        csvreader = csv.reader(csvfile1, delimiter=',')
        centroid1 = [0,0,0,0,"unknown"]
        centroid2 = [0,0,0,0,"unknown"]
        centroid3 = [0,0,0,0,"unknown"]
        sum1 = 0
        sum2 = 0
        sum3 = 0
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
                dist1 = (centroid1[0]-row[0])**2 + (centroid1[1]-row[1])**2 + (centroid1[2]-row[2])**2 + (centroid1[3]-row[3])**2
                dist2 = (centroid2[0]-row[0])**2 + (centroid2[1]-row[1])**2 + (centroid2[2]-row[2])**2 + (centroid2[3]-row[3])**2
                dist3 = (centroid3[0]-row[0])**2 + (centroid3[1]-row[1])**2 + (centroid3[2]-row[2])**2 + (centroid3[3]-row[3])**2
                distances = [dist1, dist2, dist3]
                minimum = min(distances)
                if minimum == dist1:
                    self.clus1.append(row)
                elif minimum == dist2:
                    self.clus2.append(row)
                else:
                    self.clus3.append(row)

        centroids = update_centroids()

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


