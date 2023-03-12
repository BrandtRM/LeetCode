test1 = [1,1,1,1,0,1,1,1,0,1,0,1,1,1]
test2 = [0,1,1,1,1,1,1,0,1,1,1,0]
test3 = []
test4 = [1,0]
test5 = [0,0,0,1,1,0,0,1,0,1,1,0]


def Longest_Sequence_1s_k_Flips(sequence, k):
    if(len(sequence) == 0):
        return 0
    positions = []
    positions.append(0)
    for index, item in enumerate(sequence):
        if item == 0:
            positions.append(index + 1)
    positions.append(len(sequence) + 1)
    
    if(len(positions) - 2 < k):
        return "k to large"
    elif(len(positions) - 2 == k):
        return len(sequence)
    i = 0
    left = positions[i]
    right = positions[i + k + 1]
    max_len = 0

    for i in range(len(positions) - 2):

        max_len = max(max_len, right - left - 1)

        left = positions[i]
        if(right > len(positions)):
            break
        right = positions[i + k + 1]
          
    return   max_len


print(Longest_Sequence_1s_k_Flips(test1, 2))
print(Longest_Sequence_1s_k_Flips(test2, 2))
print(Longest_Sequence_1s_k_Flips(test3, 2))
print(Longest_Sequence_1s_k_Flips(test4, 2))
print(Longest_Sequence_1s_k_Flips(test5, 2))
