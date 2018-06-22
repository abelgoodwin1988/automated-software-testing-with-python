blogs = dict('')  # blog_name : Blog object

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

    print_blogs()

def print_blogs():
    # Print the available blogs
    # [(blog_name, Blog), (blog_name, Blog)]
    for key, blog in blogs.items(): 
        print('- {}'.format(blog))

menu()