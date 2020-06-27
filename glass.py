class Glass:
    def __init__(self, cap=4):
        self.capacity = cap
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def is_full(self):
        return len(self._stack) == self.capacity

    def top(self):
        return self._stack[-1]

    def pop(self):
        _x = self._stack[-1]
        self._stack = self._stack[:-1]
        return _x

    def size(self):
        return len(self._stack)

    def has_only_single_color_balls(self):
        balls = self.get_all_balls()
        for i in range(1, len(balls)):
            if balls[i - 1] != balls[i]:
                return False
        return True

    def push_array_of_balls(self, balls):
        if len(balls) + len(self._stack) > self.capacity:
            raise Exception("error: push_array_of_balls can't exceed glass capacity")
        for ball in balls:
            self.push(ball)

    def get_all_balls(self):
        balls = list()
        while len(balls) > 0:
            balls.append(self.pop())
        balls.reverse()
        return balls

    def push(self, ball):
        if self.is_full():
            raise Exception("error: can't place the ball stack is full")
        self._stack.append(ball)

    def clone(self):
        glass = Glass(self.capacity)
        glass.push_array_of_balls(self.get_all_balls())
        return glass

    def __rep__(self):
        return ",".join(self.get_all_balls())
