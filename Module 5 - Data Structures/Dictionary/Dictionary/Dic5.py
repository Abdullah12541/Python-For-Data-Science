#9. Dictionary Comprehension:
squared = {n : n**2 for n in range(1,6)}
print(squared)

confidence = {
    "apple": 0.96,
    "banana": 0.91,
    "orange": 0.98,
    "potato": 0.87
}
confidence_percent = {key : value*100 for key, value in
                     confidence.items()}
print(confidence_percent)

high_confidence = {
    key : value for key, value in confidence.items()
    if value > .90 
}
print(high_confidence)


transform = {key : value*100 for key, value in confidence.items()
             if value > .90
}
print(transform)

student_marks = {
    "Ali": 85,
    "Ahmad": 72,
    "Abdullah": 91,
    "Sara": 88,
    "Zain": 0
}

passed_students = {
    key : value for key, value in student_marks.items()
    if value > 50 
}
print(passed_students)

detections = {
    "image_001": {
        "class": "apple",
        "confidence": 0.96
    },
    "image_002": {
        "class": "banana",
        "confidence": 0.91
    },
    "image_003": {
        "class": "orange",
        "confidence": 0.87
    },
    "image_004": {
        "class": "potato",
        "confidence": 0.98
    }
}

high_conf_detection = {
    key : value["class"] for key, value in detections.items()
    if value["confidence"] >= .90
}
print(high_conf_detection)

