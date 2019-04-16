zaius-export: Zaius Data for Engineers
======================================

Build and automate aweseome reports. Like this:
``` {.sourceCode .python}
import datetime
import zaius.export as export

# count the users who clicked this week
last_week = datetime.date.today() - datetime.timedelta(days=7)
query = """
select user_id
from events
where
  event_type = 'email'
  and action = 'click'
  and ts > {}
""".format(last_week.strftime('%s')
rows = export.API().query(query)
print(len(set([r['user_id'] for r in rows])))
```

Or, use pre-baked reports. Like this:
``` {.sourceCode .bash}
$ zaius-export product-attribution '2019-1-1' '2019-1-31' --auth zaius-api.ini
$ zaius-export order-attribution '2019-1-1' '2019-1-31' --auth zaius-api.ini
```

## Authorization

API calls depend on having a set of credentials available to authenticate your request. By
default, all tools will look for these to be defined in $HOME/.zaius\_api.ini. This file
should look like this:
``` {.sourceCode .ini}
[auth]
aws_access_key_id: ***
aws_secret_access_key: ***
zaius_secret_key: ***
```

You can find the appropriate values for this file by logging into Zaius. Click the gear icon
next to your business name at the top left of the screen, select "APIs" from the menu on the
left (under Data Management), and then find your zaius\_secret\_key under the Private tab.

Your AWS credentials can be found in the Integrations section (same gear icon, Data Management,
integrations) by opening the AWS integration.
