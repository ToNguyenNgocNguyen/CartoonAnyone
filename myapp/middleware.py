from django.http import HttpResponseBadRequest

class PreventDirectAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path is otpverify
        url = request.path.split("/")
        url.pop(-1)
        url = url[-1]
        if url == 'otpverify':
            # Check if the referer header exists
            referer = request.META.get('HTTP_REFERER')
            print(referer)
            if not referer or ('otpverify' not in referer and 'signup' not in referer):
                # If accessed directly or not from signup, return BadRequest
                return HttpResponseBadRequest('Direct access not allowed.')
                
        if url == 'resend':
            # Check if the referer header exists
            referer = request.META.get('HTTP_REFERER')
            if not referer or ('resend' not in referer and 'otpverify' not in referer):
                # If accessed directly or not from signup, return BadRequest
                return HttpResponseBadRequest('Direct access not allowed.')

        if url == 'forgot':
            # Check if the referer header exists
            referer = request.META.get('HTTP_REFERER')
            if not referer or ('forgot' not in referer and 'login' not in referer):
                # If accessed directly or not from signup, return BadRequest
                return HttpResponseBadRequest('Direct access not allowed.')

        if url == 'reset':
            # Check if the referer header exists
            referer = request.META.get('HTTP_REFERER')
            if not referer or ('reset' not in referer and 'forgot' not in referer):
                # If accessed directly or not from signup, return BadRequest
                return HttpResponseBadRequest('Direct access not allowed.')
            
        return self.get_response(request)
