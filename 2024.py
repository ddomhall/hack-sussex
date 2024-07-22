# https://www.youtube.com/watch?v=VixYfv0UEyE

# def swappable(s1, s2):
#     count = 0
#     characters = set()
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             count += 1 
#             characters.add(s1[i])
#             characters.add(s2[i])
#     if count == 2 and len(characters) == 2:
#         return True
#     else:
#         return False
#
# print(swappable('bank', 'kanb'))

def validRectangles(rectangles):
    highest = 0
    for rect in rectangles:
        square = min(rect[0], rect[1])
        if square > highest:
            highest = square

    count = 0
    for rect in rectangles:
        square = min(rect[0], rect[1])
        if square >= highest:
            count += 1

    return count

input = [[5, 8], [3, 9], [5, 12], [16, 5]]
print(validRectangles(input))
