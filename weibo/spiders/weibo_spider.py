# -*- coding: utf-8 -*-
import scrapy
import json
from weibo.items import WeiboItem
import time
class WeiboSpiderSpider(scrapy.Spider):
    name = 'weibo_spider'
    allowed_domains = ['api.weibo.cn']
    start_urls = ['https://api.weibo.cn/2/cardlist?networktype=wifi&launchid=10000365--x&sensors_device_id=bcc77522d54cc711&orifid=231619&moduleID=708&wb_version=4178&c=android&s=06637c79&ft=0&ua=samsung-SM-G9287__weibo__9.11.4__android__android7.0&wm=4260_0001&aid=01A-zfja7FHVWLKeL4i44Zj-9JewjRQ3h5tHPAvnwxRATTlJI.&ext=orifid%3A231619%7Coriuicode%3A10000010&fid=23114600418008631000000000000&lat=31.28269&lon=121.45144&uid=2729198317&v_f=2&v_p=78&from=109B495010&gsid=_2A25w50tTDeTxGeRJ6VsQ-SbPyjuIHXVRtdmbrDV6PUJbkdAKLWHNkWpNUnrQDqEZFa6czlKMoSrUIy7pwz8nvPpW&imsi=460097543801710&lang=zh_CN&lfid=231619&page=2&skin=default&count=20&oldwm=4260_0001&sflag=1&oriuicode=10000010&containerid=23114600418008631000000000000&ignore_inturrpted_error=true&luicode=10000010&sensors_mark=0&android_id=bcc77522d54cc711&need_new_pop=1&sensors_is_first_day=true&need_head_cards=0&cum=38388508']

    def parse(self, response):
        try:
            weibo_data=json.loads(response.text)['cards'][0]['card_group']
            for oneblog in weibo_data:
                weiboItem=WeiboItem()
                mblog=oneblog['mblog']
                weiboItem['mblogid']=mblog['id']
                weiboItem['created_at']=mblog['created_at']
                weiboItem['content']=mblog['text']
                weiboItem['pic_count']=len(mblog['pic_ids']) if 'pic_ids' in mblog else 0
                weiboItem['username']=mblog['user']['name']
                weiboItem['gender']=mblog['user']['gender']
                weiboItem['followers_count']=mblog['user']['followers_count']
                weiboItem['friends_count']=mblog['user']['friends_count']
                weiboItem['statuses_count']=mblog['user']['statuses_count']
                weiboItem['user_created_at']=mblog['user']['created_at']
                weiboItem['location']=mblog['tag_struct'][0]['tag_name'] if 'tag_struct' in mblog else '上海'
                yield weiboItem
        except:
            pass
        now = int(time.time())
        next = 'https://api.weibo.cn/2/cardlist?networktype=wifi&launchid=10000365--x&sensors_device_id=bcc77522d54cc711&orifid=231619&moduleID=708&wb_version=4178&c=android&s=06637c79&ft=0&ua=samsung-SM-G9287__weibo__9.11.4__android__android7.0&wm=4260_0001&aid=01A-zfja7FHVWLKeL4i44Zj-9JewjRQ3h5tHPAvnwxRATTlJI.&ext=orifid%3A231619%7Coriuicode%3A10000010&fid=23114600418008631000000000000&lat=31.28269&lon=121.45144&uid=2729198317&v_f=2&v_p=78&from=109B495010&gsid=_2A25w50tTDeTxGeRJ6VsQ-SbPyjuIHXVRtdmbrDV6PUJbkdAKLWHNkWpNUnrQDqEZFa6czlKMoSrUIy7pwz8nvPpW&imsi=460097543801710&lang=zh_CN&lfid=231619&page=2&skin=default&count=20&oldwm=4260_0001&sflag=1&oriuicode=10000010&containerid=23114600418008631000000000000&ignore_inturrpted_error=true&luicode=10000010&sensors_mark=0&android_id=bcc77522d54cc711&need_new_pop=1&sensors_is_first_day=true&need_head_cards=0&cum=38388508&time='+str(now)
        if now<1576554421:
            yield response.follow(next, self.parse)
