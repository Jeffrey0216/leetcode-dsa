from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter
        start = None
        litter = {}
        count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = count
                    count += 1

        # No litter
        if count == 0:
            return 0

        # All bits = 1
        target = (1 << count) - 1

        # row, col, energy, mask, moves
        queue = deque()
        queue.append((start[0], start[1], energy, 0, 0))

        visited = set()
        visited.add((start[0], start[1], energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()

            # All litter collected
            if mask == target:
                return moves

            # Cannot move anymore
            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                new_energy = curr_energy - 1

                # Reset area
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Update litter mask
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)

                state = (nr, nc, new_energy, new_mask)

                if state in visited:
                    continue

                visited.add(state)

                queue.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1
        