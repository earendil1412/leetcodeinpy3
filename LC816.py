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
        for i in S:
            if index == 0 or index == len(S):
                index = index + 1
                continue
            else:
                a = S[:index]
                b = S[index:]
                index = index + 1
                x = 1
                for _ in a:
                    xa = ""
                    if len(float_to_str(float(a) / x)) - 1 == len(a):
                        xa = float_to_str(float(a) / x)
                    x = x * 10
                    y = 1
                    for _ in b:
                        xb = ""
                        if len(float_to_str(float(b) / y)) - 1 == len(b):
                            xb = float_to_str(float(b) / y)
                        y = y * 10
                        if xa == "" and xb == "":
                            continue
                        if xa != "" and xb != "" and float(xa.split(".")[1]) != 0 and float(xb.split(".")[1]) != 0:
                            result.append("(" + xa + ", " + xb + ")")
                            continue
                        if xa == "" and xb != "" and float(xb.split(".")[1]) != 0 and len(a) == len(str(int(a))):
                            result.append("(" + a + ", " + xb + ")")
                            continue
                        if xb == "" and xa != "" and float(xa.split(".")[1]) != 0 and len(b) == len(str(int(b))):
                            result.append("(" + xa + ", " + b + ")")
                            continue
                if len(a) == len(str(int(a))) and len(b) == len(str(int(b))):
                    result.append("(" + a + ", " + b + ")")

        return list(set(result))

def float_to_str(f):
    float_string = repr(f)
    if 'e' in float_string:  # detect scientific notation
        digits, exp = float_string.split('e')
        digits = digits.replace('.', '').replace('-', '')
        exp = int(exp)
        zero_padding = '0' * (abs(int(exp)) - 1)  # minus 1 for decimal point in the sci notation
        sign = '-' if f < 0 else ''
        if exp > 0:
            float_string = '{}{}{}.0'.format(sign, digits, zero_padding)
        else:
            float_string = '{}0.{}{}'.format(sign, zero_padding, digits)
    return float_string

solution = Solution()
print(solution.ambiguousCoordinates("(123)"))
# print(len(123))
