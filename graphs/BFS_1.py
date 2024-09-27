# Поиск в ширину – это «слепой» алгоритм. Он называется «слепым», так как не учитывает стоимости перехода между
# вершинами графа. Алгоритм начинает работу с корневого узла (представляющего собой исходное состояние задачи) и
# исследует все узлы на рассматриваемом уровне, а только после этого переходит к узлам следующего уровня.
# Если алгоритм находит решение, то он возвращается и прекращает поиск, в противном случае наращивает от узла новое
# ребро и продолжает поиск. Алгоритм поиска в ширину является «полным» - это означает, что он всегда возвращает решение,
# если оно существует.  Точнее, алгоритм возвращает то решение, которое ближе всего к корню.
# Поэтому в задачах, где переход от узла к любому его дочернему узлу стоит единицу, алгоритм BFS возвращает
# наилучшее решение. Кроме того, чтобы исследовать узлы уровень за уровнем, он использует структуру данных под
# названием очередь, так что новые узлы добавляются в хвост очереди, а старые узлы удаляются из головы очереди.

from abc import ABC, abstractmethod


class Node(ABC):
    """
      Этот класс применяется для представления узла в графе
      Этот интерфейс важно реализовать, чтобы класс для BFS получился более общим,
      и его можно было использовать для решения различных задач
      ...


      Methods
      -------
      __eq__(self, other)
          Determines if two nodes are equal or not

      is_the_solution(self)
          Determines if the current node is the solution of the problem

      def is_the_solution(self)
          Extends the current node according to the rules of the problem

      __str__(self)
          Prints the node data
    """

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def is_the_solution(self, state):
        pass

    @abstractmethod
    def extend_node(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MazeNode(Node):
    """
      This class used to represent the node of a maze
      ...
      Attributes
      ----------
      graph : Dictionary
          represent the graph
      value : String
          represents the id of the vertex
      parent : MazeNode
          represents the parent of the current node

      Methods
      -------
      __eq__(self, other)
          Determines if the current node is the same with the other
      is_the_solution(self, final_state)
          Checks if the current node is the solution
      extend_node(self)
          Extends the current node, creating a new instance of MazeNode for each edge starts from current node
      _find_path(self)
          Find the path (all verticies and edges from the intitial state to the final state)
      __str__(self)
          Returns the solution of the maze, the whole path vertex by vertex in order to be printed properly.
    """

    def __init__(self, graph, value):
        self.graph = graph
        self.value = value
        self.parent = None

    def __eq__(self, other):
        """
          Check if the current node is equal with the other node.
          Parameters
          ----------
          Other : MazeNode
              The other vertex of the graph
          Returns
          -------
          Boolean
            True: if both verticies are the same
            False: If verticies are different
        """
        if isinstance(other, MazeNode):
            return self.value == other.value
        return self.value == other

    def is_the_solution(self, final_state):
        """
          Checks if the current node is the solution
          Parameters
          ----------
          final_state : MazeNode
              The target vertex (final state) of the graph
          Returns
          -------
          Boolean
            True: if both verticies are the same, so solution has been found
            False: If verticies are different, so solution has not been found
        """
        return self.value == final_state

    def extend_node(self):
        """
          Extends the current node, creating a new instance of MazeNode for each edge starts from the current node
          Returns
          -------
          List
            List with all valid new nodes
        """
        children = [MazeNode(self.graph, child) for child in self.graph[self.value]]
        for child in children:
            child.parent = self
        return children

    def _find_path(self):
        """
          Find the path, all verticies and edges from the intitial state to the final state
          Returns
          -------
          List
            List with all nodes fron start to end in a row
        """
        path = []
        current_node = self
        while current_node.parent is not None:
            path.insert(0, current_node.value)
            current_node = current_node.parent
        path.insert(0, current_node.value)
        return path

    def __str__(self):
        """
          Returns the solution of the maze, the whole path vertex by vertex as well as the path lenght, in order to be printed properly.
          Returns
          -------
          str
            the solution of the problem
        """
        total_path = self._find_path()
        path = ""
        for index in range(len(total_path)):
            if index == len(total_path) - 1:
                path += f"{total_path[index]} "
            else:
                path += f"{total_path[index]} -> "

        return path + f"\nPath lenght: {len(total_path) - 1}"

    def __repr__(self):
        return f'Node {self.value}'


class BFS:
    """
      This class used to represent the  Breadth First Search algorithm (BFS)

      ...

      Attributes
      ----------
      start_state : Node
          represent the initial state of the problem
      final_state : Node
          represent the final state (target) of the problem
      frontier : List
          represents the stack and is initialized with the start node
      checked_nodes : List
          represents the list of nodes that have been visited throughout the algorithm execution
      number_of_steps : Integer
          Keep track of the algorithm's number of steps
      path : List
          represents the steps from the initial state to the final state

      Methods
      -------
      insert_to_frontier(self, node)
          Insert a new node to the frontier. In this algorithm the frontier is a queue, so each new element is inserted to end of the data structure

      remove_from_frontier(self)
          Remove the first element from the frontier, following the FIFO technic. The removed node is added to the checked_node list

      remove_from_frontier(self)
          check if the frontier is empty

      search(self)
          Implements the core of algorithm. This method searches, in the search space of the problem, a solution
      """

    def __init__(self, start, final):
        self.start_state = start
        self.final_state = final
        self.frontier = [self.start_state]
        self.checked_nodes = []
        self.number_of_steps = 0
        self.path = []

    def insert_to_frontier(self, node):
        """
          Insert a node at the end of the frontier

          Parameters
          ----------
          node : Node
              The node of the problem that will be added to the frontier
        """
        self.frontier.append(node)

    def remove_from_frontier(self):
        """
          Remove a node from the beginning of the frontier
          Then add the removed node to the checked_nodes list

          Returns
          -------
          Node
            the first node of the frontier
        """
        first_node = self.frontier.pop(0)
        self.checked_nodes.append(first_node)
        return first_node

    def frontier_is_empty(self):
        """
          Check if the frontier id empty, so no solution found

          Returns
          -------
          Boolean
            True if the frontier is empty
            False if the frontier is not empty
        """
        if len(self.frontier) == 0:
            return True
        return False

    def search(self):
        """
          Is the main algorithm. Search for a solution in the solution space of the problem
          Stops if the frontier is empty, so no solution found or if find a solution.
        """
        while True:

            self.number_of_steps += 1

            print(f"Step: {self.number_of_steps}, Frontier: {self.frontier} ", end= '\t')

            if self.frontier_is_empty():
                print(f"No Solution Found after {self.number_of_steps} steps!!!")
                break

            selected_node = self.remove_from_frontier()
            print(f'slect node for next step: {selected_node.value}')



            # проверить, является ли выбранный узел решением задачи
            if selected_node.is_the_solution(self.final_state):
                print(f"Solution Found in {self.number_of_steps} steps")
                print(selected_node)
                break

            # нарастить узел
            new_nodes = selected_node.extend_node()

            # добавить нарощенные узлы на передний край
            if len(new_nodes) > 0:
                for new_node in new_nodes:
                    if new_node not in self.frontier and new_node not in self.checked_nodes:
                        self.insert_to_frontier(new_node)


graph = {
    "A": ['S'],
    "B": ['C', 'D', 'S'],
    "C": ['B', 'J'],
    "D": ['B', 'G', 'S'],
    "E": ['G', 'S'],
    "F": ['G', 'H'],
    "G": ['D', 'E', 'F', 'H', 'J'],
    "H": ['F', 'G', 'I'],
    "I": ['H', 'J'],
    "J": ['C', 'G', 'I'],
    "S": ['A', 'B', 'D', 'E']
  }

start_node = MazeNode(graph, 'A')
end_node = MazeNode(graph, 'H')
print(start_node)
bfc = BFS(start_node, end_node)
bfc.search()