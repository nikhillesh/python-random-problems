def numDecodings(s: str) -> int:
    if not s or s[0] == '0':  # If the string is empty or starts with '0', return 0
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: one way to decode an empty string
    dp[1] = 1 if s[0] != '0' else 0  # Base case: if the first character is not '0', one way to decode

    for i in range(2, n + 1):
        # Check the last one digit
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        # Check the last two digits
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]

print(numDecodings("1132634"))