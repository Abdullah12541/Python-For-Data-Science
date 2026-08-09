def get_dataset(dataset_name):
    classes = set()

    print(f"\n--- {dataset_name} ---")

    number_of_classes = int(
        input(f"How many classes are in {dataset_name}? ")
    )

    for i in range(1, number_of_classes + 1):
        class_name = input(f"Enter Class {i}: ").strip()
        classes.add(class_name)

    return classes


def compare_datasets(dataset_a, dataset_b):
    common_classes = dataset_a.intersection(dataset_b)
    missing_classes = dataset_a.difference(dataset_b)
    new_classes = dataset_b.difference(dataset_a)
    all_classes = dataset_a.union(dataset_b)
    unique_classes = dataset_a.symmetric_difference(dataset_b)

    return (
        common_classes,
        missing_classes,
        new_classes,
        all_classes,
        unique_classes
    )


def display_report(dataset_a, dataset_b):
    (
        common_classes,
        missing_classes,
        new_classes,
        all_classes,
        unique_classes
    ) = compare_datasets(dataset_a, dataset_b)

    print("\n" + "=" * 50)
    print("        DATASET CONSISTENCY REPORT")
    print("=" * 50)

    print(f"\nDataset A Classes : {len(dataset_a)}")
    print(f"Dataset B Classes : {len(dataset_b)}")

    print("\n" + "-" * 50)
    print("Common Classes")
    print("-" * 50)

    if common_classes:
        for class_name in sorted(common_classes):
            print(class_name)
    else:
        print("None")

    print("\n" + "-" * 50)
    print("Missing in Dataset B")
    print("-" * 50)

    if missing_classes:
        for class_name in sorted(missing_classes):
            print(class_name)
    else:
        print("None")

    print("\n" + "-" * 50)
    print("New Classes in Dataset B")
    print("-" * 50)

    if new_classes:
        for class_name in sorted(new_classes):
            print(class_name)
    else:
        print("None")

    print("\n" + "-" * 50)
    print("All Unique Classes")
    print("-" * 50)

    for class_name in sorted(all_classes):
        print(class_name)

    print("\n" + "-" * 50)
    print("Classes Unique to Either Dataset")
    print("-" * 50)

    if unique_classes:
        for class_name in sorted(unique_classes):
            print(class_name)
    else:
        print("None")

    print("\n" + "-" * 50)
    print("Dataset Status")
    print("-" * 50)

    if dataset_a == dataset_b:
        print("COMPATIBLE")
        print("Both datasets contain the same classes.")
    else:
        print("NOT COMPATIBLE")
        print("Review the class differences before merging.")

    print("\n" + "=" * 50)



dataset_a = get_dataset("Dataset A")
dataset_b = get_dataset("Dataset B")

display_report(dataset_a, dataset_b)