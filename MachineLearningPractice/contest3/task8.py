def count_similar_numbers(args):
    max_count = 1
    current_count = 1
    for i in range(1, len(args)):
        if args[i] == args[i-1]:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 1

    return max_count