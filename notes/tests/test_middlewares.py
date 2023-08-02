from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from notes.middleware.error_handler import ErrorHandlingMiddleware

class ErrorHandlingMiddlewareTest(TestCase):
    
    def test_custom_error_response(self):
        def raise_exception(_):
            raise Exception("Test Exception")
        
        middleware = ErrorHandlingMiddleware(raise_exception)
        response = middleware(None)
        self.assertEqual(response.status_code, 500)
        self.assertJSONEqual(str(response.content, encoding='utf-8'), {'error': 'An error occurred during request processing.'})
