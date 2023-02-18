# Lab: 34 - API Deployment

## Overview

It's time to deploy!

First steps are to make sure your Application is able to run well in a remote environment.

Once you are confident that your Application is \*deployable` then time to research deployment options.

## Feature Tasks and Requirements

### Use API Quick Start Template

-   Create a new repo `cookie-stand-api` that uses [API Quick Start](https://github.com/codefellows/python-401-api-quickstart){:target="\_blank"} as a template.
-   Modify your application using instructions in README.md found in root of repo.
    -   Change `things` app folder to be `cookie_stands`
    -   Go through code base looking for `Thing`,`thing` and `things` change to cookie-stand related names.
    -   E.g. `Thing` model becomes `CookieStand`
    -   E.g. `ThingList` becomes `CookieStandList`
-   Pro Tip: Do a global text search looking for `thing`
    -   Search should be case insensitive.

### Deeper CookieStand Changes

-   The `CookieStand` model must contain

```python
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
```

Notice the use of [JSONField](https://docs.djangoproject.com/en/3.1/ref/models/fields/#jsonfield){:target="\_blank"} which is a newer feature introduced in Django 3.1.

### Database Deployment Requirements

-   Host your Database at [ElephantSQL](https://www.elephantsql.com/){:target="\_blank"}

### Site Deployment Requirements

-   Deploy Docker container to Heroku

&nbsp;

**PR Link**: <https://github.com/YAHIAQOUS/cookie-stand-api/pull/1>

**ElephantSQL Database Deployment**: <https://api.elephantsql.com/console/129fdd3c-d3a1-4b4f-95d0-5c91c97e1d76/browser?#>

**Heroku API Lists**: <https://cookie-stands-34.herokuapp.com/api/v1/cookie_stands/>
