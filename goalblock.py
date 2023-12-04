50, 48, 68) Implement goal stack planning for block world problem
class BlockWorld:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_stack = []

    def apply_action(self, action):
        if action[0] == 'move':
            block, source, destination = action[1], action[2], action[3]

            # Check if the block is in the state before removing it
            if (block, source) in self.state:
                self.state.remove((block, source))
                self.state.append((block, destination))
            else:
                print(f"Warning: Block {block} not found at {source}. Skipping action.")

    def is_goal_achieved(self):
        return all(item in self.state for item in self.goal_stack)

    def execute_plan(self, plan):
        for action in plan:
            self.apply_action(action)
            print(f"Action: {action}, State: {self.state}")

def block_world_planning(goal_state, initial_state):
    block_world = BlockWorld(initial_state)
    block_world.goal_stack = goal_state

    plan = []
    for goal in goal_state:
        if goal not in block_world.state:
            sub_plan = [('move', item[0], item[1], goal[1]) for item in block_world.state if item[0] == goal[0]]
            plan.extend(sub_plan)
            plan.append(('move', goal[0], goal[1], 'table'))

    return plan

if __name__ == "__main__":
    initial_state = [('A', 'table'), ('B', 'A'), ('C', 'table')]
    goal_state = [('A', 'table'), ('C', 'A'), ('B', 'C')]

    plan = block_world_planning(goal_state, initial_state)

    block_world = BlockWorld(initial_state)
    block_world.execute_plan(plan)

user input: class BlockWorld:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_stack = []

    def apply_action(self, action):
        if action[0] == 'move':
            block, source, destination = action[1], action[2], action[3]

            # Check if the block is in the state before removing it
            if (block, source) in self.state:
                self.state.remove((block, source))
                self.state.append((block, destination))
            else:
                print(f"Warning: Block {block} not found at {source}. Skipping action.")

    def is_goal_achieved(self):
        return all(item in self.state for item in self.goal_stack)

    def execute_plan(self, plan):
        for action in plan:
            self.apply_action(action)
            print(f"Action: {action}, State: {self.state}")

def get_user_input(prompt):
    user_input = input(prompt)
    return [tuple(item.split()) for item in user_input.split(',')]

if __name__ == "__main__":
    print("Enter the initial state (e.g., A table, B A, C table):")
    initial_state = get_user_input("Initial state: ")

    print("Enter the goal state (e.g., A table, C A, B C):")
    goal_state = get_user_input("Goal state: ")

    plan = block_world_planning(goal_state, initial_state)

    block_world = BlockWorld(initial_state)
    print("\nInitial State:", block_world.state)
    print("Goal State:", goal_state)

    block_world.execute_plan(plan)
