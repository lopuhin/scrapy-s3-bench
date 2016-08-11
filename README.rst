Scrapy S3 file pipeline benchmark
=================================

Run::

    scrapy crawl spider \
        -s FILES_STORE=s3://some-bucket/some-prefix/ \
        -s AWS_ACCESS_KEY_ID=some-key \
        -s AWS_SECRET_ACCESS_KEY=some-secret

For reproducible runs, clean storage (or change location) before each run!
