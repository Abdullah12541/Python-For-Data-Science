# Sets — Python for Data Science

This folder contains my learning and practice work for **Python Sets** as part of my Python for Data Science journey.

Sets are an unordered collection of unique elements. They are especially useful for removing duplicate values, performing membership checks, and comparing collections using mathematical set operations.

## Topics Covered

### 1. Creating Sets

* Creating sets using `{}`.
* Creating empty sets using `set()`.
* Creating sets from lists, tuples, and strings.
* Understanding automatic removal of duplicate values.
* Understanding why sets are unordered.
* Understanding why individual elements cannot be accessed using indexing.

### 2. Adding and Removing Elements

Methods practiced:

* `add()`
* `update()`
* `remove()`
* `discard()`
* `pop()`
* `clear()`

The differences between `remove()` and `discard()`, and the behavior of `pop()` were also explored.

### 3. Set Methods

The `copy()` method was studied along with its behavior and return value.

### 4. Set Operations

Mathematical set operations were implemented using both methods and operators:

| Operation            | Method                   | Operator |
| -------------------- | ------------------------ | -------- |
| Union                | `union()`                | `\|`     |
| Intersection         | `intersection()`         | `&`      |
| Difference           | `difference()`           | `-`      |
| Symmetric Difference | `symmetric_difference()` | `^`      |

These operations were practiced for comparing datasets and identifying common, missing, and unique classes.

### 5. Membership Operators

* `in`
* `not in`

Membership operators were used to check whether particular elements exist in a set.

Both operators return a Boolean value: `True` or `False`.

### 6. Built-in Functions

The following built-in functions were practiced with sets:

* `len()`
* `min()`
* `max()`
* `sum()`
* `sorted()`
* `any()`
* `all()`

An important distinction was learned:

> `sorted()` accepts a set but returns a **list**, not a set.

### 7. Traversing Sets

Sets were traversed using `for` loops.

Because sets are unordered, their iteration order should not be relied upon.

---

## Set Methods and Return Values

| Method      | Purpose                                                     | Return Value    |
| ----------- | ----------------------------------------------------------- | --------------- |
| `add()`     | Adds one element                                            | `None`          |
| `update()`  | Adds multiple elements                                      | `None`          |
| `remove()`  | Removes a specified element                                 | `None`          |
| `discard()` | Removes an element without raising an error if it is absent | `None`          |
| `pop()`     | Removes and returns an arbitrary element                    | Removed element |
| `clear()`   | Removes all elements                                        | `None`          |
| `copy()`    | Creates a copy of the set                                   | New set         |

The distinction between methods that modify the original set and methods that return a useful value was also practiced.

---

## Hashability

Sets can only contain **hashable objects**.

Examples of hashable built-in objects include:

* `int`
* `float`
* `str`
* `bool`
* Tuples whose elements are themselves hashable

Mutable objects such as:

* `list`
* `set`
* `dict`

cannot be directly stored as elements of a set because they are unhashable.

A `frozenset` can be used when an immutable set-like object needs to be stored inside another set.

---

# Mini Project — Dataset Label Consistency Checker

## Problem

In Data Science and Machine Learning, datasets may come from different sources. Before considering combining two datasets, it is useful to compare their class/label definitions.

For example:

**Dataset A**

```text
Apple
Banana
Orange
Potato
```

**Dataset B**

```text
Apple
Orange
Potato
Tomato
```

The project identifies the differences between the two sets of labels.

## What the Project Does

The **Dataset Label Consistency Checker**:

1. Accepts class labels for Dataset A.
2. Accepts class labels for Dataset B.
3. Counts the classes in each dataset.
4. Finds common classes.
5. Finds classes present in Dataset A but missing from Dataset B.
6. Finds new classes present in Dataset B but not Dataset A.
7. Finds all unique classes across both datasets.
8. Finds classes belonging to only one dataset.
9. Determines whether the two datasets have consistent class labels.
10. Generates a readable comparison report.

## Set Concepts Used

The project applies the Sets concepts learned in this module:

* Set creation
* `add()`
* `len()`
* `union()`
* `intersection()`
* `difference()`
* `symmetric_difference()`
* `for` loops
* Membership and conditional logic

## Example Analysis

Given:

```text
Dataset A:
Apple
Banana
Orange
Potato

Dataset B:
Apple
Orange
Potato
Tomato
```

The checker can determine:

```text
Common Classes:
Apple
Orange
Potato

Missing in Dataset B:
Banana

New Classes in Dataset B:
Tomato

All Unique Classes:
Apple
Banana
Orange
Potato
Tomato
```

The project reports that the datasets are **not label-compatible** and should be reviewed before merging.

## Important Scope

This project checks **class/label consistency only**.

It does not validate:

* Image quality
* Annotation correctness
* Duplicate samples
* Class distributions
* Image dimensions
* File formats
* Data leakage
* Feature distributions

Therefore, matching class labels does not by itself prove that two datasets are fully ready for merging.

---

## Learning Outcome

Through this module, I practiced using Python Sets not only as a data structure but also as a practical tool for **data comparison and dataset preparation**.

The Dataset Label Consistency Checker demonstrates how fundamental Python concepts can be applied to a simple problem from the **Data Science and Machine Learning workflow**.
