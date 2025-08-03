#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

from collections import defaultdict, deque

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build an adjacency list where graph[src] contains all courses that depend on src
        graph = defaultdict(list)
        # in_degree[i] counts how many prerequisites course i has
        in_degree = [0] * numCourses

        # Populate graph and in-degree array
        # {
        #     0: [1, 2],  # from course 0 you can go to courses 1 and 2
        #     1: [3],     # from course 1 you can go to course 3
        #     2: [3],     # from course 2 you can go to course 3
        #     # course 3 doesn’t appear as a key because nothing depends on 3
        # }
        for dest, src in prerequisites:
            graph[src].append(dest)    # there is a directed edge src → dest
            in_degree[dest] += 1       # dest has one more prerequisite

        # Start with all courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Counter for number of courses with no remaining prerequisites aka number of courses we can take
        count = 0
        while queue:
            # Pop a course with no remaining prerequisites aka in_degree 0
            course = queue.popleft()
            count += 1

            # "Remove" this course by reducing in-degree of its dependents
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If a dependent course now has no prerequisites, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we've taken all courses, there was no cycle
        return count == numCourses
# @lc code=end
