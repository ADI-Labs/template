# ADI Labs Template

[![Build Status](https://travis-ci.org/ADI-Labs/template.svg?branch=master)](https://travis-ci.org/ADI-Labs/template)
[![Coverage Status](https://coveralls.io/repos/github/ADI-Labs/template/badge.svg?branch=master)](https://coveralls.io/github/ADI-Labs/template?branch=master)

This is a template for ADI Labs projects, using our default tech stack
(Python / Flask / Postgres). It has automated testing, linting, and code
coverage reports already set-up for you.

The TLDR is:
```bash
vagrant ssh
cd /vagrant
source config/settings.dev
flask develop
```

## Setup

We use [https://www.vagrantup.com/](Vagrant) and
[https://www.virtualbox.org/](Virtualbox) to set up our development
environment. After installing Vagrant, you'll want to navigate to
the project directory and run:

```bash
vagrant up
```

which should automatically bootstrap the development environment for
you.

## Environment Variables
We use environment variables to store our configuration. There are two
files you should care about: `config/settings.dev` and
`config/settings.test`, which store configuration for development and
testing. If you get a `flask not found` error, you probably need to run:
```bash
source config/settings.dev
```
in order to load all our configuration variables. (When you've loaded
your configuration, you should see `(app)` in front of your cursor).

## The Flask CLI

For development, we ues the new Flask command-line interface. For
obscure technical reasons relating to IP addresses and VMs, you'll need
to run `flask deploy` instead of `flask run` to access your app on your
host (non-VM) computer.

We also provide convenient a `flask pgcli` command that will open up a
[pgcli](http://pgcli.com/) shell to your postgres database (in case you
need to munge around for a little) and a `flask setup` which will setup
the database for you.

For a full list of commands, you can always use the `--help` flag (e.g.
`flask --help`)

## Testing

We use [http://flake8.pycqa.org/en/latest/](flake8) for our Python
linting and [http://doc.pytest.org/en/latest/](pytest) for our test
suite. To run them, you just need to:
```bash
flake8
```
or

```
source config/settings.test
py.test
```

Strictly speaking, you don't _have_ to `source settings.test` before
running `py.test`, but you'll delete everything in your development
database if you don't.


## File Structure
```
.
├── app/                -- Your standard Flask app structure
├── config
│   ├── bootstrap.sh    -- Script to bootstrap the Vagrant environment
│   ├── environment.yml -- Python dependencies
│   ├── settings.dev    -- Configuration for the dev environment
│   ├── settings.test   -- Configuration for the testing environment
│   └── setup.sql       -- Needed to bootstrap the postgres database
├── run.py              -- Magic needed for our `flask` commands
├── setup.cfg           -- Configuration for pytest and flake8
└── Vagrantfile
```
