from django.http import HttpResponse


class StripWH_Handler:
    """ Handles stripe webhooks """

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """
        return HttpResponse(
            content=f'Event recieved: {event["type"]}'
            status=200
        )