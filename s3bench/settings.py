# -*- coding: utf-8 -*-

BOT_NAME = 's3bench'

SPIDER_MODULES = ['s3bench.spiders']
NEWSPIDER_MODULE = 's3bench.spiders'

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/51.0.2704.84 Safari/537.36')

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 4

DOWNLOAD_MAXSIZE = 1*1024*1024

ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

CLOSESPIDER_TIMEOUT = 30
DOWNLOAD_TIMEOUT = 15

LOG_LEVEL = 'INFO'
