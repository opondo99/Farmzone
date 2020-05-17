# Create your models here.
from django.db import models
import uuid

#userid from model Usser is used for forum messaging



#theead tabel

class Thread(models.Model):
    '''
    The starter for the thread
    Once it has been created  by a user,,
    Other people can comment about it.
    '''
    thread_id = models.UUIDField(primary_key = True , unique = True , default=uuid.uuid4)
    # user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    thread_message = models.TextField(max_length = 1255)
    thread_post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Name for the table.
        '''
        db_table = "Thread"

    def _str__(self):
        """Thread instance."""
        return f'{self.thread_message}  by user_id {self.user_id}'


class Forum(models.Model):
    '''
    The class to create db for the forum messaging details
    with the time of post
    poster who posted
    and the messages itself
    This will be a reply from # thread table.
    '''
    forum_id = models.UUIDField(primary_key = True , unique = True , default=uuid.uuid4)
    # user_id = models.ForeignKey(User,on_delete = models.CASCADE)#this is not indicated in the schema
    forum_post = models.TextField(max_length=1255)
    forum_post_time = models.DateTimeField(auto_now_add=True)
    thread_id = models.ForeignKey(Thread , on_delete = models.CASCADE)




    class Meta:
        '''
        Name for the table.
        '''
        db_table = "Forum"

    def __str__(self):
        """Checking forum instance."""
        return f'{self.forum_post}  by user_id {self.user_id} on thread with id {self.thread_id}'



#chat table for commenting about a product
class Chat(models.Model):
    '''
    The implimentation for the caht table in which a user can comment
    about the product.
    '''
    chat_id = models.UUIDField(default = uuid.uuid4 , primary_key = True , unique = True)
    # user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    message = models.TextField(max_length = 1255)
    # username .....my thougth is we have user_id we can the get the username using it
    #i aslo think we can get the time---- in full format instead of getting time and date separetely
    #it will be broken apart from there
    #i have added ads-id since am seeing its purposes for showing which commodity was
    # being commented about
    # ads_id = models.ForeignKey(ProductsAds , on_delete = models.CASCADE)
    # category_id = models.ForeignKey(Category , on_delete = models.CASCADE)



    class Meta():
        '''
        message_post_time = models.DateTimeField(auto_now_add = True)
        Name for the table.
        '''
        db_table = "Chat"

<<<<<<< HEAD
    def __str__():
        """Chat instance."""
=======

    def __str__(self):
        """Check data."""
>>>>>>> origin/forum_back
        return f'{self.message} by {self.user_id}'
