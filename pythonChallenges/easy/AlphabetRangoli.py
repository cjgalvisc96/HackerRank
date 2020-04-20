def xx(N):
    if N == 1:
        print('a')
        return
    string = ''
    N = N
    count = ((N - 1) * 4) + 1
    matriz = []
    for i in range(ord('a') + (N - 1), ord('a') - 1, -1):
        string += chr(i) + '-'
        matriz.append((string + string[-4::-1]).center(count, '-'))
    print('\n'.join(matriz) + '\n' + '\n'.join(matriz[-2::-1]))

if __name__ == "__main__":
    n = int(input())
    xx(n)