from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,BaseUserManager,Group,Permission
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta
from django.utils import timezone


# class UserManager(BaseUserManager): #このメソッドは、一般ユーザーを作成するためのものです。記載内容のバックアップです!
#     #ユーザー作成手法
#     def create_user(self, username, email, password=True): #username と email を引数として受け取り、email が指定されていない場合は ValueError を発生させます。
#         if not email:
#             raise ValueError('emailを入力してください')
#         user = self.model( #self.model を使用して新しいユーザーオブジェクトを作成し、username と email を設定します。
#             username = username,
#             email = email,
#         )
#         user.set_password(password) #set_password メソッドを使用してパスワードを設定し、ハッシュ化します。
#         user.save(using=self._db) #save(using=self._db) を呼び出して、データベースにユーザーを保存します。
#         return user
#     def create_superuser(self, username, email, password=True): #このメソッドは、スーパーユーザー (管理者) を作成するためのものです。
#         user = self.model( #username と email を引数として受け取り、create_user メソッドと同様にユーザーオブジェクトを作成します。
#             username = username,
#             email = email,
#         )
#         user.set_password(password) #set_password メソッドを使用してパスワードを設定し、ハッシュ化します。
#         user.is_staff = True
#         user.is_active = True
#         user.is_superuser = True #is_staff、is_active、is_superuser のフラグをすべて True に設定して、スーパーユーザーの特権を付与します。
#         user.save(using=self._db) #save(using=self._db) を呼び出して、データベースにユーザーを保存します。
#         return user

class UserManager(BaseUserManager): #このメソッドは、一般ユーザーを作成するためのものです。記載内容のバックアップです!
    #ユーザー作成手法
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('emailを入力してください')
        if not password:
            raise ValueError('パスワードを入力してください')
        user = self.model(
            username=username,
            email=email,
    )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):
        if not password:
            raise ValueError('パスワードを入力してください')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# class Users(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255)
#     age = models.PositiveIntegerField()
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     picture = models.FileField(null=True, upload_to='picture/')
#     picture2 = models.ImageField(null=True, upload_to='images/')  # 新しい ImageField を追加します！
#     introduction = models.CharField(max_length=255, null=True) #追加します!
#     counselor = models.ForeignKey('Counselor', on_delete=models.SET_NULL, related_name='clients', null=True, blank=True)

#     groups =  models.ManyToManyField(Group,related_name='user_groups')
#     user_permissions = models.ManyToManyField(Permission,related_name='user_permissions')

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = 'users'

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)  # デフォルト値を True に変更
    is_staff = models.BooleanField(default=True)   # デフォルト値を True に変更
    picture = models.FileField(null=True, upload_to='picture/')
    picture2 = models.ImageField(null=True, upload_to='images/')
    introduction = models.CharField(max_length=255, null=True)
    counselor = models.ForeignKey('Counselor', on_delete=models.SET_NULL, related_name='clients', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # # ここにis_counselorメソッドを追加します
    # def is_counselor(self):
    #     return self.counselor is not None

    # ここにis_counselorメソッドを追加します
    def is_counselor(self):
        return self.counselor is True

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'

# from cloudinary.models import CloudinaryField　#2024年8月追加

# class Users(AbstractBaseUser, PermissionsMixin):　#2024年8月追加
#     username = models.CharField(max_length=255)
#     age = models.PositiveIntegerField()
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     picture = CloudinaryField('picture', null=True, blank=True)
#     picture2 = CloudinaryField('images', null=True, blank=True)
#     introduction = models.CharField(max_length=255, null=True)
#     counselor = models.ForeignKey('Counselor', on_delete=models.SET_NULL, related_name='clients', null=True, blank=True)
#     groups = models.ManyToManyField(Group, related_name='user_groups')
#     user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def is_counselor(self):
#         return self.counselor is True

#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = 'users'

# class Counselor(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=255)
#     age = models.PositiveIntegerField(default=0, null=True)
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     picture = models.FileField(null=True, upload_to='picture/')
#     picture2 = models.ImageField(null=True, upload_to='images/')  # 新しい ImageField を追加します！
#     introduction = models.CharField(max_length=255, null=True)
#     qualifications = models.CharField(max_length=255, null=True) #ユーザーの職業、学歴、専門知識などを記録するのに便利です。
#     is_counselor = models.BooleanField(default=False)  # 新しいフィールドを追加

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = 'counselor'

class Counselor(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0, null=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)  # デフォルト値を True に変更
    is_staff = models.BooleanField(default=True)   # デフォルト値を True に変更
    picture = models.FileField(null=True, upload_to='picture/')
    picture2 = models.ImageField(null=True, upload_to='images/')
    introduction = models.CharField(max_length=255, null=True)
    qualifications = models.CharField(max_length=255, null=True)
    is_counselor = models.BooleanField(default=True)  # デフォルト値を True に変更

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'counselor'

# class Counselor(AbstractBaseUser, PermissionsMixin): #2024年8月追加
#     username = models.CharField(max_length=255)
#     age = models.PositiveIntegerField(default=0, null=True)
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     picture = CloudinaryField('picture', null=True, blank=True)
#     picture2 = CloudinaryField('images', null=True, blank=True)
#     introduction = models.CharField(max_length=255, null=True)
#     qualifications = models.CharField(max_length=255, null=True)
#     is_counselor = models.BooleanField(default=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = 'counselor'

class UserActivateTokensManager(models.Manager):

    def activate_user_by_token(self, token):
        user_activate_token = self.filter( # type: ignore
            token=token,
            expired_at__gte=datetime.now()
        ).first()
        user = user_activate_token.user # type: ignore
        user.is_active =True
        user.save()

class UserActivateTokens(models.Model):

    token = models.UUIDField(db_index=True) # UUIDField を使用してトークンを保存します
    expired_at = models.DateTimeField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    objects = UserActivateTokensManager() # type: ignore

    class Meta:
        db_table = 'user_activate_tokens'

@receiver(post_save, sender=Users) #記載内容のバックアップです！
def publish_token(sender, instance, **kwargs):
    print(str(uuid4()))
    print(datetime.now() + timedelta(days=1))
    user_activate_token = UserActivateTokens.objects.create(
        user=instance, token=str(uuid4()), expired_at=datetime.now() + timedelta(days=1)
    )
    # メールでURLを送る方がよい
    print(f'http://127.0.0.1:8000/accounts/activate_user/{user_activate_token.token}')

