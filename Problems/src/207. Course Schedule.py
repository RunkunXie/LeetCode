from typing import List
from itertools import compress
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # find course withour prerequisites, O(E)
        learned_course = [True] * numCourses
        prereq_graph = [[0] * numCourses for _ in range(numCourses)]

        for p in prerequisites:
            learned_course[p[0]] = False
            prereq_graph[p[0]][p[1]] = 1

        num_finished = sum(learned_course)
        if num_finished is 0:
            return False

        # find if we can learn new courses from current course, O(V^2)
        learning = True
        while learning == True:
            learning = False

            # for each course
            for i in range(numCourses):

                # if not learned
                if learned_course[i] == False:

                    # if all prerequisites are learned
                    if all(compress(learned_course, prereq_graph[i])):
                        learned_course[i] = True
                        num_finished += 1
                        learning = True

            if num_finished == numCourses:
                return True

            if learning == False:
                return False


