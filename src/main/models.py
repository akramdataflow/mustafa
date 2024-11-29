from django.db import models
from django.contrib.auth.models import User

from django.db import models

# نموذج الأنواع
class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# نموذج الكورس
class Course(models.Model):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    EXPERT = 'All Level'  # خيار جديد للمستوى المتقدم جدًا
    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXPERT, 'All Level'),  # الخيار الجديد
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    category = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')  # ربط مع المستخدمين
    level = models.CharField(max_length=20,choices=LEVEL_CHOICES,default=BEGINNER)  # القيمة الافتراضية للمستوى
    lessons_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# نموذج محتوى الكورس
class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')  # ربط المحتوى بالكورس
    title = models.CharField(max_length=200)  # عنوان الفيديو
    content_file = models.FileField(upload_to='course_videos/', blank=True, null=True)  # رفع الفيديو
    created_at = models.DateTimeField(auto_now_add=True)  # تاريخ إضافة المحتوى

    def __str__(self):
        return self.title

# نموذج الاشتراكات
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')  # ربط مع المستخدمين
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # منع التكرار في الاشتراك بنفس الكورس

# نموذج المراجعات
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  # ربط مع المستخدمين
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # منع أكثر من مراجعة لنفس الكورس من نفس الطالب

# نموذج التخفيضات
class Discount(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='discounts')
    percentage = models.PositiveIntegerField()  # نسبة التخفيض
    start_date = models.DateField()
    end_date = models.DateField()

    def is_active(self):
        """
        التحقق مما إذا كان التخفيض نشطًا حاليًا.
        """
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    def __str__(self):
        return f"{self.percentage}% على {self.course.title}"
