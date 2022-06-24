import re
from jinja2 import Environment, FileSystemLoader


class Capitu:
    def __init__(self, templates_folder="templates"):
        self.url_map = []
        self.template_folder = templates_folder
        self.env = Environment(loader=FileSystemLoader(templates_folder))

    def route(self, rule, method="GET", template=None):
        
        def decorator(view):
            self.url_map.append((rule, method, view, template))
            return view

        return decorator

    def render_template(self, template_name, **context):
        template = self.env.get_template(template_name)
        return template.render(**context).encode("utf-8")

        def __call__(self, environ, start_response):
            body = b"Content Not Found"
            status = "404 Not Found"
            content_type = "text/html"
            # Processar o request
            path = environ["PATH_INFO"]
            request_method = environ["REQUEST_METHOD"]

            # Resolver URLS
            for rule, method, view, template in self.url_map:
                if (match := re.match(rule, path)):
                    if method != request_method:
                        continue
                    view_args = match.groupdict()
                    view_result = view(**view_args)
                    body = view_result.encode("utf-8")

            # Criar o responde
            headers = [("Content-type", content_type)]
            return [body]

        def run(self, host="0.0.0.0", port=8000):
            server = make_server(host, port, self)
            server.server_forever()
