from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class OrderResultSetPagination(PageNumberPagination):
    page_size = settings.ORDERS_PER_PAGE
    page_size_query_param = 'page_size'
