class Solution:

    def dfs(self, course, courseMap, academicPath):
        # print(f"DFS call: course: {course} academicPath: {academicPath}")
        if course not in courseMap:
            # print(f"No prereq for course {course} it can be completed")
            return True
        
        # print(f"AcademicPath: {academicPath}")
        if course in academicPath:
            # print(f"Course: {course} already in academicPath: {academicPath}")
            return False
        
        if courseMap[course] == []:
            return True
        
        children = courseMap[course]
        academicPath.append(course)
        for child in children:
            # print(f"AP: {academicPath}")
            result = self.dfs(child, courseMap, academicPath)
            if result == False:
                # print(f"Course cannot be completed: {child}")
                return False
        # print(f"Removing the course since it can completed: {course}")
        academicPath.remove(course)
        # If the course can be completed then remember it by removing it's children
        courseMap[course] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {}
        for course in prerequisites:
            first = course[0]
            second = course[1]
            if first in courseMap:
                courseMap[first].append(second)
            else:
                courseMap[first] = [second]
        
        # print(f"CourseMap {courseMap}")

        for key,val in courseMap.items():
            result = self.dfs(key, courseMap, [])
            if result == False:
                return False

        
        return True
        