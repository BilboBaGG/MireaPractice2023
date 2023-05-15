from database.functions import ORM

if __name__ == "__main__":
    db = ORM()

    db.CreateTable()

    db.AddStudent("Mikhail", "BISO-01-22")
    print("Mikhail's group is :", db.GetStudent("Mikhail").group)
    db.UpdateStudentGroup("Mikhail", "BISO-02-22")
    print("Mikhail's group is :", db.GetStudent("Mikhail").group)
