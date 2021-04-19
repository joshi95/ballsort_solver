import copy


class Glass:
    def __init__(self, cap):
        self.capacity = cap
        self.glasses_stack = list()

    @staticmethod
    def create_glass(balls, cap=4):
        g = Glass(cap)
        g.push_array_of_balls(balls)
        return g

    def is_empty(self):
        return len(self.glasses_stack) == 0

    def is_full(self):
        return len(self.glasses_stack) == self.capacity

    def get_top(self):
        return self.glasses_stack[-1]

    def pop_ball(self):
        _x = self.glasses_stack[-1]
        self.glasses_stack = self.glasses_stack[:-1]
        return _x

    def get_size(self):
        return len(self.glasses_stack)

    def has_only_single_color_balls(self):
        balls = self.get_all_balls()
        for i in range(1, len(balls)):
            if balls[i - 1] != balls[i]:
                return False
        return True

    def push_array_of_balls(self, balls):
        if len(balls) + len(self.glasses_stack) > self.capacity:
            return False
        for ball in balls:
            self.push_ball(ball)

    def get_all_balls(self):
        balls = list()
        for i in range(0, len(self.glasses_stack)):
            balls.append(self.glasses_stack[i])
        return balls

    def push_ball(self, ball):
        if self.is_full():
            raise Exception
            return False
        self.glasses_stack.append(ball)

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return ",".join([str(x) for x in self.get_all_balls()])
