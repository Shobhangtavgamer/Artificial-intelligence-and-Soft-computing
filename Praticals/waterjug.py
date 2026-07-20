# Water Jug Problem using informed search Algorithm (A*)
import heapq
class State:
    def __init__(self, jug1, jug2, cost, parent=None):
        self.jug1 = jug1
        self.jug2 = jug2
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(state, target, goal_jug):
    if goal_jug == 1:
        return abs(state.jug1 - target)
    else:
        return abs(state.jug2 - target)

def get_neighbors(state, cap1, cap2):
    neighbors = []

    neighbors.append(State(cap1, state.jug2, state.cost + 1, state))

    neighbors.append(State(state.jug1, cap2, state.cost + 1, state))

    neighbors.append(State(0, state.jug2, state.cost + 1, state))

    neighbors.append(State(state.jug1, 0, state.cost + 1, state))

    transfer = min(state.jug1, cap2 - state.jug2)
    neighbors.append(
        State(
            state.jug1 - transfer,
            state.jug2 + transfer,
            state.cost + 1,
            state,
        )
    )

    transfer = min(state.jug2, cap1 - state.jug1)
    neighbors.append(
        State(
            state.jug1 + transfer,
            state.jug2 - transfer,
            state.cost + 1,
            state,
        )
    )

    return neighbors

def print_path(state):
    path = []

    while state is not None:
        path.append((state.jug1, state.jug2))
        state = state.parent

    path.reverse()

    print("\n Solution Path \n")

    for i, (j1, j2) in enumerate(path):
        print(f"Step {i}: Jug1 = {j1} L, Jug2 = {j2} L")

def astar(cap1, cap2, target, goal_jug):

    start = State(0, 0, 0)
    priority_queue = []
    heapq.heappush(
        priority_queue,
        (heuristic(start, target, goal_jug), start),
    )
    visited = set()
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if (current.jug1, current.jug2) in visited:
            continue
        visited.add((current.jug1, current.jug2))
        if goal_jug == 1:
            if current.jug1 == target:
                print_path(current)
                print("\nGoal Achieved!")
                print(f"{target} L is present in Jug 1.")
                return
        else:
            if current.jug2 == target:
                print_path(current)
                print("\nGoal Achieved!")
                print(f"{target} L is present in Jug 2.")
                return

        for neighbor in get_neighbors(current, cap1, cap2):
            if (neighbor.jug1, neighbor.jug2) not in visited:
                priority = neighbor.cost + heuristic(
                    neighbor,
                    target,
                    goal_jug,
                )

                heapq.heappush(
                    priority_queue,
                    (priority, neighbor),
                )

    print("\nNo solution exists.")

print("   Water Jug Problem using A* Search Algorithm")

cap1 = int(input("Enter capacity of Jug 1: "))
cap2 = int(input("Enter capacity of Jug 2: "))

target = int(input("\nEnter target amount of water: "))

print("\nSelect the Goal Jug")
print("1. Jug 1")
print("2. Jug 2")
goal_jug = int(input("Enter your choice (1 or 2): "))
if goal_jug not in [1, 2]:
    print("\nInvalid Choice!")
elif goal_jug == 1 and target > cap1:
    print("\nTarget exceeds Jug 1 capacity.")
elif goal_jug == 2 and target > cap2:
    print("\nTarget exceeds Jug 2 capacity.")
else:
    astar(cap1, cap2, target, goal_jug)
