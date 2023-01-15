from typing import Any, cast

def my_function(var: Any) -> Any:
    return var

print(cast(str,my_function(1.2)))