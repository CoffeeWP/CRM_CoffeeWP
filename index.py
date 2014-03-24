#from django.core import management
#management.call_command("startproject", "DjangoCoffee")


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return "Hello World from Python"


