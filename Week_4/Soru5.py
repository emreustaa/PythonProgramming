student_details= [
  {'id': 1, 'subject': 'math', 'Midterm': 70, 'Final': 82},
  {'id': 2, 'subject': 'math', 'Midterm': 73, 'Final': 74},
  {'id': 3, 'subject': 'math', 'Midterm': 75, 'Final': 86}
]

av = sum([sum([student['Midterm'], student['Final']])/2 for student in student_details])/len(student_details)
print(average)