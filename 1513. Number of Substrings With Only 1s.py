class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        curr = 0   # length of current consecutive '1's

        for ch in s:
            if ch == '1':
                curr += 1          # extend the current block of 1's
                ans += curr        # add all substrings ending here
            else:
                curr = 0           # reset when we hit '0'

        return ans % MOD
