from django.db import models

# Create your models here.

class Kid(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id', verbose_name='id')
    name = models.CharField(max_length=20, db_column='name', verbose_name='kid name')
    age = models.IntegerField(db_column='age', verbose_name='kid age')
    sex = models.CharField(max_length=10, db_column='sex', verbose_name='kid sex')

    def __str__(self):
        return 'name: {0}'.format(self.name)

    class Meta:
        db_table = 'kid'

