# -*- coding: utf-8 -*-
"""Pre-baked reports

Set of reports that can be called from code or executed using
the zaius-export command line utility.

    Example:
        zaius-export demo

"""
from .spec import ReportSpec
from . import product_attribution
from . import lifecycle_progress
from . import email_metrics
from . import daily_content
from . import daily_content_salenum


SPECS = ReportSpec.specs
