from knn import KNN

print("Iris flower predictions based on KNN:")

model = KNN('./data/iris.data')
predictions = model.run_classifier('./data/bezdekIris.data')
print("Predictions for test data set:", predictions)
accuracy = model.accuracy(predictions, './data/bezdekIris.data')
print("model accuracy:", accuracy)
