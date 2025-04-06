import os

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from django.utils import timezone

from core.models import Currency
from main.models import Category, Course, Lesson, Review, Teacher, Student



class Command(BaseCommand):
    help = 'Create sample data'

    def handle(self, *args, **options):
        call_command('migrate')
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
            User.objects.create_user('teacher4', 'teacher4@example.com', 'teacher411111')
            User.objects.create_user('teacher5', 'teacher5@example.com', 'teacher511111')
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
                Teacher(name='Mustafa Nail', email='teacher0@example.com', phone_number='964222222220', user=User.objects.get(username='admin')),
                Teacher(name='Richard Hendricks', email='teacher1@mit.edu.co.uk', phone_number="964222222221", user=User.objects.get(username='teacher1')),
                Teacher(name='Mathieu Zanardini', email='teacher2@mit.edu.co.uk', phone_number="964222222222", user=User.objects.get(username='teacher2')),
                Teacher(name='Erik Brynroflsson', email='teacher3@mit.edu.co.uk', phone_number="964222222223", user=User.objects.get(username='teacher3')),
                Teacher(name='Gustavo Grinberg', email='teacher4@mit.edu.co.uk', phone_number="964222222224", user=User.objects.get(username='teacher4')),
                Teacher(name='Nathan Yaugen Henry', email='teacher5@mit.edu.co.uk', phone_number="964222222225", user=User.objects.get(username='teacher5')),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample teachers'))

        if not Student.objects.count():
            Student.objects.bulk_create([
                Student(name='Mustafa Nail', email='student0@example.com', phone_number='964111111110', user=User.objects.get(username='admin'), birth_date='2000-01-01'),
                Student(name='Johnathan Gates', email='student1@example.com', phone_number='964111111111', user=User.objects.get(username='student1'), birth_date='2000-01-01'),
                Student(name='Miragh Alhassan', email='student2@example.com', phone_number='964111111112', user=User.objects.get(username='student2'), birth_date='2000-01-01'),
                Student(name='Stevan Lopez', email='student3@example.com', phone_number='964111111113', user=User.objects.get(username='student3'), birth_date='2000-01-01'),
                Student(name='Christopher Nolan', email='student4@example.com', phone_number='964111111114', user=User.objects.get(username='student4'), birth_date='2000-01-01'),
                Student(name='Neil Harbour', email='student5@example.com', phone_number='964111111115', user=User.objects.get(username='student5'), birth_date='2000-01-01'),
                Student(name='Mark Lee', email='student6@example.com', phone_number='964111111116', user=User.objects.get(username='student6'), birth_date='2000-01-01'),
                Student(name='Nathan Smith', email='student7@example.com', phone_number='964111111117', user=User.objects.get(username='student7'), birth_date='2000-01-01'),
                Student(name='William Henry', email='student8@example.com', phone_number='964111111118', user=User.objects.get(username='student8'), birth_date='2000-01-01'),
                Student(name='Karthik Kumar', email='student9@example.com', phone_number='964111111119', user=User.objects.get(username='student9'), birth_date='2000-01-01'),
                Student(name='Eric Ries', email='student10@example.com', phone_number='964111111120', user=User.objects.get(username='student10'), birth_date='2000-01-01'),
                Student(name='Sundar Pichai', email='student11@example.com', phone_number='96411111121', user=User.objects.get(username='student11'), birth_date='2000-01-01'),
                Student(name='Manapreet Singh', email='student12@example.com', phone_number='96411111122', user=User.objects.get(username='student12'), birth_date='2000-01-01'),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample students'))

        if not Course.objects.count():
            Course.objects.bulk_create([
                Course(
                    name='Introduction to Python', 
                    image=os.path.join('images', 'course', 'python.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                    body='Python is the most popular programming language, created by Guido van Rossum, used for AI and web development.',
                    requirements='You should have basic knowledge of programming and mathematics',
                ),
                Course(
                    name='Introduction to Django', 
                    image=os.path.join('images', 'course', 'django.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=2000.00, 
                    currency=Currency.objects.get(code='IQD'),
                    body='Django is the most popular web framework, created by Django Software Foundation, used for building web applications',
                    requirements='You should have basic knowledge of python language and web development',
                ),
                Course(
                    name='React the best practice', 
                    image=os.path.join('images', 'course', 'react.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1500.00, 
                    currency=Currency.objects.get(code='IQD'),
                    body='React is the most popular frontend framework, created by Facebook',
                    requirements='You should have basic knowledge of javascript language and web development',
                ),
                Course(
                    name='Java Programming', 
                    image=os.path.join('images', 'course', 'java.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=0.00,
                    currency=Currency.objects.get(code='IQD'),
                    body='Java is the most popular programming language, created by Sun Microsystems, used primarily for desktop and mobile applications',
                    requirements='You should have basic knowledge of programming, algorithms and data structures',
                ),
                Course(
                    name='AI and ML Basics',
                    image=os.path.join('images', 'course', 'ai.jpg'),
                    category=Category.objects.get(name='Development'),
                    discount=100,
                    price=1200.00,
                    discount_starts_at=timezone.now().date(),
                    discount_ends_at=timezone.now().date() + timezone.timedelta(days=60),
                    currency=Currency.objects.get(code='IQD'),
                    body='Artificial Intelligence and Machine Learning is the technology that allows machines to learn and make predictions based on data.',
                    requirements='You should have good knowledge of Python programming and mathematics.',
                )
            ])
            # set teachers m2m field
            Course.objects.get(name='Introduction to Python').teachers.add(Teacher.objects.get(user__username='teacher1'))
            Course.objects.get(name='Introduction to Django').teachers.add(Teacher.objects.get(user__username='teacher2'))
            Course.objects.get(name='React the best practice').teachers.add(Teacher.objects.get(user__username='teacher3'))
            Course.objects.get(name='Java Programming').teachers.add(Teacher.objects.get(user__username='teacher4'))
            Course.objects.get(name='AI and ML Basics').teachers.add(Teacher.objects.get(user__username='teacher5'))

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
            course3 = Course.objects.get(name='React the best practice')
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

            # create lessons for java course
            course4 = Course.objects.get(name='Java Programming')
            Lesson.objects.bulk_create([
                Lesson(name='Why take this Java Course?', url='https://www.youtube.com/watch?v=VHbSopMyc4M', order=1, course=course4),
                Lesson(name='Programs and Programming Languages', url='https://www.youtube.com/watch?v=-C88r0niLQQ', order=2, course=course4),
                Lesson(name='Introduction to Java Programming', url='https://www.youtube.com/watch?v=mG4NLNZ37y4', order=3, course=course4),
                Lesson(name='Anatomy of Java Program', url='https://www.youtube.com/watch?v=vsxYucdzimA', order=4, course=course4),
                Lesson(name='Displaying Messages in Java', url='https://www.youtube.com/watch?v=ifirpBZLeCk', order=5, course=course4),
                Lesson(name='Displaying Numbers in Java', url='https://www.youtube.com/watch?v=UFMqdnUh4nI', order=6, course=course4),
                Lesson(name='Configuring our Java Development Environment', url='https://www.youtube.com/watch?v=FjGMYpXS9iE', order=7, course=course4),
                Lesson(name='Creating, Compiling, and Executing a Java Program', url='https://www.youtube.com/watch?v=gHXzyAkbUhk', order=8, course=course4),
                Lesson(name='Our First Java Project', url='https://www.youtube.com/watch?v=AVpLMoTnwM8', order=9, course=course4),
                Lesson(name='Java Packages, Classes, and Methods', url='https://www.youtube.com/watch?v=mgixJYEZ1Fk', order=10, course=course4),
                Lesson(name='public, private, and static in Java', url='https://www.youtube.com/watch?v=SITEc4DWwsQ', order=11, course=course4),
                Lesson(name='The void Return Type in Java', url='https://www.youtube.com/watch?v=14Cfx3fpH-w', order=12, course=course4),
                Lesson(name='Command Line Arguments in Java', url='https://www.youtube.com/watch?v=Up17-azeuyE', order=13, course=course4),
                Lesson(name='Programming Styles', url='https://www.youtube.com/watch?v=OXYT01qrDrc', order=14, course=course4),
                Lesson(name='Programming Errors', url='https://www.youtube.com/watch?v=dPQaQWyqYoc', order=15, course=course4),
                Lesson(name='Java Exercise - Creating Classes & Methods', url='https://www.youtube.com/watch?v=-94U78VoufQ', order=16, course=course4),
                Lesson(name='Java Basics - An Overview', url='https://www.youtube.com/watch?v=doxwM_gVc90', order=17, course=course4),
                Lesson(name='Introduction to Variables in Java', url='https://www.youtube.com/watch?v=N8LDSryePuc', order=18, course=course4),
                Lesson(name='Variables in Java - Practice', url='https://www.youtube.com/watch?v=Ls14YnfR7Hg', order=19, course=course4),
                Lesson(name='Constants in Java', url='https://www.youtube.com/watch?v=Ccc-Sk8qMAQ', order=20, course=course4),
            ])

            # create lessons for ai course
            course5 = Course.objects.get(name='AI and ML Basics')
            Lesson.objects.bulk_create([
                Lesson(name='The Rise of Generative AI for Business', url='https://www.youtube.com/watch?v=s4r5gXdSVPM', order=1, course=course5),
                Lesson(name='Become a value creator with generative AI', url='https://www.youtube.com/watch?v=fBR42OxjWaM', order=2, course=course5),
                Lesson(name='Why foundation models are a paradigm shift for AI', url='https://www.youtube.com/watch?v=1JzMSbcInxc', order=3, course=course5),
                Lesson(name='Trust, transparency, and governance in the age of generative AI', url='https://www.youtube.com/watch?v=odrD0OLPeiY', order=4, course=course5),
                Lesson(name='Putting AI to work for Customer Service', url='https://www.youtube.com/watch?v=_3-ZOKKo7II', order=5, course=course5),
                Lesson(name='Putting AI to Work for Application Modernization', url='https://www.youtube.com/watch?v=AINoTKMZSGI', order=6, course=course5),
                Lesson(name='Is data management the secret to generative AI?', url='https://www.youtube.com/watch?v=qtuzVc0N5o0', order=7, course=course5),
                Lesson(name='Putting AI to Work for Marketing', url='https://www.youtube.com/watch?v=c54qSfmTT5U', order=8, course=course5),
                Lesson(name='Putting AI to Work for talent', url='https://www.youtube.com/watch?v=MZmJTnjJd7Y', order=9, course=course5),
                Lesson(name='Select the right AI use case for your business', url='https://www.youtube.com/watch?v=C1ecR-sIE1A', order=10, course=course5),
                Lesson(name='How responsible AI can prepare you for AI regulations', url='https://www.youtube.com/watch?v=n0WapyCr0tk', order=11, course=course5),
                Lesson(name='Choose the right AI model for your use case', url='https://www.youtube.com/watch?v=aqWXSShwGO0', order=12, course=course5),
                Lesson(name='From pilot to production: Driving ROI with genAI', url='https://www.youtube.com/watch?v=FtYKoDomUp8', order=13, course=course5),
                Lesson(name='Achieving AI-readiness with hybrid cloud', url='https://www.youtube.com/watch?v=vI_2LSc6NCg', order=14, course=course5),
                Lesson(name='Putting AI to work in IT Operations', url='https://www.youtube.com/watch?v=4VCwKSaMOqY', order=15, course=course5),
                Lesson(name='Design a hybrid cloud infrastructure for and with AI', url='https://www.youtube.com/watch?v=6-s_fUXP0FM', order=16, course=course5),
                Lesson(name='Putting AI to work for Finance', url='https://www.youtube.com/watch?v=kNXOCsL9OF8', order=17, course=course5),
                Lesson(name='How business leaders budget for generative AI', url='https://www.youtube.com/watch?v=anirI6Xtezs', order=18, course=course5),
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