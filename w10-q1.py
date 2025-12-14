import sqlite3

def createDatabase(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS RESEARCHER("
              "orcidid TEXT PRIMARY KEY,"
              "firstname TEXT,"
              "lastname TEXT,"
              "university TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS PROJECT("
              "projectid INTEGER PRIMARY KEY,"
              "projectname TEXT,"
              "budget INTEGER,"
              "startyear INTEGER,"
              "finishyear INTEGER)")

    c.execute("CREATE TABLE IF NOT EXISTS WORK("
              "orcidid TEXT,"
              "projectid INTEGER,"
              "roles TEXT,"
              "FOREIGN KEY (orcidid) REFERENCES RESEARCHER(orcidid),"
              "FOREIGN KEY (projectid) REFERENCES PROJECT(projectid),"
              "PRIMARY KEY (orcidid, projectid, roles))")

    conn.close()

def insertRecords(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    researchers = [
        ("0000-1111-2222-3333", "James",  "Smith",  "Manchester University"),
        ("4444-5555-6666-7777", "Robert", "Jones",  "Wolverhampton University"),
        ("1111-1111-2222-3333", "John",   "Taylor", "Manchester University"),
        ("4444-4444-6666-7777", "David",  "Evans",  "Middlesex University")
    ]
    c.executemany("INSERT INTO RESEARCHER VALUES(?,?,?,?)", researchers)

    projects = [
        (1, "Educational Data Mining", 2020, 2021, 50000),
        (2, "Medical Informatics",     2021, 2022, 150000)
    ]
    c.executemany("INSERT INTO PROJECT VALUES(?,?,?,?,?)", projects)

    works = [
        ("0000-1111-2222-3333", 1, "Data Scientist"),
        ("0000-1111-2222-3333", 2, "Data Scientist"),
        ("1111-1111-2222-3333", 2, "Medical Doctor"),
        ("4444-4444-6666-7777", 1, "Education Specialist"),
        ("4444-5555-6666-7777", 1, "Programmer")
    ]
    c.executemany("INSERT INTO WORK VALUES(?,?,?)", works)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    dbname = input("Enter the database file name: ")
    #createDatabase(dbname)
    #insertRecords(dbname)

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    #1. Show the researchers with their details who are working in a given project. The project id will be taken from the user.
    """
    pid = input("Enter project id: ")
    c.execute("SELECT r.OrcidID, r.FirstName, r.LastName, r.University, w.Roles "
              "FROM RESEARCHER r, WORK w "
              "WHERE r.OrcidID = w.OrcidID AND w.ProjectID = ?", (pid,))
    row = c.fetchone()
    while row != None:
        print("Orcid:", row[0], "| Name:", row[1], row[2], "| Uni:", row[3], "| Role:", row[4])
        row = c.fetchone()
    """

    #2. Show the number of researchers in each project
    """
    c.execute("SELECT p.ProjectID, p.ProjectName, COUNT(DISTINCT w.OrcidID) "
              "FROM PROJECT p LEFT JOIN WORK w ON p.ProjectID = w.ProjectID "
              "GROUP BY p.ProjectID, p.ProjectName")
    row = c.fetchone()
    while row != None:
        print("Project: ", row[0], row[1], "| Researcher Count: ", row[2])
        row = c.fetchone()
    """
    # 3. Show the names of the researchers who are participating in a project with a budget greater than
    # 100000 and from Manchester University.
    """
    c.execute("SELECT DISTINCT r.FirstName, r.LastName "
              "FROM RESEARCHER r, WORK w, PROJECT p "
              "WHERE r.OrcidID = w.OrcidID AND p.ProjectID = w.ProjectID "
              "AND p.Budget > 100000 AND r.University = 'Manchester University'")
    row = c.fetchone()
    while row != None:
        print("Researcher:", row[0], row[1])
        row = c.fetchone()
    """
    # 4. Show the projects with a researcher whose role is Programmer.
    """
    c.execute("SELECT DISTINCT p.ProjectID, p.ProjectName "
              "FROM PROJECT p, WORK w "
              "WHERE p.ProjectID = w.ProjectID AND w.Roles = 'Programmer'")
    row = c.fetchone()
    while row != None:
        print("Project: ", row[0], row[1])
        row = c.fetchone()
    """



