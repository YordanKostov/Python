def negative_vs_positive(numbers):
    sum_negatives = sum([num for num in numbers if num < 0])
    sum_positives = sum([num for num in numbers if num >= 0])

    print(f"{sum_negatives}")
    print(f"{sum_positives}")
    if abs(sum_negatives) > sum_positives:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


negative_vs_positive([int(num) for num in input().split()])