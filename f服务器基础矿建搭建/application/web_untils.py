def create_http_split(status, response_body):
    response_line = "HTTP/1.1 %s ok\r\n" % status
    response_header = "Servers:pythonfqm\r\n"
    response_blank = "\r\n"

    data = response_line + response_header + response_blank + response_body
    return data
