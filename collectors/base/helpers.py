# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import time
import logging
import datetime
logger = logging.getLogger(__name__)


# Module API

def slugify(value):
    """Slugify string value.
    """
    value = re.sub(r'[\W_]+', '_', value)
    value = value.strip('_')
    value = value.lower()
    value = value[:63]  # Postgres limitation is 63
    return value


def parse_date(value, format):
    """Parse sting date.
    """
    return datetime.datetime.strptime(value, format).date()


def parse_datetime(value, format):
    """Parse sting datetime.
    """
    return datetime.datetime.strptime(value, format)


def start(name, message):
    """Start collector.
    """
    logger.info('Collector %s has been started(%s)', name, message)


def stop(name, message, sleep_hours=1):
    """Stop collector after sleep.
    """
    template = 'Collector %s has been stopped (%s) (will sleep %s hour(s) and exit)'
    logger.info(template, name, message, sleep_hours)
    time.sleep(sleep_hours*60*60)
    exit()
