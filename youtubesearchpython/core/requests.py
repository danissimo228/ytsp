import httpx
import os

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    def __init__(self):
        self.url = None
        self.data = None
        self.timeout = 2
        self.proxy = {}
        self.user_agent = userAgent
        http_proxy = os.environ.get("HTTP_PROXY")
        if http_proxy:
            self.proxy["http://"] = http_proxy
        https_proxy = os.environ.get("HTTPS_PROXY")
        if https_proxy:
            self.proxy["https://"] = https_proxy

    def syncPostRequest(self) -> httpx.Response:
        if self.url == 'https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&contentCheckOk=True&racyCheckOk=True&videoId=z0GKGpObgPY':
            print("============================================================================")
            print(self.url)
            print({"User-Agent": self.user_agent},"asdasd")
            print(self.data,"asdasd")
            print(self.timeout, "asdasd")
            print(self.proxy,"asdasd")
            from tete import a
            self.data = a
            self.url = 'https://www.youtube.com/youtubei/v1/player?prettyPrint=false'
            print(httpx.post(
                self.url,
                headers={"User-Agent": self.user_agent},
                json=self.data,
                timeout=self.timeout,
                proxies=self.proxy
            ).text)
            print("============================================================================")

        return httpx.post(
            self.url,
            headers={"User-Agent": self.user_agent},
            json=self.data,
            timeout=self.timeout,
            proxies=self.proxy
        )

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(proxies=self.proxy) as client:
            r = await client.post(self.url, headers={"User-Agent": self.user_agent}, json=self.data,
                                  timeout=self.timeout)
            return r

    def syncGetRequest(self) -> httpx.Response:
        return httpx.get(self.url, headers={"User-Agent": self.user_agent}, timeout=self.timeout,
                         cookies={'CONSENT': 'YES+1'}, proxies=self.proxy)

    async def asyncGetRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(proxies=self.proxy) as client:
            r = await client.get(self.url, headers={"User-Agent": self.user_agent}, timeout=self.timeout,
                                 cookies={'CONSENT': 'YES+1'})
            return r
