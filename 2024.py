# https://www.youtube.com/watch?v=VixYfv0UEyE

def swappable(s1, s2):
    count = 0
    characters = set()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1 
            characters.add(s1[i])
            characters.add(s2[i])
    if count == 2 and len(characters) == 2:
        return True
    else:
        return False

print(swappable('bank', 'kanb'))
