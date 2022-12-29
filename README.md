# uca-starter-python
Uniconnapp Quick Start Template for python users

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&repo=583330162)

# Building blocks of Uniconnapps
## UCA (Uniconnapps) Platform
- We need an account in Uniconnapps Platform to try examples or build demo apps.
- If you are not an existing user visit [uniconnapps.com](https://uniconnapps.com/) to get access. If you are an existing user login to [Uniconnapps Platform](https://platform.uniconnapps.com/)

## AppSpace
- It houses Apps and Users within it.
- For demo apps and simplicity sake, we can just start with a single space with name of the developer.

## App (Unified App)
- It is a typical demo project or a microservice

## UCA Client Object
- It is a main object in the application code
- It holds the identity, auth, config, etc. and it is specific to an App (Uniapp) in UCA platform.
- We use this object to register actions (functionalities) and send events.
- We can get all the parameters required to initialize this object in "Build -> Environment" section or use a portion of  "Sample Code" in "Build -> Code" section of [Uniconnapps Platform](https://platform.uniconnapps.com/).
 

# Usage
## Python Version
- The recommended python version is 3.10 but UCA client supports 3.7+
## Installing the SDK
Note: You can skip this step if you are using GitHub Codespaces

uniconnapps-connector is available on PyPI:
```console
$ pip install uniconnapps-connector
```
if you don't have pip command use -m pip
```console
$ python -m pip install uniconnapps-connector
```

## Steps to run
- Open main.py and replace UCA client initialization code according to your UCA App parameters
- The typical code needs to be replaced is
```python
uca_client = connector.UcaClient(
  connector_endpoint="uca://xxxxxxx.xxx",
  app_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  )
```
- Simply Run .py file using python interpreter
```console
$ python main.py
```
- You will typically see "Streaming Actions from UCA Cloud Queue..."
```console
...
Streaming Actions from UCA Cloud Queue...
Streaming Actions from UCA Cloud Queue...
Streaming Actions from UCA Cloud Queue...
```
- Now keep it running and check "Experience -> Actions" section in UCA platform (in Web Browser, you may need to refresh)
- Invoke Actions from browser directly

# Resources
- [NOTICE](https://github.com/uniconnapps/uca-starter-python/blob/main/NOTICE)
- [LICENSE](https://github.com/uniconnapps/uca-starter-python/blob/main/LICENSE)
