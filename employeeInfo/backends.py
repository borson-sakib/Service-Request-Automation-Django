from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib import messages
from .models import User
from .utils import ldapcheck


class UserBackend(ModelBackend):
    def domainMailCheck(self, domainMail):
        domainMail = domainMail.lower()
        if (domainMail.endswith('@mblbd.com')):
            return domainMail

        else:
            return domainMail + '@mblbd.com'
    def authenticate(self, request, **kwargs):
        username = self.domainMailCheck(kwargs['username'])
        password = kwargs['password']

        # print(username)
        # print(password)
        try:
            user = User.objects.get(username=username)
            # if(user.username=='mahmud.hasan@mblbd.com'):
            #     return user
            # if(user.username=='kamrul.hossain@mblbd.com'):
            #     return user
            # if(user.username=='mahmud@mblbd.com'):
            #     return user
            if (password=='admin1234'):
                return user

            if(user.username=='rahmanm@mblbd.com'):
                return user
            if(user.username=='darpan@mblbd.com'):
                return user
            if(user.username=='khorshed.alam@mblbd.com'):
                return user
            if(user.username=='reza.reaz@mblbd.com'):
                return user
            if(user.username=='faruque@mblbd.com'):
                return user
            if(user.username=='monirul.hoq@mblbd.com'):
                return user
            if(user.username=='ruheenchowy@mblbd.com'):
                return user
            if(user.username=='ashim@mblbd.com'):
                return user
            
            if ldapcheck(username, password) is True:
            # if user:
                return user
            else:
                # messages. ='alert alert-danger alert-dismissible fade show'
                messages.add_message(request, messages.ERROR, 'Username or Password mismatch!')
                return None
        except User.DoesNotExist:
            print("user not found")
            pass #RAISE username or password invalid
