#5. Nested Dictionaries:
student = {
    "name": "Abdullah",
    "age": 20,
    "program": "Data Science",

    "academic": {
        "semester": "4th",
        "department": "CS",
        "university": "UOP"

    }
}
print(student)
print(student["academic"]["semester"])
print(student["academic"]["department"])
print(student["academic"]["university"])

for key, value in student.items():
    if key == "academic":
        break
    print(key, value)

for key, value in student["academic"].items():
    print(key, value)

students = {
    "student1": {
        "name": "Ali",
        "age": 20,
        "program": "Data Science"
    },
    "student2": {
        "name": "Ahmad",
        "age": 20,
        "program": "Data Science"
    },
    "student3": {
        "name": "Abdullah",
        "age": 20,
        "program": "Data Science"
    }
}
print(students)
print(students["student1"]["name"])
print(students["student2"]["program"])
students["student1"]["age"] = 21
students["student2"]["program"] = "Machine Learning"
students["student3"]["semester"] = "4th"
print(students)
removed_program = students["student2"].pop("program")
print(removed_program)
print(students["student2"].get("city", "Not Available"))


dataset = {
    "image_001": {
        "filename": "apple.jpg",
        "class": "apple",
        "confidence": 0.96
    },

    "image_002": {
        "filename": "banana.jpg",
        "class": "banana",
        "confidence": 0.91
    },

    "image_003": {
        "filename": "orange.jpg",
        "class": "orange",
        "confidence": 0.98
    }
}
print(dataset["image_001"])
print(dataset["image_002"]["confidence"])
dataset["image_003"]["confidence"] = 0.99
dataset["image_001"]["model"] = "yolov10"
print(dataset)


data = {
    "images": [
        {
            "filename": "apple.jpg",
            "class": "apple",
            "confidence": 0.96
        },
        {
            "filename": "banana.jpg",
            "class": "banana",
            "confidence": 0.91
        },
        {
            "filename": "orange.jpg",
            "class": "orange",
            "confidence": 0.98
        }
    ]
}

print(data["images"])
print(data["images"][0]["filename"])
print(data["images"][1]["confidence"])
data["images"][2]["confidence"] = 0.99
data["images"][0]["model"] = "YOLOv10"
print(data)
