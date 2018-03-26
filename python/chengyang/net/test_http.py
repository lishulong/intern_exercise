from pykit import http


if __name__ == '__main__':

    headers = {
        'Host': '127.0.0.1',
        'Accept-Language': 'en, mi',
    }
    h_client = http.Client('127.0.0.1', 8000)

    h_client.send_request('./test.txt', method='GET', headers=headers)

    test_status = h_client.read_status()
    test_headers = h_client.read_headers()
    test_boby = h_client.read_body(1024)
    test_trace = h_client.get_trace_str()

    print test_status
    print test_headers
    print test_boby
    print test_trace
    print

    test = 'wo shi cheng yang '
    headers['content-length'] = len(test)

    h_client.send_request('./test.txt', method='POST', headers=headers)

    h_client.send_body(test)

    test_status, test_headers = h_client.read_response()
    test_boby = h_client.read_body(1024)

    print test_status
    print test_headers
    print test_boby
    print
