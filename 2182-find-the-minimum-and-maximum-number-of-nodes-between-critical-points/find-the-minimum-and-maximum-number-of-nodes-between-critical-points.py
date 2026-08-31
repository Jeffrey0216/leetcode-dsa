class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        first = -1
        last = -1
        min_dist = float('inf')
        index = 1

        while curr.next:
            next_node = curr.next

            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = next_node
            index += 1

        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]