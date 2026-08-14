# 📖 Python Dictionaries

This folder contains my learning and practice work for **Python Dictionaries**, completed as part of **Module 5: Data Structures** in my Python for Data Science learning journey.

Dictionaries are one of the most important Python data structures for Data Science because they allow data to be stored as **key-value pairs** and are commonly used for structured records, configuration data, JSON data, API responses, and machine learning results.

---

## 📚 Topics Covered

### 1. Creating Dictionaries
- Creating dictionaries
- Key-value pairs
- Empty dictionaries
- Dictionary data types

### 2. Accessing Values
- Accessing values using keys
- `get()`
- Default values with `get()`

### 3. Updating Dictionaries
- Adding new key-value pairs
- Updating existing values
- `update()`

### 4. Dictionary Methods
- `keys()`
- `values()`
- `items()`
- `pop()`
- `popitem()`
- `clear()`
- `copy()`
- `setdefault()`

### 5. Nested Dictionaries
- Dictionary inside a dictionary
- Accessing nested values
- Updating nested data
- Adding and removing nested values
- Dictionary → List → Dictionary structures
- Data Science and computer vision style structured data

### 6. Built-in Functions
Practiced dictionary-related use of:
- `len()`
- `max()`
- `min()`
- `sum()`
- `sorted()`
- `any()`
- `all()`
- `type()`

### 7. Dictionary Traversal
- Traversing keys
- Traversing values
- Traversing key-value pairs
- Filtering data while traversing
- Accumulating values
- Finding maximum values
- Calculating averages
- Traversing nested dictionaries
- Dictionary → List → Dictionary traversal

### 8. Dictionary Comprehension
- Basic dictionary comprehension
- Transforming values
- Filtering records
- Filtering and transforming simultaneously
- Working with nested dictionary data

---

## 🧠 Data Science Applications

The practice in this folder focuses on situations that are relevant to Data Science, Machine Learning, and Computer Vision.

Examples include:

- Student performance records
- Machine learning model metrics
- Object detection results
- Confidence scores
- Structured detection data
- Filtering high-confidence predictions
- Processing nested records

Example structure:

```python
detections = {
    "image_001": {
        "class": "apple",
        "confidence": 0.96
    },
    "image_002": {
        "class": "banana",
        "confidence": 0.91
    }
}
