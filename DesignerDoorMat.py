"""
# Cris
N, M = map(int, input().split())
char_1 = '.|.'
char_2 = '-'
text = 'WELCOME'
# Top
for i in range(N//2):
    print(('.|.'*(2*i + 1)).center(M, '-'))

# Center
print(text.center(M, char_2))

# Bottom
for i in range((N//2)-1, -1, -1):
    print(('.|.'*(2*i + 1)).center(M, '-'))
"""
# Teso
n, m = map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))