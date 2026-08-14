students = {
    "student1": {
        "name": "Ali",
        "age": 20,
        "program": "Data Science"
    },
    "student2": {
        "name": "Ahmad",
        "age": 21,
        "program": "Machine Learning"
    },
    "student3": {
        "name": "Abdullah",
        "age": 20,
        "program": "Data Science"
    }
}
for key, value in students.items() :
    print(f"{key}: {value['name']} - {value['program']}")

for key, value in students.items() :
    if value["program"] == "Data Science" :
        print(f"{value['name']} : {value['program']}")

for key, value in students.items() :
    if value["age"] == 20 :
        print(value["name"])

total = 0
count = 0
for key, value in students.items() :
    if value["program"] == "Data Science" :
        total += value["age"]
        count += 1
average_age = total/count
print(average_age)

oldest_st = None
highest_age = 0
for key, value in students.items() :
    if value["age"] > highest_age :
        highest_age = value["age"]
        oldest_st = value["name"]
print(oldest_st, highest_age)


students = {
    "student1": {
        "name": "Ali",
        "subjects": {
            "Python": 85,
            "Statistics": 78,
            "Machine Learning": 90
        }
    },
    "student2": {
        "name": "Ahmad",
        "subjects": {
            "Python": 72,
            "Statistics": 81,
            "Machine Learning": 75
        }
    }
}
for key, value in students.items() :
    print(value["name"])
    for subj_name, marks in value["subjects"].items() :
        print(subj_name, marks)

for key, value in students.items() :
    for subj_name, marks in value["subjects"].items() :
        if marks >= 80 :
            print(subj_name, marks)


data = {
    "detections": [
        {
            "image": "apple.jpg",
            "class": "apple",
            "confidence": 0.96
        },
        {
            "image": "banana.jpg",
            "class": "banana",
            "confidence": 0.91
        },
        {
            "image": "orange.jpg",
            "class": "orange",
            "confidence": 0.98
        },
        {
            "image": "potato.jpg",
            "class": "potato",
            "confidence": 0.87
        }
    ]
}
print("All Detections:")

for detection in data["detections"]:
    print(f"{detection['image']} → {detection['class']}")

print("\nHigh Confidence Detections:")

for detection in data["detections"]:
    if detection["confidence"] >= 0.90:
        print(
            f"{detection['image']} → "
            f"{detection['class']} → "
            f"{detection['confidence']}")