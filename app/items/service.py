from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import *

class PaginationProduct(PageNumberPagination):
    page_size = 1
    max_page_size = 12

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
