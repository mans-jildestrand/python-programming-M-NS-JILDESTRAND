import math

# Training data
# Format: (width, height, label)
training_data = [
    (25, 32, "Pikachu"),
    (24.2, 31.5, "Pikachu"),
    (22, 34, "Pikachu"),
    (20.5, 34, "Pichu")
]

def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def classify(point):
    """Classify a point by finding the nearest neighbor"""
    closest = None
    min_dist = float("inf")

    for data_point in training_data:
        d = distance(point, (data_point[0], data_point[1]))
        if d < min_dist:
            min_dist = d
            closest = data_point

    return closest[2]

# Test with given points (compare with expected results)
print("=== Testing given points ===")
test_points = [
    (25, 32, "Pikachu"),
    (24.2, 31.5, "Pikachu"),
    (22, 34, "Pikachu"),
    (20.5, 34, "Pichu")
]

for tp in test_points:
    predicted = classify((tp[0], tp[1]))
    print(f"Point ({tp[0]}, {tp[1]}) -> Predicted: {predicted}, Expected: {tp[2]}")

print("\n=== Classify your own points ===")
while True:
    try:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if width <= 0 or height <= 0:
            print("Error: width and height must be positive numbers.\n")
            continue

        result = classify((width, height))
        print(f"Point ({width}, {height}) is classified as {result}\n")

    except ValueError:
        print("Error: please enter numeric values.\n")