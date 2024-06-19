from cgi import parse_qs
from template import html
import matplotlib.pyplot as plt

def application(environ, start_response):
	if environ['PATH_INFO'] == '/img/graph.png':
		try:
			with open('./img/graph.png', 'rb') as f:
				response_body = f.read()
		except:
			response_body = ''
		start_response('200 OK', [
			('Content-Type', 'image/png'),
			('Content-Length', str(len(response_body)))
		])
