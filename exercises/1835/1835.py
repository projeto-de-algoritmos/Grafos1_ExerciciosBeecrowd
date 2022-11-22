def solve(index: int):
  x = input()
  if(' ' not in str(x)):
    M = int(input())
    N = int(x)
  else:
    N, M = x.split()
    N = int(N)
    M = int(M)

  nodes = {}

  for n in range(1, N + 1):
    nodes[n] = [n];

  for m in range(M):
    x = input()
    if(' ' not in str(x)):
      n2 = int(input())
      n1 = int(x)
    else:
      n1, n2 = x.split()
      n1 = int(n1)
      n2 = int(n2)

    nodes[n1].append(n2)
    nodes[n2].append(n1)

  graph = []

  for i in range(1, N + 1):
    graph.append(nodes[i])

  for i in range(len(graph) - 1):
    size = len(graph[i])
    if(graph[i] == '-'):
      continue
    m = 1
    while (m < size):
      if (len(graph[graph[i][m] - 1]) == 1):
        graph[graph[i][m]] = '-'
      else:
        for num in graph[graph[i][m] - 1]:
          try:
            graph[i].index(num)
          except:
            graph[i].append(num)
            size += 1
        graph[graph[i][m] -1] = '-'
      m += 1


  rem = True

  while (rem):
    try:
      graph.remove(graph[graph.index('-')])
    except:
      rem = False

  remaining_roads = len(graph) - 1
  if remaining_roads == 0:
    print('Caso #{}: a promessa foi cumprida'.format(str(index+1)))
  else:
    print('Caso #{}: ainda falta(m) {} estrada(s)'.format(str(index+1), str(remaining_roads)))


def main():
  num_cases = int(input())
  for index in range(0, num_cases):
    solve(index)


if __name__ == "__main__":
  main()
