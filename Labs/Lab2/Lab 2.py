import math

# Some training examples
# format is (width, height, label)
training_data = [
    (25, 32, "Pikachu"),
    (24.2, 31.5, "Pikachu"),
    (22, 34, "Pikachu"),
    (20.5, 34, "Pichu")
]

def distance(p1, p2):
    # euclidean distance formula
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def classify(point):
    # nearest neighbour classification
    closest = None
    min_dist = float("inf")

    for data_point in training_data:
        d = distance(point, (data_point[0], data_point[1]))
        if d < min_dist:
            min_dist = d
            closest = data_point

    return closest[2]

# quick test with the training data
print("=== Testing ===")
test_points = [
    (25, 32, "Pikachu"),
    (24.2, 31.5, "Pikachu"),
    (22, 34, "Pikachu"),
    (20.5, 34, "Pichu")
]

for tp in test_points:
    predicted = classify((tp[0], tp[1]))
    print(f"Point {tp[0]}, {tp[1]} -> Predicted: {predicted}, Expected: {tp[2]}")

# user can try their own
print("\n=== Try it yourself ===")
while True:
    try:
        width = input("Enter width (or q to quit): ")
        if width.lower() == "q":
            break
        height = input("Enter height (or q to quit): ")
        if height.lower() == "q":
            break

        width = float(width)
        height = float(height)

        if width <= 0 or height <= 0:
            print("Width and height must be positive!\n")
            continue

        result = classify((width, height))
        print(f"({width}, {height}) classified as {result}\n")

    except:
        # user typed something weird
        print("Invalid input, try again.\n")
