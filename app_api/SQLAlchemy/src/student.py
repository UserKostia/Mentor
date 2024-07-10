from operator import or_

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Підключення до бази даних PostgreSQL
try:
    engine = create_engine("postgresql://postgres:kostia532@localhost:5432/Student", echo=False)
except Exception as e:
    print("e = ", e)


# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Базовий клас для моделей
Base = declarative_base()


# Опис моделі Student
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# Створення таблиць у базі даних
# Base.metadata.create_all(engine)


student1 = Student(name="Kostia", age=18, grade="Fifth")
student2 = Student(name="Vlad", age=25, grade="Fourth")
student3 = Student(name="Sasha", age=19, grade="Third")
student4 = Student(name="Dima", age=20, grade="Second")
session.add(student1)
session.add_all([student2, student3, student4])
session.commit()


# Get all data
print("Get all data")
students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name)


# Get data in order
print()
print("Get data in order")
students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name)


# Get data by filtering
print()
print("Get data by filtering")
# students = session.query(Student).filter(Student.name == "Dima").all()

students = session.query(Student).filter(or_(Student.name == "Dima", Student.name == "Vlad"))

for student in students:
    print(student.name)


# Count the number of results
print()
print("Count the number of results")

count_students = session.query(Student).filter(or_(Student.name == "Dima", Student.name == "Vlad")).count()

print(f"{count_students = }")


# Update data
student = session.query(Student).filter(Student.name == "Kostia").first()
student.name = "Nazar"
session.commit()

print()
print("Updated")
student = session.query(Student)

for student in students:
    print(student.name)


# Delete data
student = session.query(Student).filter(Student.name == "Nazar").first()
session.delete(student)
session.commit()
