from typing import Any, cast

def my_function(var: Any) -> Any:
    return var

print(cast(str,my_function(1.2)))
print(cast(int,my_function(1.2)))
print(cast(float,my_function('hello')))