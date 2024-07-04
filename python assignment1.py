# task 1
number = 0
next_numbers = 0

for i in range(10):
    number += i
    next_numbers = number + 1
    print(f"number:{number}, 'sum of previous and current number': {next_numbers}" )
    if next_numbers > 10:
        break

# task 2 of the assignment
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def calculate_average_grade(self, grades):
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

# task 3 of the assignment



def numbers(list):
     if list[0] == list[-1]:
          return True
     else:
          return False
     
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(numbers(numbers_x))
print(numbers(numbers_y))


#django project
# blogapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

# blogapp/admin.py

from django.contrib import admin
from .models import Blog

admin.site.register(Blog)

# blogapp/views.py

from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user  # Current logged-in user

        blog = Blog.objects.create(title=title, content=content, author=author)
        # Optionally, you can redirect to a success page or the blog detail view
        return redirect('blog-detail', pk=blog.pk)

    return render(request, 'blog/create_blog.html')
