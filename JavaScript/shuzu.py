data = [
    3, 12, 25, 28, 34, 64, 84, 91, 109, 128, 161, 174, 175, 176, 185, 188, 193, 195, 199, 200,
    208, 226, 230, 303, 365, 417, 421, 424, 430, 468, 485, 487, 488, 554, 724, 822, 871, 968,
    1068, 1111, 1209, 1282, 1325, 1412, 1549, 1553, 1569, 1616, 1699, 1727, 1885, 1979, 2045,
    2142, 2348, 2578, 2734, 2912, 2915, 3229, 3294, 3331, 3577, 3666, 3956, 4092, 4445, 4558,
    4709, 5100, 5396, 5458, 5757, 5890, 6038, 6467, 6485, 6491, 6505, 6528, 6606, 6607, 6656,
    6665, 6669, 6670, 6676, 6706, 6831, 6926, 6930, 6958, 7025, 7055, 7142, 7143, 7169, 8224,
    8319, 8460, 8584, 8669, 8728, 9059, 9263, 9324, 9369, 9431, 9464, 9503, 9516, 9541, 9613,
    9646, 9680, 9712, 9713, 9739, 9899, 9900, 9909, 10002, 10045, 10070, 10074, 10146, 10269,
    10292, 10293, 10304, 10400, 10406, 10423, 10538, 10781, 10790, 7556, 7557, 7558, 7559,
    7560, 7689, 7692
]

# 转换为字符串数组
string_array = [str(num).zfill(5) for num in data]

print(string_array)