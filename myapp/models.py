from django.db import models

# Create your models here.
class admintbl(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.username},{self.password}"

class manage_book_tbl(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    total_copies=models.CharField(max_length=100)
    available_copies=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.title},{self.author},{self.category},{self.total_copies},{self.available_copies}"

class manage_member_tbl(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    members_date=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.name},{self.email},{self.phone},{self.members_date}"

class issue_return_tbl(models.Model):
    id=models.AutoField(primary_key=True)
    bookid=models.CharField(max_length=100)
    memberid=models.CharField(max_length=100)
    duedate=models.CharField(max_length=100)
    issuedate=models.CharField(max_length=100)
    returndate=models.CharField(max_length=100)
    fine=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.bookid},{self.memberid},{self.duedate},{self.issuedate},{self.returndate},{self.fine}"

class return_book_tbl(models.Model):
    id=models.AutoField(primary_key=True)
    bookid=models.CharField(max_length=100)
    memberid=models.CharField(max_length=100)
    returndate=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id},{self.bookid},{self.memberid},{self.returndate}"

















