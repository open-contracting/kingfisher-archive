Contributing
============

Kingfisher Archive operates on GBs of data. As such, it tries to be bound only by I/O, by doing the following:

-  Cache the results of calculations.
-  Avoid expensive calculations, by postponing them and returning early, where possible.
-  Use `xxHash <https://cyan4973.github.io/xxHash/>`__ to calculate checksums of OCDS data, which is faster than DDR4 SDRAM's transfer rate. (Find your RAM's description by running ``lshw -short -C memory`` and `look up its transfer rate <https://en.wikipedia.org/wiki/List_of_interface_bit_rates#Dynamic_random-access_memory>`__.)