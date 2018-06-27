from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post

class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test Blog', 'Test Author')
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {blog.title: blog}
        
    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Blog', 'Test Author', 'q')
            
            app.menu()

            self.assertIsNotNone(app.blogs['Test Blog'])

    def test_menu_calls_print_blogs_values(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print.assert_called_with(
                    '- Test Blog by Test Author (1 post)')

    def test_menu_calls_ask_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('r', 'Test Blog', 'q')
                
                expected_print = '''
--- Test Post ---

Test Content

'''
                app.menu()
            
                mocked_print.assert_called_with(expected_print)

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p','Test Blog', 'Test Post', 'Test Content', 'q')
            app.menu()
            self.assertEqual(app.blogs['Test Blog'].posts[0].title, 'Test Post')

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Blog by Test Author (1 post)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test Blog'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test Blog'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test Blog'])

    def test_print_posts(self):
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(app.blogs['Test Blog'])

            mocked_print_post.assert_called_with(app.blogs['Test Blog'].posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
--- Post title ---

Post content

'''

        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {blog.title: blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')
