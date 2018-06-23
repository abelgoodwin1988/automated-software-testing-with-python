MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit.'

blogs = dict('')  # blog_name : Blog object

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

    print_blogs()
    selection = get_input()
    
def get_input():
    return input(MENU_PROMPT)

def print_blogs():
    # Print the available blogs
    # [(blog_name, Blog), (blog_name, Blog)]
    for key, blog in blogs.items(): 
        print('- {}'.format(blog))

menu()
