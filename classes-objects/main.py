from user import User
from post import Post

app_user_one = User("taiwo@gmail.com", "taiwo", "pwd", "Devops Engineer")
app_user_one.get_user_info()

app_user_two = User("007@janesbond.io", "Bond", "Super Agent", "Agent")
app_user_two.get_user_info()

new_post = Post("This is a classified info", app_user_two.name)
new_post.get_post_info()