import datetime

from ocdskingfisherarchive.archive import Archive
from ocdskingfisherarchive.collection import Collection
from ocdskingfisherarchive.config import Config
from ocdskingfisherarchive.scrapy_log_file import ScrapyLogFile


def test_no_previous():
    """" No Previous collections have been archived. We should archive. """
    config = Config()
    database_archive = None
    database_process = None
    s3 = None

    archive = Archive(config, database_archive, database_process, s3)
    archive._get_exact_archived_collection = lambda c: None
    archive._get_last_archived_collection = lambda c: None

    collection = Collection(config, 1, 'scotland', datetime.datetime(2020, 9, 2, 5, 25, 00))
    collection.get_data_files_exist = lambda: True
    collection._scrapy_log_file_name = 'test.log'
    collection._scrapy_log_file = ScrapyLogFile('test.log')
    collection._scrapy_log_file._errors_sent_to_process_count = 0
    collection._scrapy_log_file._spider_arguments = {}

    assert True == archive.should_we_archive_collection(collection)  # noqa: E712


def test_no_previous_subset():
    """" No Previous collections have been archived. But this is a subset, so we should not archive. """
    config = Config()
    database_archive = None
    database_process = None
    s3 = None

    archive = Archive(config, database_archive, database_process, s3)
    archive._get_exact_archived_collection = lambda c: None
    archive._get_last_archived_collection = lambda c: None

    collection = Collection(config, 1, 'scotland', datetime.datetime(2020, 9, 2, 5, 25, 00))
    collection.get_data_files_exist = lambda: True
    collection._scrapy_log_file_name = 'test.log'
    collection._scrapy_log_file = ScrapyLogFile('test.log')
    collection._scrapy_log_file._errors_sent_to_process_count = 0
    collection._scrapy_log_file._spider_arguments = {'sample': 'true'}

    assert False == archive.should_we_archive_collection(collection)  # noqa: E712


def test_no_data_files():
    """" No Previous collections have been archived. But there are no data files, so we should not archive. """
    config = Config()
    database_archive = None
    database_process = None
    s3 = None

    archive = Archive(config, database_archive, database_process, s3)
    archive._get_exact_archived_collection = lambda c: None
    archive._get_last_archived_collection = lambda c: None

    collection = Collection(config, 1, 'scotland', datetime.datetime(2020, 9, 2, 5, 25, 00))
    collection.get_data_files_exist = lambda: False
    collection._scrapy_log_file_name = 'test.log'
    collection._scrapy_log_file = ScrapyLogFile('test.log')
    collection._scrapy_log_file._errors_sent_to_process_count = 0
    collection._scrapy_log_file._spider_arguments = {}

    assert False == archive.should_we_archive_collection(collection)  # noqa: E712