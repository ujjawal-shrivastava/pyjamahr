import logging
from django.http import JsonResponse

class ErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
            try:
                response = self.get_response(request)
            except Exception as e:
                self.logger.exception("An error occurred during request processing.")
                error_message = "An error occurred during request processing."
                response_data = {'error': error_message}
                response = JsonResponse(response_data, status=500)
            return response

