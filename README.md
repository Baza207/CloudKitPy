# CloudKitPy
CloudKitPy - A python wrapper around CloudKit Web Services for server-to-server connections.

[![Build Status](https://travis-ci.org/Baza207/CloudKitPy.svg?branch=master)](https://travis-ci.org/Baza207/CloudKitPy)

## Under Development

This project is still under initial development. This means parts of it may incomplete or not fully tested in it's current state, and probably shouldn't not yet be used in production projects yet.

## Overview
CloudKitPy is built to be a wrapper around [CloudKit Web Services](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Introduction/Introduction.html), similar to how [CloudKit JS](https://developer.apple.com/library/ios/documentation/CloudKitJS/Reference/CloudKitJavaScriptReference/index.html) is. Because of this it has been designed around the native framework and CloudKit JS's structure to allow ease of transition between platforms.

## Prerequisites
Before you can make connection to CloudKit you must  first setup CloudKit via an iOS or OS X app. Also, you need to have created a server-to-server key and set it in the CloudKit dashboard for your app. For more details on both of these steps, please refer to [Apple's Documentation](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/SettingUpWebServices/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6).

This framework is based on Python 2.7 (with plans to add support for Python 3.4 and 3.5 in the future).

## Installation
To install CloudKitPy follow the steps below:

1. `cd` into the root directory via the terminal,
2. Run `python setup.py install`
3. You're installed! Just add `import cloudkitpy` into your project to get started.

**Note:** In the future I am planning to submit this to allow installation via `pip`. However I want this framework to be a lot more fleshed out before I do that.

## Basic Setup
To setup a CloudKit instance to connect to CloudKit, use the following code:

```python
from cloudkitpy.datatypes import ContainerConfig
from cloudkitpy.datatypes import CloudKitConfig
from cloudkitpy.cloudkit import CloudKit

my_container = ContainerConfig(
    '<your container id>',
    CloudKit.DEVELOPMENT_ENVIRONMENT,   # Or CloudKit.PRODUCTION_ENVIRONMENT for production
    server_to_server_key='<your server-to-server key id>',
    cert_path='<path to your private key>'
)
cloudkit_config = CloudKitConfig([my_container])
ck = CloudKit(cloudkit_config, log_path='log.txt')
container = ck.get_default_container()
```

Now to get the current user and print it's record name, all you have to do is:

```python
result = container.fetch_user_info()
if result.is_success is True:
    print result.value.user_record_name
```

Further examples for setup and basic container and database operations can be found in the [Wiki](https://github.com/Baza207/CloudKitPy/wiki/Examples).

## Create, Save, Fetch and Modify Record Example
Below is a basic example that will do the following:

- Create a `Person` record for John Appleseed, aged 24
- Save it to the public database
- Use that saved record to fetch the record back from the server
- Update the age to 25 and re-save it
- Print the result after the second save

(The code below assumes you have a setup a `my_container` object, as shown above.)

```python
database = my_container.public_cloud_database

# Save a new record
record = Record()
record.record_type = 'Person'
fields = {
    'first_name': 'John',
    'last_name': 'Appleseed',
    'age': 24
}
record.fields = CKValue.fields(fields)

result = database.save_records([record])
if result.is_failure is True:
    ck.logger.error(
        "Failed to save record: %s" % result.error.server_error_code
    )
elif result.is_success is True:
    ck.logger.info(
        "Saved record successfully!"
    )
    record = result.value[0] # This record is with the name, change tag, etc returned from the save

# Fetch the record
result = database.fetch_records([record]) # This uses the returned record with the name, change tag, etc
if result.is_failure is True:
    ck.logger.error(
        "Failed to fetch records: %s" % result.error.server_error_code
    )
elif result.is_success is True:
    ck.logger.info(
        "Fetched records successfully!"
    )
    record = result.value[0] # This should then be the fetched record

# Modify and re-save the record
record.fields['age'] = CKValue(25).json() # For a single value this works the same as `CKValue.fields(fields)` without having to create a dictionary of the whole record and then back to a record
result = database.save_records([record])
if result.is_failure is True:
    ck.logger.error(
        "Failed to modify records: %s" % result.error.server_error_code
    )
elif result.is_success is True:
    record = result.value[0]
    ck.logger.info(
        "Modified records successfully! %s %s is %d years old" % (
            CKValue(json=record.fields['first_name']).value,
            CKValue(json=record.fields['last_name']).value
            CKValue(json=record.fields['age']).value
        )
    )
```

## Contributions

If you would like to contribute, please create an issue first before creating a pull request, just incase I am already working on that part of the project.

## Roadmap
- [x] Create wrappers for base parts of the CloudKit framework (data types, containers, databases and configuring)
- [x] Implement an error handling system and logging
- [ ] **[IN PROGRESS]** Create Example Code
- [ ] Add support for Python 3.4 and 3.5
- [ ] Continue with further wrappers for remaining parts of CloudKit
- [ ] Upload and download assets
- [ ] Expand Example Code
- [ ] Async Callbacks
- [ ] Expand for API usage for non-server-to-server usage
- [ ] Comprehensive Unit Test Coverage
- [ ] Complete Documentation

Below is listed the sections of CloudKit that are being created in CloudKitPy. This is a continuous list and will be added to and updated as development continues.

- [x] CloudKit
    - [x] Configuration
    - [x] Container Management
    - [x] Constants
- [x] Data Types
    - [x] Asset
    - [x] Filter
    - [x] Location
    - [x] Notification Info
    - [x] Query
    - [x] Record
    - [x] Reference
    - [x] Sort Descriptor
    - [x] Subscription
    - [x] User Info
    - [x] Zone
    - [x] Zone ID
    - [x] CloutKit Config
    - [x] Container Config
- [x] CKValue (mostly implemented, needs some expansion of `type` but the basic principle works)
- [x] CKError
- [x] Container
    - [x] Configuration
    - [x] Private and Public database creation
    - [x] Discovering Users
- [x] Database
    - [x] Accessing Records
    - [x] Syncing Records
    - [x] Accessing Record Zones
- [ ] **[IN PROGRESS]** Records Batch Builder
- [ ] Response
    - [ ] Record Zones Response
        - [ ] Changed Records Response
        - [ ] Query Response
    - [ ] Subscriptions Response
    - [ ] User Info Response

## License

[MIT Licence](LICENSE)

## Creator

[James Barrow](james@pigonahill.com)
