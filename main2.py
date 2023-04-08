from user import User
from post import Post

app_user_one = User("nn@nn.com","abdo", "pwd" , "devops")
#app_user_one.get_user_info()


app_user_one = User("ffff@dd.com","hhhh", "pwd" , "bbbbb")
#app_user_one.get_user_info()

new_post = Post("hello" , app_user_one.name)
new_post.get_post_info()