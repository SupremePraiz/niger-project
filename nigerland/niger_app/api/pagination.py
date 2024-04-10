from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class DocumentListPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 20
    last_page_strings = 'end'


class DocumentListPaginationLO(LimitOffsetPagination):
    default_limit = 5
    max_limit = 7
    limit_query_param = 'limit'
    offset_query_param = 'start'


class DocumentListPaginationCu(CursorPagination):
    page_size = 3


