from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit. '
ASK_CREATE_POST_PROMPT_BLOG_TITLE = 'Enter the title of a blog above: '
ASK_CREATE_POST_PROMPT_POST_TITLE = 'Enter the title of the post: '
ASK_CREATE_POST_PROMPT_POST_CONTENT = 'Enter the content of the post: '
POST_PRINT_TEMPLATE = '''
--- {} ---

{}

'''

blogs = dict('')  # blog_name : Blog object

def menu():
    # show the user the available blogs
    print_blogs()
    # let the user make a choice
    selection = input(MENU_PROMPT)
    # do something with that choice
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()        
        selection = input(MENU_PROMPT)
    # eventually exit

def print_blogs():
    # Print the available blogs
    # [(blog_name, Blog), (blog_name, Blog)]
    if len(blogs) < 1:
        print('No Blogs, try creating one.')
    else:
        for key, blog in blogs.items():
            print('- {}'.format(blog))

def ask_create_blog():
    title = input('Enter title name: ')
    author = input('Enter Author name: ')
    blogs.update({title: Blog(title, author)})

def ask_read_blog():
    list_blog_titles()
    title = input('Enter the title of a blog above: ')
    try:
        print_posts(blogs[title])
    except:
        print('No Title Found.')
        print('Redirecting to main menu...')

def ask_create_post():
    list_blog_titles()
    blog_title = input(ASK_CREATE_POST_PROMPT_BLOG_TITLE)
    post_title = input(ASK_CREATE_POST_PROMPT_POST_TITLE)
    post_content = input(ASK_CREATE_POST_PROMPT_POST_CONTENT)
    blogs[blog_title].create_post(post_title, post_content)

def list_blog_titles():
    for key, blog in blogs.items():
        print(blog.title)

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_PRINT_TEMPLATE.format(post.title, post.content))


#menu()
