class Solution:
    def romanToInt(self, s: str) -> int:
            sol = 0
            it = 0

            while it < len(s):
                print(str(it) + ' | ' + str(sol) + ' | ' + str(s[it]))
                if s[it] == 'M':
                    sol += 1000
                elif s[it] == 'D':
                    sol += 500
                elif s[it] == 'C':
                    if it + 1 < len(s) and s[it + 1] == 'M':
                        sol += 900
                        it += 1
                    elif it + 1 < len(s) and s[it + 1] == 'D':
                        sol += 400
                        it += 1
                    else:
                        sol += 100
                elif s[it] == 'L':
                    sol += 50
                elif s[it] == 'X':
                    if it + 1 < len(s) and s[it + 1] == 'C':
                        sol += 90
                        it += 1
                    elif it + 1 < len(s) and s[it + 1] == 'L':
                        sol += 40
                        it += 1
                    else:
                        sol += 10
                elif s[it] == 'V':
                    sol += 5
                elif s[it] == 'I':
                    if it + 1 < len(s) and s[it + 1] == 'X':
                        sol += 9
                        it += 1
                    elif it + 1 < len(s) and s[it + 1] == 'V':
                        sol += 4
                        it += 1
                    else:
                        sol += 1
                    
                it += 1
            return sol
