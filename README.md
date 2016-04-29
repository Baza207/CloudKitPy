# CloudKitPy
CloudKitPy - A python wrapper of CloudKit Web Services for server-to-server connections.

[![Build Status](https://travis-ci.org/Baza207/CloudKitPy.svg?branch=master)](https://travis-ci.org/Baza207/CloudKitPy)

## Under Development

This project is still under initial development. This means it is incomplete in it's current state and should not yet be used in production projects.

## Prerequisites
Before you can make connection to CloudKit you must  first setup CloudKit via an iOS app. Also you need to have created a server-to-server key and set it in the CloudKit dashboard. For more details on both of these steps, please refer to [Apple's Documentation](https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/SettingUpWebServices/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6).

This framework is based on Python 2.7.

## Installation
To install CloudKitPy follow the steps below:

1. `cd` into the root directory via the terminal,
2. Run `python setup.py install` (note you may have to `sudo` this),
3. You're installed, just `import cloudkitpy` into your project to get started.

**Note:** In the future I am planning to submit this to allow installation via `pip`. However I want this framework to be a lot more fleshed out before I do that.

## Basic Connection Setup
To setup a CloudKit instance to connect to CloudKit, use the following code:

```python
from cloudkitpy.ckdatatypes import ContainerConfig
from cloudkitpy.ckdatatypes import CloudKitConfig
from cloudkitpy.cloudkit import CloudKit

my_container = ContainerConfig(
    '<your container id>',
    'development',
    server_to_server_key='<your server-to-server key id>',
    cert_path='<path to your private key>'
)
cloudkit_config = CloudKitConfig([my_container])
ck = CloudKit(cloudkit_config)
ck.get_current_user()
```

**Note:** `get_current_user()` is currently just a test function to make sure that the request is being created correctly. This will change in the future when the framework progresses. Therefor this might have been moved or changed before the documentation is updated.

## Contributions

If you would like to contribute, please create an issue first before creating a pull request, just incase I am already working on that part of the project.

## Roadmap

A roadmap will be up shortly defining what operations are planned and the priority.

## License

[MIT Licence](LICENSE)

## Creator

[James Barrow](james@pigonahill.com)
