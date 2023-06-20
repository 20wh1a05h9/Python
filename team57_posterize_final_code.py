red_pixels = int(input('Enter no of red pixels : '))
allowed_integers = int(input('Enter no of integers that need to be allowed : '))
limit = 256
list_red_values = []

def get_index(v):
    for intensity_value in range(red_pixels):
        if list_red_values[intensity_value][0] > v:
            return intensity_value
    return red_pixels - 1

def base(previous, used):
    if used == allowed_integers:
        total = 0
        ind = get_index(int(previous))
        for i in range(ind , red_pixels):
            total += list_red_values[i][1] * (list_red_values[i][0] - previous) * (list_red_values[i][0] - previous)
        return total
    res = -1

    for right_value in range(previous + 1, limit):
        total = 0
        ind = get_index(int(previous))
        for right_index in range(ind , red_pixels):
            if list_red_values[right_index ][0] > right_value :
                break
            total1 = list_red_values[right_index ][0] - previous
            total1 = min(total1, right_value - list_red_values[right_index ][0])
            total += total1 * total1 * list_red_values[right_index ][1]
        ans = total + base(right_value, used + 1)
        if res == -1:
            res = ans
        else:
            res = min(res, ans)
    return res

def main():
    for entries in range(red_pixels):
        intensity = int(input('Enter intensity : '))
        pixels = int(input('Enter no of pixels : '))
        list_red_values.append([intensity, pixels])
    ans = -1
    for allowed_intensity in range(limit):
        total = 0
        for allowed_intensity_1 in range(red_pixels):
            if list_red_values[allowed_intensity_1][0] > allowed_intensity:
                break
            total += (allowed_intensity - list_red_values[allowed_intensity_1][0]) * (allowed_intensity - list_red_values[allowed_intensity_1][0]) * list_red_values[allowed_intensity_1][1]
        total += base(allowed_intensity, 1)
        if ans == -1:
            ans = total
        else:
            ans = min(ans, total)
    return ans

print(main())
