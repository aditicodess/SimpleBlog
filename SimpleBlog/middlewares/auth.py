from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        print(request.session.get('token'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('token'):
            return redirect(f'login?return_url={returnUrl}')
        
        response = get_response(request)
        return response
    
    return middleware