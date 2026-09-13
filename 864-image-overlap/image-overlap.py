class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_points, img2_points = [], []
        d = defaultdict(int)

        n = len(img1)
        for r in range(n):
            for c in range(n):
                if img1[r][c]:
                    img1_points.append((r, c))
                if img2[r][c]:
                    img2_points.append((r, c))

        for r_1, c_1, in img1_points:
            for r_2, c_2 in img2_points:
                d[(r_2 - r_1, c_2 - c_1)] += 1

        return max(d.values() or [0])