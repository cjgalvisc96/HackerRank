set_a, set_b = [set(input().split()) for _ in range(4)][1::2]
print('\n'.join(sorted(set_a ^ set_b, key=int)))

