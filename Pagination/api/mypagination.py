from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination # limit of page
from rest_framework.pagination import CursorPagination # cursor paginaiton



# class MyPageNumberPagination(PageNumberPagination):
#     page_size=5
#     page_query_param='p'
#     # define the client in the page size
#     page_size_query_param = 'records'
#     # define the page size
#     max_page_size=5


# class MyPageNumberPagination(LimitOffsetPagination):
#     pass

# Cursor Pagination
class MyCursorPagination(CursorPagination):
    page_size=3
    ordering = 'name'