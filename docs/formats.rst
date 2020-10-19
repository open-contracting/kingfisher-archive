Archival formats
================

This repository operates on the data collected by Kingfisher Collect.

Kingfisher Collect
------------------

`Kingfisher Collect <https://kingfisher-collect.readthedocs.io/en/latest/>`__ uses Scrapy to download OCDS data and store it on disk: consult `its documentation <https://kingfisher-collect.readthedocs.io/en/latest/#how-it-works>`__ for the file layout. Scrapy writes a log file for each crawl.

A crawl's directory is archived as a TAR file and compressed with LZ4. The log file is stored alongside the LZ4 file.

ocdsdata
--------

Before Kingfisher Collect, a bespoke framework (`ocdsdata <https://github.com/open-contracting/kingfisher-collect/tree/5435f5dcaa99d4c7c2c16e5dcef234ef823e1a37/ocdskingfisher>`__) was used, then ported to Scrapy. The last spider was ported from ``ocdsdata`` on 2019-08-27. Collecting data with ``ocdsdata`` produced a directory containing JSON files and a ``metadb.sqlite3`` file, which describes the collection process. The ``filestatus`` table has a ``fetch_success`` boolean column indicating whether the file (URL) was retrieved without error. If there were errors, a ``fetch_errors`` text column describes the error in a string of JSON.

Each directory is archived as a TAR file and compressed with LZ4.