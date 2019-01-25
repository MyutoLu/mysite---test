from django.db import models
#from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.conf import settings
'''class test():
    def get_read_num(self):    
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct,object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0'''

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


 
class Blog(models.Model,ReadNumExpandMethod):
    """docstring for Blog"""
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    '''def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    '''
    '''def get_read_num(self):
        
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct,object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0'''

    def __str__(self):
        return "<Blog: %s>" %self.title
    class Meta:
        ordering = ['-created_time']
'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog,on_delete=models.DO_NOTHING)
'''
