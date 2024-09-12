# djangoSRI

Conceptual, logical and archetype data model for the [Smart Readiness Indicator (SRI). ](https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/smart-readiness-indicator_enr) . We use the 3DCityDB as a database and Django as a framework to provide a REST API and a GIS based web application.

The concept is illustrated in the following figure:

![20240824_GraphicalAbstract.drawio.png](img/20240824_GraphicalAbstract.drawio.png)

The project consists of thre main parts.

1. Data Needs for the SRI and its functionality levels.
2. Digital Archetypes, that reflect examplary technologies for the SRI and its functionality levels.
3. A data model, extending the 3DCityDB and ADE schema.
4. A django app, that allows for a quick start of a project using the data model and parameterizing CityGML buildings with the data needs and digital archetypes.

# 3DCityDB with SRI for Django

## Introduction

The `django-sri` application is an interface to 3DCityDB with extensions of djanoSRI. We are schema-compliant with 3DCityDB and ADE.

Under data, information about mapped data and the SRI and its functionality levels is stored.

In addition this app will offer Django templates and static Java scripts that can be used for a GIS based web application with various pre-defined functions. Feel free to use and change them for you specific project.

To run this app you'll have to have access to a `PostGIS PostgreSQL` and `InfluxDB`
database, we assume that you'll set up Django project and a python environment with
dependencies and corresponding environment variables. As a template you can use
[vDistrict](https://github.com/TUB-DVG/vDistrict), where you'll also find detailed instructions for isntallation of
databases and your python environment.

This application is developed by `DVG`, if you have any questions don't hesitate to
contact [us](mailto:info@dvg.tu-berlin.de). The goal is to publish
it as open-source software.

## Install python package `django-sri` and its dependencies in your project 

To install the `django-sri` package itself do the following:

- Clone this repository into your desired folder:

        $ git clone [SSH-Key/Https]


- Use pip to install the local copy of `django-sri` (the path should point to the folder that contains this `README`):

        $ pip install -e [Path/to/your/django-sri/Clone]


## Install Install python package `django-sri` as a part of vdistrict

To install the `django-sri` package itself do the following:

- Clone this repository into your desired folder:

        $ git clone [SSH-Key/Https]


- Use pip to install the local copy of `django-sri` (the path should point to the folder that contains this `README`):

        $ pip install -e [Path/to/your/django-citydb/Clone]



## Quick start to use `django-citydb` in your personal Django project

We assume you have followed installation instructions above (including setting
up the databases or having databases available).

1. Add `sridb` to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = [
        ...
        'sridb',
        ]

2. Include the `sridb` URLconf in your project `urls.py`, with its required dependencies, like this::

        from django.conf.urls import url
        from django.urls import include
        url(r'^sridb/', include('sridb.urls')),

3. Run to create and synchronize the models (after the first `migrate` you will
    get some errors, that the table `building` already exists, please just ignore it)

        $ python manage.py migrate sridb
        $ python manage.py migrate --fake-initial

5. Visit http://127.0.0.1:8000/citydb/ to test if installation worked

## Version

This is version 0.1.0


## How to cite?

Publication will be available soon.

- 


## How to contribute?

Thanks for contributing! Please follow our [contributors guide](./docs/contributor.md)

## License

MIT.


## Acknowledgements

`django-citydb` has been developed within public funded projects
and with financial support by BMWk (German Federal Ministry for Economic Affairs and Climate Action) by the Institute for Energy Efficient Buildings and Indoor Climate. It is now maintained by the Begleitforschung Energiewendebauen - Modul Digitalisierung.


<img src="img\bmwk-logo-2022-en-web-transparent.gif" width="200">
