from django.db import models



class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField( default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    #Olusturulma Tarihine göre siralamak icin class Meta olusturduk. - isareti tersten siralamaya yariyor.
    class Meta:
        ordering = ('-created_date',)# - nin amaci en son ekledigim en basta listelensin diye.
        
    def __str__(self):
        return self.title
    
    
    