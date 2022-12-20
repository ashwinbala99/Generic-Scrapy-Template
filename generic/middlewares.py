# A downloader middleware to set the common headers for all requests
class SetCommonHeadersMiddleware:
    def process_request(self, request, spider):
        request.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
