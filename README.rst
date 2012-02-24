Yet Another IRC Stats Site
~~~~~~~~~~~~~~~~~~~~~~~~~~

This will be something similar to pisg_ but Django_ based and
PostgreSQL_ backed.

.. _pisg: http://pisg.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _PostgreSQL: http://www.postgresql.org/

The idea is have a ZenIRCBot_ running on the same server, or a server
where the bot's Redis_ instance is accessible by this code base. It
will log everything said on IRC then generate stats like who talks the
most, what time of day, logs, etc. With options to disable any of
this.

.. _ZenIRCBot: https://github.com/wraithan/zenircbot
.. _Redis: http://redis.io/
