MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'

blogs = dict('')  # blog_name : Blog object

def menu():
    # show the user the available blogs
    print_blogs()
    # let the user make a choice
    selection = input(MENU_PROMPT)
    # do something with that choice
    # eventually exit

def print_blogs():
    # Print the available blogs
    # [(blog_name, Blog), (blog_name, Blog)]
    for key, blog in blogs.items(): 
        print('- {}'.format(blog))

#menu()
