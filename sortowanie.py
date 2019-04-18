numbers = [2, 64, 84, 22, 17, 99, 8, 77, 58, 72]
print(numbers)
x = numbers[0]

a = 0

sorted = False



while not sorted:
    sorted = True
    for num in numbers:
        if numbers.index(num) < len(numbers) - 1 and num > numbers[(numbers.index(num) + 1)]:
            numbers.insert(numbers.index(num), numbers[(numbers.index(num) + 1)])
            numbers.pop(numbers.index(num)+1)
            sorted = False
    a += 1

print(numbers)

