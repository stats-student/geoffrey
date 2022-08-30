<p align="center">
    <img src="docs/static/images/geoffrey-logo.png">
</p>

<p align="center">
    <img src="https://github.com/danielyates2/geoffrey/actions/workflows/ci.yml/badge.svg" alt="ci">
    <a href="https://codecov.io/gh/danielyates2/geoffrey" > 
        <img src="https://codecov.io/gh/danielyates2/geoffrey/branch/main/graph/badge.svg?token=ZFU8ZYE9HG"/> 
    </a>
</p>

<p align="center">
A simple tool to automate the creation of some folders and files for my
data science projects
</p>

<h3>Introduction</h3>
Geoffrey is a tool to automate and standardise(ish) the admin in my data science projects by creating folders and common files to speed up project setup and ensure that every project has a similar layout.
<br>
My general workflow for a data science project consists of 4 steps:

* 📄 Data sources
* 🔎 Exploration
* 📈 Models
* 🎁 Products

Geoffrey allows you to create projects and add in each of these 4 components in a modular way.

The quickstart is below and the manual for the different commands is <a href="docs/geoff.md">here</a>

<h3>Quickstart</h3>
<h5>Installation</h5>

```console
foo@bar:~$ python -m pip install git+https://github.com/danielyates2/geoffrey#v0.1.1
Collecting git+https://github.com/danielyates2/geoffrey#v0.1.1
  Cloning https://github.com/danielyates2/geoffrey to /tmp/pip-req-build-3gtmwyf2
  Running command git clone -q https://github.com/danielyates2/geoffrey /tmp/pip-req-build-3gtmwyf2
  Installing build dependencies ... done
  ...
Successfully built geoffrey
```

<h5>Create a project</h5>

```console
foo@bar:~$ geoff create test_project
🚀 test_project created!

test_project
├── 🖿 data_sources
├── 🖿 explorations
├── 🖿 models
├── 🖿 products
├── 🗋 README.md
└── 🗋 project_scoping.md
```

<h5>Add a data source</h5>
<h5>Add an exploration</h5>
<h5>Add a model</h5>
<h5>Add a product</h5>


### Attribution
<a href="https://www.flaticon.com/free-icons/professor" title="icon">Logo icon created by Freepik - Flaticon</a>
