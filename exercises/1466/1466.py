import collections

class Node:
    def __init__(self, data: int = None) -> None:
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data: int):
        if self.data is None:
            self.data = data
            return
        
        if self.data == data:
            return

        if self.data > data:
            if self.left:
                self.left.insert(data)
                return
            self.left = Node(data)
            return
        
        if self.data < data:
            if self.right:
                self.right.insert(data)
                return
            self.right = Node(data)
            return   

    def levelOrderTraversal(self):
        response = list()

        if self.data is None:
            return response

        queue = collections.deque()
        queue.append(self)

        while queue:
            current_size = len(queue)
            current_list = list()

            while current_size > 0:
                current_node = queue.popleft()
                current_list.append(current_node.data)
                current_size -= 1

                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            
            response.extend(current_list)
        
        return response
            


def init_case(index: int):
    node = Node()
    num_nodes = int(input())

    data_inputs = map(int, input().split())

    for data in data_inputs:
        node.insert(data)

    print(f"Case {index+1}:")
    print(" ".join(map(str, node.levelOrderTraversal())))
    print()


def main():
    num_cases = int(input())
    for index in range(0, num_cases):
        init_case(index)

if __name__ == "__main__":
    main()
