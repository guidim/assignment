PK
     !{NQ�E��       main.py#Exercise1

days = {}

days.update({'Monday': 1, 'Tuesday': 2, "Wednesday": 3, "Thursday": 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7})
user= input("Enter a day: ")
del days[user]
user= input("Enter a day: ")
del days[user]
print(days)

#Exercise2

personel = {
  "John": {
    "Age": 25,
    "Sex": "Male"
  },
   "Lisa": {
    "Age": 28,
    "Sex": "Female"
  },
   "Linda": {
    "Age": 32,
    "Sex": "Female",
    "Child": {
      "Susan": {
        "Age": 6,
        "Sex": "Female"
        }
      }
  },
   "Michael": {
    "Age": 41,
    "Sex": "Male",
    "Child": {
      "Karen": {
        "Age": 12,
        "Sex": "Female",
      "Greg": {
        "Age": 7,
        "Sex": "Male",
      }
    }
  }
}
}
print(personel)

#Exercise6

print(personel["Michael"]["Child"])PK 
     !{NQ�E��                     main.pyPK      5   2    