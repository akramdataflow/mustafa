import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.models import Currency
from main.models import Category, Course, Lesson, Review, Teacher, Student



class Command(BaseCommand):
    help = 'Create sample data'

    def handle(self, *args, **options):
        if not Currency.objects.count():
            Currency.objects.bulk_create([
                Currency(name='United States Dollar', code='USD', code3='USD', symbol='$', order=1),
                Currency(name='Iraqi Dinar', code='IQD', code3='IQD', symbol='د.ع', order=2),
                Currency(name='Saudi Riyal', code='SAR', code3='SAR', symbol='ر.س', order=3),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample currencies'))

        if not User.objects.count():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            # create teachers
            User.objects.create_user('teacher1', 'teacher1@example.com', 'teacher111111')
            User.objects.create_user('teacher2', 'teacher2@example.com', 'teacher211111')
            User.objects.create_user('teacher3', 'teacher3@example.com', 'teacher311111')
            # create studens
            User.objects.create_user(username='student1', email='student1@example.com', password='student111111')
            User.objects.create_user(username='student2', email='student2@example.com', password='student211111')
            User.objects.create_user(username='student3', email='student3@example.com', password='student311111')
            User.objects.create_user(username='student4', email='student4@example.com', password='student411111')
            User.objects.create_user(username='student5', email='student5@example.com', password='student511111')
            User.objects.create_user(username='student6', email='student6@example.com', password='student611111')
            User.objects.create_user(username='student7', email='student7@example.com', password='student711111')
            User.objects.create_user(username='student8', email='student8@example.com', password='student811111')
            User.objects.create_user(username='student9', email='student9@example.com', password='student911111')
            User.objects.create_user(username='student10', email='student10@example.com', password='student1011111')
            User.objects.create_user(username='student11', email='student11@example.com', password='student1111111')
            User.objects.create_user(username='student12', email='student12@example.com', password='student1211111')
            User.objects.create_user(username='student13', email='student13@example.com', password='student1311111')
            User.objects.create_user(username='student14', email='student14@example.com', password='student1411111')
            User.objects.create_user(username='student15', email='student15@example.com', password='student1511111')
            User.objects.create_user(username='student16', email='student16@example.com', password='student1611111')
            User.objects.create_user(username='student17', email='student17@example.com', password='student1711111')
            User.objects.create_user(username='student18', email='student18@example.com', password='student1811111')
            User.objects.create_user(username='student19', email='student19@example.com', password='student1911111')
            User.objects.create_user(username='student20', email='student20@example.com', password='student2011111')

            self.stdout.write(self.style.SUCCESS('Successfully created sample users'))

        if not Category.objects.count():
            Category.objects.bulk_create([
                Category(name='Development', slug='development'),
                Category(name='Business', slug='business'),
                Category(name='Design', slug='design'),
                Category(name='Marketing', slug='marketing'),
                Category(name='IT and Software', slug='it-and-software'),
                Category(name='Personal Development', slug='personal-development'),
                Category(name='Health and Fitness', slug='health-and-fitness'),
                Category(name='Photography', slug='photography'),
                Category(name='Music', slug='music'),
                Category(name='Teaching', slug='teaching'),
                Category(name='Language Learning', slug='language-learning'),
                Category(name='Cooking', slug='cooking'),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample categories'))

        if not Teacher.objects.count():
            Teacher.objects.bulk_create([
                Teacher(name='Richard Hendricks', email='teacher1@mit.edu.co.uk', user=User.objects.get(username='teacher1')),
                Teacher(name='Mathieu Zanardini', email='teacher2@mit.edu.co.uk', user=User.objects.get(username='teacher2')),
                Teacher(name='Erik Brynroflsson', email='teacher3@mit.edu.co.uk', user=User.objects.get(username='teacher3')),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample teachers'))

        if not Student.objects.count():
            Student.objects.bulk_create([
                Student(name='Johnathan Gates', email='student1@example.com', user=User.objects.get(username='student1')),
                Student(name='Miragh Alhassan', email='student2@example.com', user=User.objects.get(username='student2')),
                Student(name='Stevan Lopez', email='student3@example.com', user=User.objects.get(username='student3')),
                Student(name='Christopher Nolan', email='student4@example.com', user=User.objects.get(username='student4')),
                Student(name='Neil Harbour', email='student5@example.com', user=User.objects.get(username='student5')),
                Student(name='Mark Lee', email='student6@example.com', user=User.objects.get(username='student6')),
                Student(name='Nathan Smith', email='student7@example.com', user=User.objects.get(username='student7')),
                Student(name='William Henry', email='student8@example.com', user=User.objects.get(username='student8')),
                Student(name='Karthik Kumar', email='student9@example.com', user=User.objects.get(username='student9')),
                Student(name='Eric Ries', email='student10@example.com', user=User.objects.get(username='student10')),
                Student(name='Sundar Pichai', email='student11@example.com', user=User.objects.get(username='student11')),
                Student(name='Manapreet Singh', email='student12@example.com', user=User.objects.get(username='student12')),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample students'))

        if not Course.objects.count():
            Course.objects.bulk_create([
                Course(
                    name='Introduction to Python', 
                    body='Python is the most popular programming language', 
                    image=os.path.join('images', 'course', 'python.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                ),
                Course(
                    name='Introduction to Django', 
                    body='Django is the most popular web framework', 
                    image=os.path.join('images', 'course', 'django.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                ),
                Course(
                    name='Introduction to React', 
                    body='React is the most popular frontend framework', 
                    image=os.path.join('images', 'course', 'react.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                ),
            ])
            # set teachers m2m field
            Course.objects.get(name='Introduction to Python').teachers.add(Teacher.objects.get(user__username='teacher1'))
            Course.objects.get(name='Introduction to Django').teachers.add(Teacher.objects.get(user__username='teacher2'))
            Course.objects.get(name='Introduction to React').teachers.add(Teacher.objects.get(user__username='teacher3'))

            self.stdout.write(self.style.SUCCESS('Successfully created sample courses'))

        if not Lesson.objects.count():
            # create lessons for python course
            course1 = Course.objects.get(name='Introduction to Python')
            Lesson.objects.bulk_create([
                Lesson(name='Installing Python', url="https://www.python.org/downloads/", order=1, course=course1),
                Lesson(name='Variables and Data Types', url="https://youtu.be/LKFrQXaoSMQ", order=2, course=course1),
                Lesson(name='Control Flow', url="https://www.youtube.com/watch?v=Zp5MuPOtsSY", order=3, course=course1),
                Lesson(name='Functions', url="https://www.youtube.com/watch?v=89cGQjB5R4M", order=4, course=course1),
                Lesson(name='Lists', url="https://www.youtube.com/watch?v=9OeznAkyQz4", order=5, course=course1),
                Lesson(name='Dictionaries', url="https://www.youtube.com/watch?v=MZZSMaEAC2g", order=6, course=course1),
                Lesson(name='Tuples', url="https://www.youtube.com/watch?v=w6hL_dszMxk", order=7, course=course1),
                Lesson(name='Sets', url="https://www.youtube.com/watch?v=t9j8lCUGZXo", order=8, course=course1),
                Lesson(name='Loops', url="https://www.youtube.com/watch?v=94UHCEmprCY", order=9, course=course1),
                Lesson(name='Modules', url="https://www.youtube.com/watch?v=XcfxkHrHTVE", order=10, course=course1),
                Lesson(name='Classes', url="https://www.youtube.com/watch?v=g-qRKZD3FgE", order=11, course=course1),
                Lesson(name='Exceptions', url="https://www.youtube.com/watch?v=j_q6NGOwDJo", order=12, course=course1),
                Lesson(name='File I/O', url="https://www.youtube.com/watch?v=LpZmZs2_BC4", order=13, course=course1),
                Lesson(name='Object-Oriented Programming', url="https://www.youtube.com/watch?v=q2SGW2VgwAM", order=14, course=course1),
                Lesson(name='Regular Expressions', url="https://www.youtube.com/watch?v=nxjwB8up2gI", order=15, course=course1),
                Lesson(name='Generators', url="https://www.youtube.com/watch?v=gMompY5MyPg", order=16, course=course1),
                Lesson(name='Decorators', url="https://www.youtube.com/watch?v=U-G-mSd4KAE", order=17, course=course1),
                Lesson(name='Multithreading', url="https://www.youtube.com/watch?v=STEOavXqXkQ", order=18, course=course1),
                Lesson(name='Asynchronous Programming', url="https://www.youtube.com/watch?v=K56nNuBEd0c", order=19, course=course1),
                Lesson(name='Testing', url="https://www.youtube.com/watch?v=1Lfv5tUGsn8", order=20, course=course1),
                Lesson(name='Debugging', url="https://www.youtube.com/watch?v=bHx8A8tbj2c", order=21, course=course1),
                Lesson(name='Deployment', url="https://www.youtube.com/watch?v=Ehhs8czHDNY", order=22, course=course1),
            ])

            # create lessons for django course
            course2 = Course.objects.get(name='Introduction to Django')
            Lesson.objects.bulk_create([
                Lesson(name='Installing Django', url='https://www.youtube.com/watch?v=rHux0gMZ3Eg', order=1, course=course2),
                Lesson(name='Models', url='https://www.youtube.com/watch?v=rI95wyHD_6k', order=2, course=course2),
                Lesson(name='Views', url='https://www.youtube.com/watch?v=RE0HlKch_3U', order=3, course=course2),
                Lesson(name='Templates', url='https://www.youtube.com/watch?v=GNlIe5zvBeQ', order=4, course=course2),
                Lesson(name='Forms', url='https://www.youtube.com/watch?v=4pSPWkrd-1M', order=5, course=course2),
                Lesson(name='Authentication', url='https://www.youtube.com/watch?v=tUqUdu0Sjyc', order=6, course=course2),
                Lesson(name='APIs', url='https://www.youtube.com/watch?v=cJveiktaOSQ&t=1s', order=7, course=course2),
                Lesson(name='Testing', url='https://www.youtube.com/watch?v=bIFVweK0hMc', order=8, course=course2),
                Lesson(name='Deployment', url='https://www.youtube.com/watch?v=IoxHUrbiqUo', order=9, course=course2),
            ])

            # create lessons for react course
            course3 = Course.objects.get(name='Introduction to React')
            Lesson.objects.bulk_create([
                Lesson(name='Installing React', url='https://www.youtube.com/watch?v=yOAZDymGWVw', order=1, course=course3),
                Lesson(name='Components', url='https://www.youtube.com/watch?v=Y2hgEGPzTZY', order=2, course=course3),
                Lesson(name='Props', url='https://www.youtube.com/watch?v=uvEAvxWvwOs', order=3, course=course3),
                Lesson(name='State', url='https://www.youtube.com/watch?v=O6P86uwfdR0', order=4, course=course3),
                Lesson(name='Events', url='https://www.youtube.com/watch?v=lE31_0cXeAg', order=5, course=course3),
                Lesson(name='Forms', url='https://www.youtube.com/watch?v=cc_xmawJ8Kg', order=6, course=course3),
                Lesson(name='APIs', url='https://www.youtube.com/watch?v=00lxm_doFYw', order=7, course=course3),
                Lesson(name='Testing', url='https://www.youtube.com/watch?v=8Xwq35cPwYg', order=8, course=course3),
                Lesson(name='Deployment', url='https://www.youtube.com/watch?v=KFwFDZpEzXY', order=9, course=course3),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample lessons'))

            if not Review.objects.exists():
                Review.objects.bulk_create([
                    Review(body='This course was a great introduction to Python.', rating=5, course=course1, user_id=1),
                    Review(body='I learned a lot from python course.', rating=4, course=course1, user_id=2),
                    Review(body='The instructor well explained the concepts.', rating=4, course=course1, user_id=3),
                    Review(body='I enjoyed the interactive examples.', rating=4, course=course1, user_id=4),
                    Review(body='The course was well-organized and easy to follow.', rating=4, course=course1, user_id=5),
                    Review(body='This course was a great introduction to Django.', rating=5, course=course2, user_id=6),
                    Review(body='I learned a lot from this course and I enjoyed it.', rating=4, course=course2, user_id=7),
                    Review(body='The instructor has a good understanding of Django.', rating=4, course=course2, user_id=8),
                    Review(body='I enjoyed the content of the course.', rating=4, course=course2, user_id=9),
                    Review(body='The course was well-organized and simple.', rating=4, course=course2, user_id=10),
                    Review(body='This course was a great introduction to React.', rating=5, course=course3, user_id=11),
                    Review(body='I learned a lot from this course.', rating=4, course=course3, user_id=12),
                    Review(body='The instructor was very knowledgeable.', rating=4, course=course3, user_id=1),
                    Review(body='I enjoyed the interactive exercises.', rating=4, course=course3, user_id=2),
                    Review(body='The course was well-organized.', rating=4, course=course3, user_id=3),
                    Review(body='This course was a great introduction to JavaScript.', rating=5, course=course3, user_id=4),
                    Review(body='I learned a lot from this course.', rating=4, course=course3, user_id=5),
                    Review(body='The instructor was very knowledgeable.', rating=4, course=course3, user_id=6),
                    Review(body='I enjoyed the interactive exercises.', rating=4, course=course3, user_id=7),
                    Review(body='The course was well-organized.', rating=4, course=course3, user_id=8),
                ])
                self.stdout.write(self.style.SUCCESS('Successfully created sample reviews'))