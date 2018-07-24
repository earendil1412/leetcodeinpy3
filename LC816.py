class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        index = 0
        flag = True
        S = S[1:-1]
        for _ in S:
            if index == 0 or index == len(S):
                index = index + 1
                continue
            else:
                a = __add_dot__(S[:index])
                b = __add_dot__(S[index:])
                index = index + 1
                if len(a) > 0 and len(b) > 0:
                    for ia in a:
                        for ib in b:
                            result.append("(" + ia + ", " + ib + ")")

        return result


def __add_dot__(S):
    """
    :type S: str
    :rtype: List[str]
    """
    if len(S) == 1:
        return [S]
    if S[0] == "0" and S[len(S) - 1] == "0":
        return []
    if S[0] == "0":
        return [S[0] + "." + S[1:]]
    if S[len(S) - 1] == "0":
        return [S]
    result = [S]
    index = 0
    for _ in S:
        if index == 0 or index == len(S):
            index = index + 1
            continue
        else:
            result.append(S[:index] + "." + S[index:])
            index = index + 1
    return result


solution = Solution()
print(solution.ambiguousCoordinates("(0123)"))
# print(len(123))
