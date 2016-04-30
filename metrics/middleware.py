from metrics import models

def get_ip(request):
    x_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_for:
        ip = x_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class HitRecorder:
    def process_request(self, request):
        hit = models.Hit()
        hit.ip = get_ip(request)
        hit.ua = request.META.get('HTTP_USER_AGENT')
        hit.url = request.get_full_path()
        hit.save()
