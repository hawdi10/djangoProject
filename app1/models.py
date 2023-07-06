from django.db import models
# Create your models here.
class price(models.Model):
    money = models.IntegerField()
    stock = models.IntegerField()

class register(models.Model):
    name = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateTimeField()

class list(models.Model):
    name=models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"

class vahed(models.Model):
    name=models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    count = models.CharField(max_length=100)

class hesab(models.Model):
    name=models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    addres = models.CharField(max_length=100)

class register_person(models.Model):
    name=models.OneToOneField(list,on_delete=models.CASCADE)
    vahed=models.ForeignKey(vahed,on_delete=models.CASCADE)
    hesab=models.ManyToManyField(hesab)
    address = models.CharField(max_length=200)

class product(models.Model):
    title = models.CharField(max_length=50)
    Price = models.ManyToManyField(price)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.money}"

    def __str__(self):
        return f"{self.Price}"


class attribute(models.Model):
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    depth = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.title}"
