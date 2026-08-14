models = {
    "Random Forest": {
        "accuracy": 0.92,
        "precision": 0.90,
        "recall": 0.88,
        "f1_score": 0.89
    },
    "Logistic Regression": {
        "accuracy": 0.87,
        "precision": 0.85,
        "recall": 0.84,
        "f1_score": 0.84
    },
    "SVM": {
        "accuracy": 0.94,
        "precision": 0.93,
        "recall": 0.91,
        "f1_score": 0.92
    }
}


def display_models():
    for name, metrics in models.items():
        print(f"\n{name}")
        print(f"Accuracy: {metrics['accuracy'] * 100:.1f}%")
        print(f"Precision: {metrics['precision'] * 100:.1f}%")
        print(f"Recall: {metrics['recall'] * 100:.1f}%")
        print(f"F1-Score: {metrics['f1_score'] * 100:.1f}%")


def average_metrics():
    totals = {
        "accuracy": 0,
        "precision": 0,
        "recall": 0,
        "f1_score": 0
    }

    for metrics in models.values():
        for metric in totals:
            totals[metric] += metrics[metric]

    print("\nAverage Metrics:")
    for metric, total in totals.items():
        average = total / len(models)
        print(f"{metric}: {average * 100:.2f}%")


def best_model():
    metric = input(
        "\nEnter metric (accuracy, precision, recall, f1_score): "
    ).lower()

    best_name = None
    best_value = 0

    for name, metrics in models.items():
        if metrics[metric] > best_value:
            best_value = metrics[metric]
            best_name = name

    print(f"\nBest Model based on {metric}:")
    print(f"{best_name} → {best_value * 100:.1f}%")


def filter_models():
    threshold = float(input("\nEnter minimum accuracy (e.g. 0.90): "))

    high_accuracy = {
        name: metrics
        for name, metrics in models.items()
        if metrics["accuracy"] >= threshold
    }

    print("\nModels Above Accuracy Threshold:")

    for name, metrics in high_accuracy.items():
        print(f"{name} → {metrics['accuracy'] * 100:.1f}%")


while True:
    print("\n========== ML MODEL PERFORMANCE ANALYZER ==========")
    print("1. Display All Models")
    print("2. Show Average Metrics")
    print("3. Find Best Model")
    print("4. Show Models Above Accuracy")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_models()

    elif choice == "2":
        average_metrics()

    elif choice == "3":
        best_model()

    elif choice == "4":
        filter_models()

    elif choice == "5":
        print("\nThank you for using ML Model Performance Analyzer!")
        break

    else:
        print("Invalid choice. Please try again.")