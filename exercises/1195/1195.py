class Node:
    def __init__(self, data: int = None) -> None:
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data: int):
        if not self.data:
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
    
    def inorder(self, datas = []):
        if self.left is not None:
            self.left.inorder(datas)
        if self.data is not None:
            datas.append(self.data)
        if self.right is not None:
            self.right.inorder(datas)
        return " ".join(map(str, datas))

    def preorder(self, datas = []):
        if self.data is not None:
            datas.append(self.data)
        if self.left is not None:
            self.left.preorder(datas)
        if self.right is not None:
            self.right.preorder(datas)
        return " ".join(map(str, datas))

    def postorder(self, datas = []):
        if self.left is not None:
            self.left.postorder(datas)
        if self.right is not None:
            self.right.postorder(datas)
        if self.data is not None:
            datas.append(self.data)
        return " ".join(map(str, datas))

def init_case(index: int):
    node = Node()
    num_nodes = int(input())

    data_inputs = map(int, input().split())

    for data in data_inputs:
        node.insert(data)
    
    print(f"Case {index + 1}:")
    print(f"Pre.: {node.preorder()}")
    print(f"In..: {node.inorder()}")
    print(f"Post: {node.postorder()}")


def main():
    num_cases = int(input())
    for index in range(0, num_cases):
        init_case(index)

if __name__ == "__main__":
    main()
