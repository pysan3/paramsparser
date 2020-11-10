from paramsparser import Json2Params
from paramsparser import Yaml2Params

params = Yaml2Params()
print(params)
params = Json2Params(params=params)
