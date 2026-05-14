class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for ast in asteroids:
            is_destroyed = False
            while stack and ast < 0 and stack[-1] > 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast):
                    stack.pop()
                    is_destroyed = True
                else:
                    is_destroyed = True
                break
            if not is_destroyed:
                stack.append(ast)

        return stack
        