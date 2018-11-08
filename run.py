''' This is a script to run the classifier '''

from knn import KNN
from knn import accuracy

print("Iris flower predictions based on KNN:")

model = KNN('./data/iris.data')
predictions = model.run_classifier('./data/bezdekIris.data')
print("Predictions for test data set:", predictions)
accuracy = accuracy(predictions, './data/bezdekIris.data')
print("model accuracy:", accuracy)
