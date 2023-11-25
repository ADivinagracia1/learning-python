# def canFinish(numCourses, prerequisites):

#     stack = [0] # everything is labeled from 0 to numCourses-1
#     taken = set()

#     while len(stack) > 0:
#         v = stack.pop()
#         taken.add(v)

#         for next_course in prerequisites[v]:
#             if next_course not in taken:
#                 stack.append(next_course)
#             else: # cycle detected
#                 return False

#         if len(taken) == numCourses:
#             return True
    
#     return False

def canFinish(numCourses, prerequisites):
    # go and think about simplest case, then check if it applies to the p

    stack = [0] # everything is labeled from 0 to numCourses-1
    taken = set()

    for course, preq in prerequisites:
        print(course, preq)
        



numCourses = 2
prerequisites = [[1,0], [0, 1]]

val = canFinish(numCourses, prerequisites)
print(val)