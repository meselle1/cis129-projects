# define available courses using a dictionary with course codes as keys and nested dictionaries for course details
courses = {
    'MON101': {'name': 'Introduction to Scaring', 'time': 'Monday 9:00 AM - 10:30 AM'},
    'MON201': {'name': 'Advanced Scaring Techniques', 'time': 'Tuesday 10:00 AM - 11:30 AM'},
    'MON301': {'name': 'Monster Psychology', 'time': 'Wednesday 1:00 PM - 2:30 PM'},
    'MON401': {'name': 'Scream Science 101', 'time': 'Thursday 3:00 PM - 4:30 PM'},
    'MON501': {'name': 'Monster Leadership', 'time': 'Friday 8:00 AM - 9:30 AM'},
    'ART101': {'name': 'Art of Monster Design', 'time': 'Monday 2:00 PM - 3:30 PM'},
    'ART201': {'name': 'Advanced Art of Monster Design', 'time': 'Tuesday 4:00 PM - 5:30 PM'},
    'BIO101': {'name': 'Monster Biology', 'time': 'Wednesday 10:00 AM - 11:30 AM'},
    'BIO201': {'name': 'Mutations and Monster Anatomy', 'time': 'Thursday 9:00 AM - 10:30 AM'},
    'ENG101': {'name': 'Monster Communication 101', 'time': 'Friday 11:00 AM - 12:30 PM'},
    'ENG201': {'name': 'Advanced Monster Linguistics', 'time': 'Monday 4:00 PM - 5:30 PM'},
    'MATH101': {'name': 'Mathematics of Fright', 'time': 'Tuesday 8:00 AM - 9:30 AM'},
    'PHYS101': {'name': 'Physics of Scream Energy', 'time': 'Wednesday 3:00 PM - 4:30 PM'},
    'CHEM101': {'name': 'Chemistry of Fear', 'time': 'Thursday 1:00 PM - 2:30 PM'},
    'HIST101': {'name': 'History of Monsters: Origins', 'time': 'Friday 2:00 PM - 3:30 PM'},
    'HIST201': {'name': 'Modern Monsters and Mythology', 'time': 'Monday 10:00 AM - 11:30 AM'},
    'PSY101': {'name': 'Psychology of Scaring', 'time': 'Tuesday 1:00 PM - 2:30 PM'},
    'PSY201': {'name': 'Scare Tactics and Mind Games', 'time': 'Wednesday 9:00 AM - 10:30 AM'},
    'CS101': {'name': 'Monster Technology and Gadgets', 'time': 'Thursday 10:00 AM - 11:30 AM'},
    'CS201': {'name': 'Monster Robotics and Automation', 'time': 'Friday 1:00 PM - 2:30 PM'}
}

# store registered students in a dictionary 
student_registration = {}

def display_courses():
    print("Available Courses:")
    for code, details in courses.items():
        print(f"{code}: {details['name']} ({details['time']})")

def register_courses(student_name):
    registered_courses = []
    
    # If the student is already in the registration dictionary, use their current courses
    if student_name in student_registration:
        registered_courses = student_registration[student_name]

    while True:
        print("\nEnter the course code you want to register for (or type 'done' to finish):")
        course_code = input().upper()  # converting input to uppercase to avoid case sensitivity
        
        if course_code == 'DONE':
            break
        elif course_code in courses:
            # Check if the student is already registered for the course
            if courses[course_code]['name'] in registered_courses:
                print(f"You are already registered for {courses[course_code]['name']}. Please choose a different course.")
            else:
                registered_courses.append(courses[course_code]['name'])
                print(f"Successfully registered for {courses[course_code]['name']} ({courses[course_code]['time']})")
        else:
            print("Invalid course code. Please try again.")
    
    student_registration[student_name] = registered_courses
    print(f"\n{student_name} has successfully registered for the following courses:")
    for course in registered_courses:
        print(course)

def main():
    print("Welcome to Monsters University!")
    
    student_name = input("Enter your name: ")

    display_courses()

    register_courses(student_name)

    print(f"\nFinal registration list for {student_name}:")
    for course in student_registration[student_name]:
        print(course)
       

if __name__ == "__main__":
    main()

print('Have a fearful semester!')
