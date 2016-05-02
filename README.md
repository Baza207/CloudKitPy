# CloudKitPy
CloudKitPy - A python wrapper around CloudKit Web Services for server-to-server connections.

[![Build Status](https://travis-ci.org/Baza207/CloudKitPy.svg?branch=master)](https://travis-ci.org/Baza207/CloudKitPy)

## Under Development

This project is still under initial development. This means it is incomplete in it's current state and should not yet be used in production projects.

## Prerequisites
Before you can make connection to CloudKit you must  first setup CloudKit via an iOS app. Also you need to have created a server-to-server key and set it in the CloudKit dashboard. For more details on both of these steps, please refer to [Apple's Documentation](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/SettingUpWebServices/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6).

This framework is based on Python 2.7.

## Installation
To install CloudKitPy follow the steps below:

1. `cd` into the root directory via the terminal,
2. Run `python setup.py install`
3. You're installed, just `import cloudkitpy` into your project to get started.

**Note:** In the future I am planning to submit this to allow installation via `pip`. However I want this framework to be a lot more fleshed out before I do that.

## Basic Setup
To setup a CloudKit instance to connect to CloudKit, use the following code:

```python
from cloudkitpy.ckdatatypes import ContainerConfig
from cloudkitpy.ckdatatypes import CloudKitConfig
from cloudkitpy.cloudkit import CloudKit

my_container = ContainerConfig(
    '<your container id>',
    CloudKit.DEVELOPMENT_ENVIRONMENT,   # Or CloudKit.PRODUCTION_ENVIRONMENT for production
    server_to_server_key='<your server-to-server key id>',
    cert_path='<path to your private key>'
)
cloudkit_config = CloudKitConfig([my_container])
ck = CloudKit(cloudkit_config)
container = ck.get_default_container()
```

Now to get the current user and print it's record name, all you have to do is:

```python
result = container.fetch_user_info()
if result.is_success is True:
    print result.value.user_record_name
```

## Contributions

If you would like to contribute, please create an issue first before creating a pull request, just incase I am already working on that part of the project.

## Roadmap
- [x] Create wrappers for base parts of the CloudKit framework (data types, containers, databases and configuring)
- [x] Implement an error handling system and logging
- [ ] **[IN PROGRESS]** Continue with further wrappers for remaining parts of CloudKit
- [ ] Create Example Code
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
