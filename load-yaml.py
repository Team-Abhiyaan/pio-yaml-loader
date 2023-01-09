import os
import yaml

# we only want to load variable definitions into the current project
Import("projenv")

# look for the environment variable MCU_PARAMS_FILE
yaml_file_location = os.getenv("MCU_PARAMS_FILE", default="mcu-params.yml")

print("using YAML file at %s" % yaml_file_location)

# load YAML file
dictionary = yaml.load(open(yaml_file_location, "r"), yaml.Loader)

print(projenv.Dump())

# list of definitions we are going to pass to the compiler
defines = [("yaml_params")] # by default we define "yaml_params" so that we can check #ifdef

# recursively add definitions from our YAML file
# `dictionary` is an element containing other keys
# `path` is the name appended to the prefix of all definitions
def append_keys(dictionary, path):
    for key in dictionary:
        if type(dictionary[key]) is dict:
            append_keys(dictionary[key], path + "_" + key)
        else:
            defines.append((path + "_" + key, dictionary[key]))

# every parameter in the yaml file will be imported with a prefix of `param_`
append_keys(dictionary, "param")

projenv.Append(CPPDEFINES=defines)