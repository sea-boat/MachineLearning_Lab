import random
from enum import Enum

TIMES = 200
R = 0.05
ALPHA = 0.1
GAMMA = 0.9
ROWS = 5
COLUMNS = 6
ENTRANCE = (0, 0)
EXIT = (4, 5)
BARRIERS = list()
BARRIERS.append((1, 1))
BARRIERS.append((2, 1))
BARRIERS.append((3, 1))
BARRIERS.append((4, 1))
BARRIERS.append((0, 3))
BARRIERS.append((1, 3))
BARRIERS.append((3, 3))
BARRIERS.append((4, 3))
BARRIERS.append((3, 4))
BARRIERS.append((1, 5))
q_values = dict()
results = list()


class Actions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


class State:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def init_q_values():
    for row in range(0, ROWS):
        for col in range(0, COLUMNS):
            state = State(row, col)
            for action in Actions:
                q = (state.row, state.col, action)
                q_values[q] = 0


def explore(curr_state):
    rand = random.random()
    if rand <= R:
        return random.choice(list(Actions))
    else:
        best = list()
        best_action = Actions.up
        best_value = -10000000
        for action in Actions:
            q = (curr_state.row, curr_state.col, action)
            if q_values[q] > best_value:
                best_action = action
                best_value = q_values[q]
        best.append(best_action)
        # perhaps it has not only one best action
        for action in Actions:
            q = (curr_state.row, curr_state.col, action)
            if action != best_action:
                if q_values[q] == best_value:
                    best.append(action)
        return random.choice(best)


def move(curr_state, action):
    new_state = State(curr_state.row, curr_state.col)
    # check borders
    if action == Actions.up:
        if (new_state.row - 1) >= 0:
            new_state.row -= 1
    elif action == Actions.down:
        if (new_state.row + 1) <= (ROWS - 1):
            new_state.row += 1
    elif action == Actions.left:
        if (new_state.col - 1) >= 0:
            new_state.col -= 1
    elif action == Actions.right:
        if (new_state.col + 1) <= (COLUMNS - 1):
            new_state.col += 1
    return new_state


def update(curr_state, last_action):
    q = (curr_state.row, curr_state.col, last_action)
    new_state = move(curr_state, last_action)
    position = (new_state.row, new_state.col)
    reward = -1
    if position == EXIT:
        reward = 0
    elif position in BARRIERS:
        reward = -100
    old_value = q_values[q]
    max_new = max([q_values[(new_state.row, new_state.col, a)] for a in Actions])
    q_values[q] = old_value + ALPHA * (reward + (GAMMA * max_new) - old_value)
    curr_state.row = new_state.row
    curr_state.col = new_state.col


def update_results(temp_results):
    global results
    if len(results) > 0:
        if (results[-1][0] == EXIT[0]) and (results[-1][1] == EXIT[1]):
            if (temp_results[-1][0] == EXIT[0]) and (temp_results[-1][1] == EXIT[1]):
                if len(temp_results) < len(results):
                    results = temp_results
        elif (temp_results[-1][0] == EXIT[0]) and (temp_results[-1][1] == EXIT[1]):
            results = temp_results
        elif len(temp_results) > len(results):
            results = temp_results
    else:
        results = temp_results


def try_exploring():
    temp_results = list()
    curr_state = State(ENTRANCE[0], ENTRANCE[1])
    ended = False
    while not ended:
        last_action = explore(curr_state)
        q = (curr_state.row, curr_state.col, last_action)
        temp_results.append(q)
        update(curr_state, last_action)
        position = (curr_state.row, curr_state.col)
        if (position[0] == EXIT[0]) and (position[1] == EXIT[1]):
            q = (curr_state.row, curr_state.col, last_action)
            temp_results.append(q)
            ended = True
        else:
            for barrier in BARRIERS:
                if (position[0] == barrier[0]) and (position[1] == barrier[1]):
                    q = (curr_state.row, curr_state.col, last_action)
                    temp_results.append(q)
                    ended = True
                    break
    return temp_results


if __name__ == '__main__':
    init_q_values()
    for i in range(0, TIMES):
        results = try_exploring()
        update_results(results)
    for a in results:
        print(a[2])
