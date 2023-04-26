def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[i+j] = left_half[i]
                i += 1
            else:
                lst[i+j] = right_half[j]
                j += 1

        lst[i+j:] = left_half[i:] + right_half[j:]

    return lst


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_list = list(first_string)
    second_string_list = list(second_string)

    merge_sort(first_string_list)
    merge_sort(second_string_list)

    if first_string == "" or second_string == "":
        return (
            "".join(first_string_list),
            "".join(second_string_list),
            False,
        )

    return (
        "".join(first_string_list),
        "".join(second_string_list),
        first_string_list == second_string_list,
    )
