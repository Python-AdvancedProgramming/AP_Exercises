def find_indices(items: list, target) -> list[int]:
    return [i for i, item in enumerate(items) if item == target]


# Test
print(find_indices(["a", "b", "a", "c", "a"], "a"))  # [0, 2, 4]
print(find_indices([1, 2, 3, 2, 4, 2], 2))          # [1, 3, 5]
