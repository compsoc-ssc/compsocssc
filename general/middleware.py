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
        """Process this and let it fall through.
        Requires the presence of auth beforehand"""

        track_needed = True
        if (request.path[:8] == '/static/'):
            track_needed = False
        if (request.path[:7]=='/media/'):
            track_needed = False
        if (request.path[:7]=='/admin/'):
            track_needed = False
        if not track_needed:
            return None

        rq = models.Track()
        rq.ip = get_client_ip(request)
        rq.url = request.path
        try:
            rq.user = request.user
        except:
            rq.user = None
        rq.agent = request.META.get('HTTP_USER_AGENT')
        rq.save()
        #-------------
        try:
            models.SiteVisit.objects.get(ip=rq.ip)
        except:
            sv = models.SiteVisit()
            sv.ip = rq.ip
            if rq.user != None:
                sv.users += 1
                sv.auth_access += 1
            sv.save()
        return None
