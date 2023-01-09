# YAML parameter loader for PlatformIO
This is a small script (`load-yaml.py`) that can load YAML files as variables in CPP for uploading to microcontollers.

## How it works
The script looks for a YAML file (defined by the environment variable `MCU_PARAMS_FILE`), and recursively defines all the properties in it in CPP, adding `param_` as a prefix.

E.g., if your YAML file is like:
```yaml
la:
    kp: 5.0
    ki: 3.5
    kd: 0.0
throttle:
    max: 4096
```

In the CPP files in the project, you will now be able to access the following variables:
- `param_la_kp`
- `param_la_ki`
- `param_la_kd`
- `param_throttle_max`

In addition, the variable `yaml_params` will also be defined, to indicate that parameters have been loaded from YAML.

## Usage
### 1. Set the path of the YAML file
Set the absolute path of the paramters YAML file in the environment variable `MCU_PARAMS_FILE`.

E.g. you could set this in your `.bashrc`:
```bash
export MCU_PARAMS_FILE="/home/abhiyaan2/mcu-params.yml"
```

If this variable is not set, the script looks for `mcu-params.yml` in the same folder as `platformio.ini`.

### 2. Copy files and add config
Copy `load-yaml.py` into your platformio project folder, and add this line under the `[env:...]` section in your `platformio.ini`:

```ini
[env:uno] # or whichever else is there in your platformio.ini

# ...

extra_scripts =
    post:load-yaml.py
```

### 3. Add definitions for parameters in your CPP
The above 2 steps should actually be enough for loading parameters into cpp. However, VSCode won't detect that the parameters have been loaded so it will keep yelling at you. To make it calm down, you need to add whatever parameters you are using to the top of your cpp file.

E.g.
```cpp
#include "Arduino.h"

// The values you supply here aren't actually used and will be overwritten by the ones in the YAML file. This is solely to make VSCode shut up. `yaml_params` will be defined if the yaml config is loaded, so this block will never execute.
#ifndef yaml_params

#define param_la_kp 666.0
#define param_la_ki 69.0
#define param_la_kd 420.0

#endif

// now we can do stuff with the parameters mentioned above without VSCode throwing errors
```

This step is only for VSCode, and it won't change anything when you are building via platformio.