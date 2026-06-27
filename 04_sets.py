cs_courses = {"statics","math","physics","compscience"}
art_courses = {"math","socialScience","polity"}

print("math" in cs_courses)

# INTERSECTION
print(cs_courses.intersection(art_courses))

#DIFFERENCE
print(cs_courses.difference(art_courses))

#UNION
print(cs_courses.union(art_courses))
