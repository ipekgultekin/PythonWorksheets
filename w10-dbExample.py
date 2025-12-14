import sqlite3


def createDatabase(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS STUDENT("
              "stdID INTEGER PRIMARY KEY,"
              "stdName TEXT,"
              "major TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS COURSE("
              "courseCode TEXT PRIMARY KEY,"
              "courseName TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS STUDENTCOURSE("
              "stdID INTEGER,"
              "courseCode TEXT,"
              "grade TEXT,"
              "semester INTEGER,"
              "FOREIGN KEY (stdID) REFERENCES STUDENT(stdID),"
              "FOREIGN KEY (courseCode) REFERENCES COURSE(courseCode),"
              "PRIMARY KEY (stdID, courseCode, semester))")

    conn.close()


def insertRecords(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    students = [(1, "Olivia Ethan", "CNG"), (2, "William Harper", "CNG"), (3, "Sophia Ball", "SNG")]
    c.executemany("INSERT INTO STUDENT VALUES(?, ?, ?)", students)

    courses = [("CNG140", "C Programming"), ("CNG213", "Data Structures"), ("CNG315", "Algorithms")]
    c.executemany("INSERT INTO COURSE VALUES(?,?)", courses)

    studentcourses = [(1, "CNG140", 20192, "AA"), (2, "CNG140", 20192, "BB"), (2, "CNG213", 20201, "CC")]
    c.executemany("INSERT INTO STUDENTCOURSE(stdID, courseCode, semester, grade) VALUES(?,?,?,?)", studentcourses)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    dbname = input("Enter the database file name: ")
    # createDatabase(dbname)
    # insertRecords(dbname)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    # Print the names of the students who took CNG140 in 20192
    """
    c.execute("SELECT stdName FROM STUDENT s, STUDENTCOURSE sc WHERE s.stdID = sc.stdID AND courseCode = 'CNG140' AND semester = 20192")
    row = c.fetchone()
    while row != None:
        print("Student Name: ", row[0])
        row = c.fetchone()

    rows = c.fetchall()
    print(rows)
    """

    # Print the history of the courses for a given student
    """
    stdID = input("Enter student ID number: ")
    c.execute("SELECT stdID, courseCode, semester, grade FROM STUDENTCOURSE WHERE stdID = ?", (stdID,))
    row = c.fetchone()
    print("ID No\tCourse\tSemester\tGrade")
    while row != None:
        print(str(row[0]) + "\t" + row[1] + "\t" + str(row[2]) + "\t" + row[3])
        row = c.fetchone()
    """

    # Print the courses order by name
    """
    c.execute("SELECT * FROM COURSE ORDER BY courseName DESC")
    row = c.fetchone()
    while row != None:
        print(row)
        row = c.fetchone()
    """

    # Print the number of students for each department
    """
    c.execute("SELECT major, COUNT(*) FROM STUDENT GROUP BY major")
    row = c.fetchone()
    while row != None:
        print(row)
        row = c.fetchone()
    """

    # Print the number of students for each department with at least two students
    """"
    c.execute("SELECT major, COUNT(*) FROM STUDENT GROUP BY major HAVING COUNT(*) > 1")
    row = c.fetchone()
    while row != None:
        print(row)
        row = c.fetchone()
    """

    # Print the courses whose name is taken from the user
    """
    name = input("Enter course name: ")
    c.execute("SELECT courseName FROM COURSE WHERE courseName LIKE '%{}%'".format(name))
    row = c.fetchone()
    while row != None:
        print(row)
        row = c.fetchone()

    """

    c.execute(
        "SELECT s.stdID, stdName, c.courseCode, courseName, grade, semester FROM COURSE c, STUDENT s, STUDENTCOURSE sc WHERE s.stdID = sc.stdID AND c.courseCode = sc.courseCode AND c.courseCode='CNG140'")
    row = c.fetchone()
    while row != None:
        print(row)
        row = c.fetchone()

    conn.close()