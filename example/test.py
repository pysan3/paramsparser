from paramsparser import Yaml2Params

yaml_params = Yaml2Params()
print(yaml_params)

from paramsparser import Json2Params
json_params = Json2Params(params=yaml_params)
json_params.save()

from paramsparser import Config2Params
params = Config2Params()
params.save()
