from django.db import models

# Create your models here.
class ContentCategory(models.Model):
    type = models.CharField(max_length=10) # 101: list, 102: gallery, 103: video, 104: file
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    sort = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "content_category"
        ordering = ['sort']


class Content(models.Model):
    category = models.ForeignKey(ContentCategory, on_delete=models.CASCADE)
    header = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100)
    content = models.TextField(null=True)
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    is_notice = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_comment = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        db_table = "contents"
        ordering = ['-created_date']


class ContentAttach(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    attach_type = models.CharField(max_length=10) # 101: image, 102: video, 103: file 
    attach_name = models.CharField(max_length=100)
    extension = models.CharField(max_length=10, null=True)
    size = models.IntegerField(null=True)
    sort = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.attach_name
    
    class Meta:
        db_table = "contents_attach"
        ordering = ['sort']