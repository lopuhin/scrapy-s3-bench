# -*- coding: utf-8 -*-

import os.path

import scrapy
from scrapy.linkextractors import LinkExtractor
import vmprof


class Spider(scrapy.Spider):
    name = 'spider'

    def __init__(self):
        with open(os.path.join(
                os.path.dirname(__file__), '..', 'top-1k.txt')) as f:
            self.start_urls = ['http://{}'.format(line.strip()) for line in f]

        self.le = LinkExtractor()
        self.images_le = LinkExtractor(
            tags=['img'], attrs=['src'], deny_extensions=[])
        self.files_le = LinkExtractor(
            tags=['a'], attrs=['href'], deny_extensions=[])

        # Set up profiling
        self.profile_filename = _get_prof_filename('vmprof')
        self.profile = open(self.profile_filename, 'wb')
        vmprof.enable(self.profile.fileno())

        super(Spider, self).__init__()

    def parse(self, response):
        get_urls = lambda le: {link.url for link in le.extract_links(response)}
        page_urls = get_urls(self.le)
        for url in page_urls:
            yield scrapy.Request(url)
        file_urls = (
            get_urls(self.images_le) | get_urls(self.files_le) - page_urls)
        yield {
            'url': response.url,
            'file_urls': file_urls,
        }

    def closed(self, _):
        vmprof.disable()
        self.profile.close()
        self.logger.info('vmprof saved to {}'.format(self.profile_filename))


def _get_prof_filename(prefix):
    i = 1
    while True:
        filename = '{}_{}.vmprof'.format(prefix, i)
        if not os.path.exists(filename):
            return filename
        i += 1
