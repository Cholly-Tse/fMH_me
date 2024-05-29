"""
@Project   : onepush
@Author    : y1ndan
@Blog      : https://www.yindan.me
"""

from ..core import Provider


class Discord(Provider):
    name = 'discord'
    site_url = 'https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'

    _params = {
        'required': ['webhook'],
        'optional': ['title', 'content', 'username', 'avatar_url', 'color']
    }

    async def _prepare_url(self, webhook: str, **kwargs):
        self.url = webhook
        return self.url

    async def _prepare_data(self,
                      title: str = None,
                      content: str = None,
                      username: str = None,
                      avatar_url: str = None,
                      color: str = '16478873',
                      **kwargs):
        self.data = {
            'username': username,
            'avatar_url': avatar_url,
            'embeds': [{
                'title': title,
                'description': content,
                'color': color
            }]
        }
        return self.data

    async def _send_message(self):
        return await self.request('post', self.url, json=self.data)
