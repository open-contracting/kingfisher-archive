Use
===

Archive
-------

The application's command-line interface uses `process locking <https://pypi.org/project/python-pidfile/>`__, to ensure that only one archival process runs at one time.

.. code-block:: shell

   python manage.py archive

To do a dry run:

.. code-block:: shell

   python manage.py archive --dry-run

To see all options:

.. code-block:: shell

   python manage.py archive --help

Restore
-------

#. Access Amazon S3
#. Find and download the archive
#. Uncompress the archive, for example:

   .. code-block:: shell

      unlz4 source.tar.lz4

#. Extract the files, for example:

   .. code-block:: shell

      tar xvf source.tar

#. Load the files into `Kingfisher Process <https://kingfisher-process.readthedocs.io/en/latest/>`__
#. Delete the files, for example:

   .. code-block:: shell

      rm -f source.tar.lz4 source.tar
      rm -rf source/20200102_030405
      rmdir source

If you downloaded multiple archives for the same source, the above commands will only delete the individual archive.

.. note::

   Do not extract the files into Kingfisher Collect's ``FILES_STORE`` directory. Otherwise, they risk being archived again!

Maintain
--------

If a spider is renamed in Kingfisher Collect, the corresponding directory on Amazon S3 should be renamed, for easier lookup.
