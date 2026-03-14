import os

from solution.secrets_accessor import MODE_ENV_VAR, RunMode

os.environ[MODE_ENV_VAR] = RunMode.TEST.value
