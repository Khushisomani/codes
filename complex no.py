class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a, b = a.split('+'), b.split('+')    # split integer part and complex part
        a1, b1 = int(a[0]), int(a[-1][:-1])  # convert to integer
        a2, b2 = int(b[0]), int(b[-1][:-1])
        x = a1*a2                            # multiplication first part integer*integer 
        y = a1*b2+a2*b1                      # integer * complex
        z = -(b1*b2)                         # complex * complex
        return f'{str(x+z)}+{str(y)}i' 
        