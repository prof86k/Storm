from django.db import models

# Create your models here.


class MainChurch(models.Model):
    """ Main church existing example Catholic """
    pass



class ChurchBranch(models.Model):
    """ The branch of a particular main church. """
    mainchurch = models.ForeignKey(MainChurch,on_delete=models.CASCADE)