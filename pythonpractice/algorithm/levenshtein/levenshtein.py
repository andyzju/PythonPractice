# coding=utf-8

def getLevenshtein(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    len1 = len(str1) + 1
    len2 = len(str2) + 1

    matrix = [range(len2) for x in range(len1)]  #创建二维数组方法

    for j in range(len2):
        matrix[0][j] = j
    for i in range(len1):
        matrix[i][0] = i

    print matrix

    print str1, str2
    for i in range(1, len1):
        for j in range(1, len2):
            f = 0
            if str1[i-1] != str2[j-1]:
                f = 1
            else:
                f = 0

            dist1 = matrix[i-1][j] + 1
            dist2 = matrix[i][j-1] + 1
            dist_diff = matrix[i-1][j-1] + f

            matrix[i][j] = min(dist1, dist2, dist_diff)

    print len1, len2
    print matrix

    print matrix[len1-1][len2-1]



if __name__ == "__main__":
    getLevenshtein("abcd", "abcef")



