s = input("Введите числа от 1 до 999 через пробел(в любом порядке): ")

if ' ' not in s:
    s = input("Введены некорректные данные(либо введено одно число). Введите числа от 1 до 999 через пробел(в любом порядке): ")

s = s.split() #Преобразование введённой последовательности в список

s = [int(b) for b in s] #Преобразование в числа

for i in range(len(s)):
    if s[i] < 1 or s[i] > 999:
        s = input("Введены некорректные данные. Введите числа от 1 до 999 через пробел(в любом порядке): ")
        s = s.split()  # Преобразование введённой последовательности в список
        s = [int(b) for b in s]  # Преобразование в числа
        break


def merge_sort(s):
    if len(s) < 2:
        return s[:]
    else:
        middle = len(s) // 2
        left = merge_sort(s[:middle])
        right = merge_sort(s[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(s))

def binary_search(s, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if s[middle] == element:
        return middle
    elif element < s[middle]:
        return binary_search(s, element, left, middle - 1)
    else:
        return binary_search(s, element, middle + 1, right)


while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")


print(binary_search(s, element, 0,  len(s)))













