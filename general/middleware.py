from general import models
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
class TrackMiddleware:
    def process_request(self,request):
        """process this and let it fall through.
        Requires the presence of auth beforehand"""
        rq=models.Track()
        rq.ip=get_client_ip(request)
        rq.url=request.path
        try:rq.user=request.user
        except:rq.user=None
        rq.agent=request.META.get('HTTP_USER_AGENT')
        rq.save()
        return None
