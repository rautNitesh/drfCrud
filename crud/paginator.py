from rest_framework.pagination import LimitOffsetPagination


class MyPaginator(LimitOffsetPagination):
    default_limit = 1