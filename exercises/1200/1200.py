class Node:
  def __init__(self, data: str = None) -> None:
    self.data = data
    self.right = None
    self.left = None

  def insert(self, data: str):
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
    return " ".join(datas)

  def preorder(self, datas = []):
    if self.data is not None:
      datas.append(self.data)
    if self.left is not None:
      self.left.preorder(datas)
    if self.right is not None:
      self.right.preorder(datas)
    return " ".join(datas)

  def postorder(self, datas = []):
    if self.left is not None:
      self.left.postorder(datas)
    if self.right is not None:
      self.right.postorder(datas)
    if self.data is not None:
      datas.append(self.data)
    return " ".join(datas)

  def search(self, node, data):
    if not data or not node:
      return False
    
    if node.data == data:
      return True

    response_1 = self.search(node.left, data)
    if response_1:
      return True

    response_2 = self.search(node.right, data)
    if response_2:
      return True
            

def main(node: Node):
  try:
    data = input().split()
  except EOFError:
    return

  if not data:
    return

  if data[0] == "I":
    node.insert(data[1])
  elif data[0] == "P":
    response = node.search(node, data[1])
    if response:
      print(f"{data[1]} existe")
    else:
      print(f"{data[1]} nao existe")
  elif data[0] == "INFIXA":
    print(node.inorder([]))
  elif data[0] == "PREFIXA":
    print(node.preorder([]))
  elif data[0] == "POSFIXA":
      print(node.postorder([]))

  main(node)

if __name__ == "__main__":
  node = Node()
  main(node)
