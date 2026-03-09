from typing import Callable, List, Type, Any
import functools


def circuit_breaker(
        state_count: int,
        error_count: int,
        network_errors: List[Type[Exception]],
        slep_time_sec: int
) -> Callable:
    if state_count <= 10:
        raise ValueError("state_count must be > 10")
    if error_count >= 10:
        raise ValueError("error_count must be < 10")

    def decorator(fn) -> Callable:
        history: List[Any] = []
        errors: int = 0
        last_error_time: float = 0.0

        @functools.wraps(fn)
        def wrapper(*args, **kwargs) -> Any:
            res = fn(*args, **kwargs)
            return res
        return wrapper
    return decorator
