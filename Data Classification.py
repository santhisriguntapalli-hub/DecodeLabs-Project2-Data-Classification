# Dataset
dataset = [
    [2, "Fail"],
    [3, "Fail"],
    [4, "Pass"],
    [5, "Pass"],
    [6, "Pass"],
    [1, "Fail"],
    [7, "Pass"],
    [2, "Fail"]
]

# Split dataset
train = dataset[:6]
test = dataset[6:]

correct = 0

print("Testing Model\n")

for sample in test:
    hours = sample[0]
    actual = sample[1]

    # Classification rule
    if hours >= 4:
        prediction = "Pass"
    else:
        prediction = "Fail"

    print("Hours:", hours)
    print("Actual:", actual)
    print("Prediction:", prediction)
    print()

    if prediction == actual:
        correct += 1

accuracy = (correct / len(test)) * 100

print("Accuracy =", accuracy, "%")