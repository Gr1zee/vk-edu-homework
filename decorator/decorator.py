from typing import Callable, List, Type, Any
from collections import deque

import time
import functools


class NotAliveError(Exception):
    def __init__(self, message: str = "Сервер не отвечает"):
        super().__init__(message)


def circuit_breaker(
    state_count: int,
    error_count: int,
    network_errors: List[Type[Exception]],
    sleep_time_sec: int,
) -> Callable:
    if state_count <= 10:
        raise ValueError("state_count must be > 10")
    if error_count >= 10:
        raise ValueError("error_count must be < 10")

    def decorator(fn) -> Callable[[Callable], Callable]:
        history = deque(maxlen=state_count)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs) -> Any:
            if len(history) >= error_count:
                recent_errors = list(history)[-error_count:]
                if all(not success for success in recent_errors):
                    raise NotAliveError()

            if history and history[-1] is False:
                time.sleep(sleep_time_sec)
            try:
                res = fn(*args, **kwargs)
                history.append(True)
            except tuple(network_errors):
                history.append(False)
                raise
            except Exception:
                raise

            return res

        return wrapper

    return decorator
