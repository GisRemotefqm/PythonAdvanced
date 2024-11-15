from web_untils import *


def parse_request(html_data):
    loc = html_data.find("\r\n")
    request_line = html_data[:loc]
    print("请求行是%s" % request_line)
    line_list = request_line.split(" ")
    print("请求行是%s" % line_list)
    file_path = line_list[1]
    print("资源路径是fqmhtml%s" % file_path)
    # 8.拼接响应报文

    return file_path


def applications(html_data):

    file_path = parse_request(html_data)
    # 返回固定页面
    try:
        with open("fqmhtml" + file_path, "r") as file:
            response_body = file.read()
        data = create_http_split("200 ok", response_body)
    except Exception as e:
        # 修改响应行
        data = create_http_split("404 Not Found", response_body)

    return data
