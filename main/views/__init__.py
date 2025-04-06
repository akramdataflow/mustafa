from .api import *
from .common import about_view, contact_view, user_login, signup_view, payment_page, payment_status
from .course import (
    course_list_view, course_details_view, teacher_list_view, teacher_details_view,
    learning_board_view, lesson_preview_view,
)
from .cart import add_to_cart_view, remove_from_cart_view, join_course_view
from .home import home_view