from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Class for HelloApiView"""

    def get(self, request, format=None):
        """Returns a list of apiview features"""
        an_apiview = [
            'Uses traditional HTTP methods as functions(get, post, put, patch, delete)',
            'Gives most control over application logic',
            'Is similar to traditional Django View',
            'URLs are mapped manually to APIView'
        ]
        return Response({
            'message': 'Hello', 'an_apiview': an_apiview
        })
