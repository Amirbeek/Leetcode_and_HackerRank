def topKFrequent(nums: list[int], k: int) -> list[int]:
    basket = {}

    for num in nums:
        if num not in basket:
            basket[num] = 1
            continue
        basket[num] += 1

    arr = []
    for v, i in basket.items():
        print(v, i)


topKFrequent([1, 2, 2, 3], 2)
