from rest_framework.pagination import PageNumberPagination

class SmallSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 12

class MediumSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 21


class LargeSetPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 21
    page_size_query_param = 'page_size'
    max_page_size = 27