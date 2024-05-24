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
        return httpx.post(
            self.url,
            headers={"User-Agent": self.user_agent},
            json=self.data,
            timeout=self.timeout,
            proxies=self.proxy
        )

    def video_get_syncPostRequest(self, video_id: str = None):  # new
        from tete import get_video_data
        data = get_video_data(video_id=video_id)
        self.data = data if data else self.data
        self.url = 'https://www.youtube.com/youtubei/v1/player?prettyPrint=false'
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
