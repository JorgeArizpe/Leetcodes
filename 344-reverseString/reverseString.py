def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s) - 1

    for i in range(int(n/2) + 1):
        s[i], s[n - i] = s[n - i], s[i]

s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]

reverseString(s)

print(len(s))