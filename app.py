import os
import pickle

# --- Modification Functions ---

def modify_book(x):
    """Searches for a book by ID and allows the user to update details."""
    if not os.path.exists("book.dat"):
        print("\n\t\tFile not found")
        return

    books = []
    found = False
    with open("book.dat", "rb") as f:
        while True:
            try:
                bk = pickle.load(f)
                if bk.bno == x:
                    print("\n\t\tRecord Found! Enter new details:")
                    bk.create_b() # Input new details
                    found = True
                books.append(bk)
            except EOFError:
                break
    
    if found:
        with open("book.dat", "wb") as f:
            for b in books:
                pickle.dump(b, f)
        print("\n\t\tRecord Updated Successfully")
    else:
        print("\n\t\tNo such record exists")

def modify_student(x):
    """Searches for a student by Admission No and updates details."""
    if not os.path.exists("student.dat"):
        print("\n\t\tFile not found")
        return

    students = []
    found = False
    with open("student.dat", "rb") as f:
        while True:
            try:
                st = pickle.load(f)
                if st.admno == x:
                    print("\n\t\tRecord Found! Enter new details:")
                    st.create_s()
                    found = True
                students.append(st)
            except EOFError:
                break

    if found:
        with open("student.dat", "wb") as f:
            for s in students:
                pickle.dump(s, f)
        print("\n\t\tRecord Updated Successfully")
    else:
        print("\n\t\tNo such record exists")

# --- Deletion Functions ---

def delete_student(x):
    """Removes a student record from the binary file."""
    if not os.path.exists("student.dat"):
        print("\n\t\tFile not found")
        return

    students = []
    found = False
    with open("student.dat", "rb") as f:
        while True:
            try:
                st = pickle.load(f)
                if st.admno == x:
                    found = True
                    continue # Skip this record to "delete" it
                students.append(st)
            except EOFError:
                break

    if found:
        with open("student.dat", "wb") as f:
            for s in students:
                pickle.dump(s, f)
        print("\n\t\tRecord deleted successfully")
    else:
        print("\n\t\tNo such record exists")

def delete_book(x):
    """Removes a book record from the binary file."""
    if not os.path.exists("book.dat"):
        print("\n\t\tFile not found")
        return

    books = []
    found = False
    with open("book.dat", "rb") as f:
        while True:
            try:
                bk = pickle.load(f)
                if bk.bno == x:
                    found = True
                    continue # Skip this record to "delete" it
                books.append(bk)
            except EOFError:
                break

    if found:
        with open("book.dat", "wb") as f:
            for b in books:
                pickle.dump(b, f)
        print("\n\t\tRecord deleted successfully")
    else:
        print("\n\t\tNo such record exists")
