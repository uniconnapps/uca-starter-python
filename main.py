# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from uniconnapps import connector

#Replace with your config
uca_client = connector.UcaClient(
  connector_endpoint="uca://xxxxxxx.xxx",
  app_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  client_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  )

@uca_client.action
def addition(number1:float, number2: float) -> float:
    return number1 + number2

@uca_client.action
def subtraction(number1:float, number2: float) -> float:
    return number1 - number2

@uca_client.action
def multiplication(number1:float, number2: float) -> float:
    return number1 * number2

@uca_client.action
def division(number1:float, number2: float) -> float:
    return number1 / number2

if __name__ == '__main__':
    uca_client.run_forever()
    
