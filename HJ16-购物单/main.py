import sys

n, m = map(lambda x: int(x), sys.stdin.readline().strip().split())
n //= 10
arr = []
for i in range(m):
    arr.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split())))
    arr[-1][0] //= 10
    arr[-1].append([])

i = 0
while i < len(arr):
    if arr[i][2] != 0:
        arr[arr[i][2] - 1][3].append([arr[i][0], arr[i][1]])
    i += 1

arr = list(filter(lambda x: x[2] == 0, arr))


def transfer_to_good_list(good):
    sub_good = good[3]
    good_len = len(sub_good)
    main_good_value = good[0] * good[1]
    if good_len == 0:
        return [(good[0], main_good_value)]
    elif good_len == 1:
        sub_good_0_value = sub_good[0][0] * sub_good[0][1]
        return [
            (good[0], main_good_value),
            (good[0] + sub_good[0][0], main_good_value + sub_good_0_value),
        ]
    elif good_len == 2:
        sub_good_0_value = sub_good[0][0] * sub_good[0][1]
        sub_good_1_value = sub_good[1][0] * sub_good[1][1]
        return [
            (good[0], main_good_value),
            (good[0] + sub_good[0][0], main_good_value + sub_good_0_value),
            (good[0] + sub_good[1][0], main_good_value + sub_good_1_value),
            (good[0] + sub_good[0][0] + sub_good[1][0], main_good_value + sub_good_0_value + sub_good_1_value),
        ]


goods_list = []
for i in range(len(arr)):
    goods_list.append(transfer_to_good_list(arr[i]))
del arr

# print(goods_list)

price_list = [-1] * (n + 1)
price_list[0] = 0
for k in range(len(goods_list)):
    for i in range(len(price_list) - 1, -1, -1):
        if price_list[i] >= 0:
            for j in range(len(goods_list[k])):
                if i + goods_list[k][j][0] <= n:
                    price_list[i + goods_list[k][j][0]] = max(
                        price_list[i + goods_list[k][j][0]],
                        price_list[i] + goods_list[k][j][1],
                    )

# print(price_list)

print(max(price_list)*10)
