import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.models import Currency
from main.models import Category, Course, Lesson, Review, Teacher



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
            User.objects.create_superuser('admin', 'admin', 'admin')
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
                Teacher(name='Richard Hendricks', user=User.objects.get(username='teacher1')),
                Teacher(name='Mathieu Zanardini', user=User.objects.get(username='teacher2')),
                Teacher(name='Erik Brynroflsson', user=User.objects.get(username='teacher3')),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample teachers'))

        if not Course.objects.count():
            Course.objects.bulk_create([
                Course(
                    name='Introduction to Python', 
                    body='Python is the most popular programming language', 
                    image=os.path.join('images', 'course', 'python.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                    teachers=[Teacher.objects.get(name='Teacher 1')]
                ),
                Course(
                    name='Introduction to Django', 
                    body='Django is the most popular web framework', 
                    image=os.path.join('images', 'course', 'django.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                    teachers=[Teacher.objects.get(name='Teacher 2')]
                ),
                Course(
                    name='Introduction to React', 
                    body='React is the most popular frontend framework', 
                    image=os.path.join('images', 'course', 'react.jpg'), 
                    category=Category.objects.get(name='Development'), 
                    price=1000.00, 
                    currency=Currency.objects.get(code='IQD'),
                    teachers=[Teacher.objects.get(name='Teacher 3')]
                ),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample courses'))

        if not Lesson.objects.count():
            # create lessons for python course
            Course.objects.get(name='Introduction to Python').lessons.bulk_create([
                Lesson(name='Installing Python', url="https://www.python.org/downloads/", order=1),
                Lesson(name='Variables and Data Types', url="https://youtu.be/LKFrQXaoSMQ", order=2),
                Lesson(name='Control Flow', url="https://www.youtube.com/watch?v=Zp5MuPOtsSY", order=3),
                Lesson(name='Functions', url="https://www.youtube.com/watch?v=89cGQjB5R4M", order=4),
                Lesson(name='Lists', url="https://www.youtube.com/watch?v=9OeznAkyQz4", order=5),
                Lesson(name='Dictionaries', url="https://www.youtube.com/watch?v=MZZSMaEAC2g", order=6),
                Lesson(name='Tuples', url="https://www.youtube.com/watch?v=w6hL_dszMxk", order=7),
                Lesson(name='Sets', url="https://www.youtube.com/watch?v=t9j8lCUGZXo", order=8),
                Lesson(name='Loops', url="https://www.youtube.com/watch?v=94UHCEmprCY", order=9),
                Lesson(name='Modules', url="https://www.youtube.com/watch?v=XcfxkHrHTVE", order=10),
                Lesson(name='Classes', url="https://www.youtube.com/watch?v=g-qRKZD3FgE", order=11),
                Lesson(name='Exceptions', url="https://www.youtube.com/watch?v=j_q6NGOwDJo", order=12),
                Lesson(name='File I/O', url="https://www.youtube.com/watch?v=LpZmZs2_BC4", order=13),
                Lesson(name='Object-Oriented Programming', url="https://www.youtube.com/watch?v=q2SGW2VgwAM", order=14),
                Lesson(name='Regular Expressions', url="https://www.youtube.com/watch?v=nxjwB8up2gI", order=15),
                Lesson(name='Generators', url="https://www.youtube.com/watch?v=gMompY5MyPg", order=16),
                Lesson(name='Decorators', url="https://www.youtube.com/watch?v=U-G-mSd4KAE", order=17),
                Lesson(name='Multithreading', url="https://www.youtube.com/watch?v=STEOavXqXkQ", order=18),
                Lesson(name='Asynchronous Programming', url="https://www.youtube.com/watch?v=K56nNuBEd0c", order=19),
                Lesson(name='Testing', url="https://www.youtube.com/watch?v=1Lfv5tUGsn8", order=20),
                Lesson(name='Debugging', url="https://www.youtube.com/watch?v=bHx8A8tbj2c", order=21),
                Lesson(name='Deployment', url="https://www.youtube.com/watch?v=Ehhs8czHDNY", order=22),
            ])

            # create lessons for django course
            Course.objects.get(name='Introduction to Django').lessons.bulk_create([
                Lesson(name='Installing Django', url='https://www.youtube.com/watch?v=rHux0gMZ3Eg', order=1),
                Lesson(name='Models', url='https://www.youtube.com/watch?v=rI95wyHD_6k', order=2),
                Lesson(name='Views', url='https://www.youtube.com/watch?v=RE0HlKch_3U', order=3),
                Lesson(name='Templates', url='https://www.youtube.com/watch?v=GNlIe5zvBeQ', order=4),
                Lesson(name='Forms', url='https://www.youtube.com/watch?v=4pSPWkrd-1M', order=5),
                Lesson(name='Authentication', url='https://www.youtube.com/watch?v=tUqUdu0Sjyc', order=6),
                Lesson(name='APIs', url='https://www.youtube.com/watch?v=cJveiktaOSQ&t=1s', order=7),
                Lesson(name='Testing', url='https://www.youtube.com/watch?v=bIFVweK0hMc', order=8),
                Lesson(name='Deployment', url='https://www.youtube.com/watch?v=IoxHUrbiqUo', order=9),
            ])

            # create lessons for react course
            Course.objects.get(name='Introduction to React').lessons.bulk_create([
                Lesson(name='Installing React', url='https://www.youtube.com/watch?v=yOAZDymGWVw', order=1),
                Lesson(name='Components', url='https://www.youtube.com/watch?v=Y2hgEGPzTZY', order=2),
                Lesson(name='Props', url='https://www.youtube.com/watch?v=uvEAvxWvwOs', order=3),
                Lesson(name='State', url='https://www.youtube.com/watch?v=O6P86uwfdR0', order=4),
                Lesson(name='Events', url='https://www.youtube.com/watch?v=lE31_0cXeAg', order=5),
                Lesson(name='Forms', url='https://www.youtube.com/watch?v=cc_xmawJ8Kg', order=6),
                Lesson(name='APIs', url='https://www.youtube.com/watch?v=00lxm_doFYw', order=7),
                Lesson(name='Testing', url='https://www.youtube.com/watch?v=8Xwq35cPwYg', order=8),
                Lesson(name='Deployment', url='https://www.youtube.com/watch?v=KFwFDZpEzXY', order=9),
            ])

            self.stdout.write(self.style.SUCCESS('Successfully created sample lessons'))
