import itertools

def count(n, k):
    def is_balanced(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def has_at_most_k_nested(s):
        stack = []
        max_nested = 0
        for c in s:
            if c == '(':
                stack.append(c)
                max_nested = max(max_nested, len(stack))
            elif c == ')':
                stack.pop()
        return max_nested <= k

    count = 0
    for s in itertools.product('()', repeat=n):
        s = ''.join(s)
        if is_balanced(s) and has_at_most_k_nested(s):
            count += 1
    return count


if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094
