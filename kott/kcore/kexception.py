# -*- coding: utf-8 -*-
"""Exception handling decorator for functions and methods"""

import sys
import traceback


class kException(object):
    _function_ = None
    _exc_args_ = {}
    _result_ = None

    def __init__(self, function):
        self._function_ = function

    def __call__(self, *args, **kwargs):

        if kwargs.get("else_function") is not None:
            self._exc_args_["else_function"] = kwargs.pop("else_function")

        if kwargs.get("finally_function") is not None:
            self._exc_args_["finally_function"] = kwargs.pop("finally_function")
        # please visit: http://stackoverflow.com/questions/9005941/python-exception-decorator-how-to-preserve-stacktrace
        try:
            self._result_ = self._function_(*args)
        except Exception:
            exc_type, exc_instance, exc_traceback = sys.exc_info()
            formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
            message = '\n{0}\n{1}:\n{2}'.format(
                formatted_traceback,
                exc_type.__name__,
                exc_instance.message
            )
            raise exc_type(message)
        else:
            if self._exc_args_.get("else_function") is None:
                pass
            else:
                self._exc_args_["else_function"]()
        finally:
            if self._exc_args_.get("finally_function") is None:
                pass
            else:
                self._exc_args_["finally_function"]()

        return self._result_
