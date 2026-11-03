class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.__marks = marks

    def display(self):
        print("\nRoll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.__marks)

    def update_marks(self, marks):
        self.__marks = marks
        print("Marks updated successfully!")

    def calculate_average(self):
        return sum(self.__marks) / len(self.__marks)

    def get_marks(self):
        return self.__marks


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll_no = input("Enter Roll Number: ")

        if self.search_student(roll_no, show=False):
            print("Student already exists!")
            return

        name = input("Enter Student Name: ")

        try:
            marks = list(map(float, input(
                "Enter marks in 3 subjects: "
            ).split()))

            if len(marks) != 3 or any(
                mark < 0 or mark > 100 for mark in marks
            ):
                print("Enter exactly 3 marks between 0 and 100.")
                return

        except ValueError:
            print("Please enter valid numeric marks.")
            return

        student = Student(roll_no, name, marks)
        self.students.append(student)

        print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            student.display()
            print("Average Marks:", round(
                student.calculate_average(), 2
            ))

    def search_student(self, roll_no=None, show=True):
        if roll_no is None:
            roll_no = input("Enter Roll Number to search: ")

        for student in self.students:
            if student.roll_no == roll_no:
                if show:
                    student.display()
                return student

        if show:
            print("Student not found!")

        return None

    def update_student(self):
        roll_no = input("Enter Roll Number: ")
        student = self.search_student(roll_no, show=False)

        if student:
            try:
                marks = list(map(float, input(
                    "Enter new marks in 3 subjects: "
                ).split()))

                if len(marks) != 3 or any(
                    mark < 0 or mark > 100 for mark in marks
                ):
                    print("Enter exactly 3 marks between 0 and 100.")
                    return

                student.update_marks(marks)

            except ValueError:
                print("Please enter valid numeric marks.")
        else:
            print("Student not found!")

    def delete_student(self):
        roll_no = input("Enter Roll Number to delete: ")

        student = self.search_student(roll_no, show=False)

        if student:
            self.students.remove(student)
            print("Student deleted successfully!")
        else:
            print("Student not found!")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.display_students()

        elif choice == "3":
            system.search_student()

        elif choice == "4":
            system.update_student()

        elif choice == "5":
            system.delete_student()

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
