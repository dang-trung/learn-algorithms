def tower_hanoi(n, source, target, spare):
    if n == 1:
        print(f"Move disk {n} from {source} to {target}.")
    else:
        tower_hanoi(n-1, source, spare, target)
        print(f"Move disk {n} from {source} to {target}.")
        tower_hanoi(n-1, spare, target, source)

if __name__ == '__main__':
    tower_hanoi(3, 'A', 'C', 'B')