<p align="center">
    <img src="../../static/images/geoffrey-logo.png">
</p>

# geoff add data-source

```shell
geoff add data-source [OPTIONS] NAME
```

Adds a new folder in data_sources folder called `NAME` which contains a metadata markdown document to populate. The metadata file captures some details about the data source and any key people that were involved in the collection or authorisation to access the data.

There are three different metadata templates that are created depending on whether the data source is a 

<img src="../../static/images/db.png" height="25px" width="25px" style="vertical-align: middle;"> database source  
  
<img src="../../static/images/folder.png" height="25px" width="25px" style="vertical-align: middle;"> extract source  
  
<img src="../../static/images/cloud-download.png" height="25px" width="25px" style="vertical-align: middle;"> 
web download source

## Arguments

`name`
The name of the data sources

Data source name

```shell
foo@bar:~$ geoff create iris
```

If no options are passed a directory is created with an empty metadata.md

## Options

`--parents` \ `--no-parents`

Default: `--no-parents`

Whether to create the parents of the supplied path or not.

`--help`
Shows help message and exits

## Examples

Create a project

```shell
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

Create a project and parents of specified path

```shell
foo@bar:~$ geoff create --parents path/to/test_project
🚀 test_project created!

test_project
├── 🖿 data_sources
├── 🖿 explorations
├── 🖿 models
├── 🖿 products
├── 🗋 README.md
└── 🗋 project_scoping.md
```
