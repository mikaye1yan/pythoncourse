student1 = { "name": "John", "notes": [3, 5, 4] }
student2 = { "name": "Max", "notes": [1, 4, 6] }
student3 = { "name": "Zygmund", "notes": [1, 2, 3] }
top_note1 = {"name": student1["name"], "top_note": max(student1["notes"])}
top_note2 = {"name": student2["name"], "top_note": max(student2["notes"])}
top_note3 = {"name": student3["name"], "top_note": max(student3["notes"])}
print(top_note1)
print(top_note2)
print(top_note3)