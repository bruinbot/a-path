class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    def __lt__(self, other):
        return self.f < other.f
    def __gt__(self, other):
        return self.f < other.f

from heapq import heappush, heappop

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = set()

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node with smallest f value and pop it 
        current_node = heappop(open_list)

        # Add to closed list
        closed_list.add(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closed_list:
                continue
          

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            heappush(open_list, child)


def main():

    maze = [[0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, "X", 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    from copy import deepcopy
    traversed = deepcopy(maze)
    cnt = 1
    for i,j in path:
        traversed[i][j] = cnt
        cnt+=1
  
    print(path)
    for i in traversed:
        print(i)


if __name__ == '__main__':
    main()