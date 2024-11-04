test_grades = {
    "Harsha" : "A",
    "Havisha" : "A",
    "Ryan" : "A",
    3 : 95.2
}

print( test_grades["Harsha"] )
print( test_grades.get("Ryan", "No Student Found") )
print( test_grades[3] )
