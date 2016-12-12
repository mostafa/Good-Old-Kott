# -*- coding: utf-8 -*-
"""docstring."""


def kSingleton(class_instance):
    """docstring."""
    # protected instance
    _k_instances_ = {}

    def get_instance():
        """docstring."""
        if class_instance not in _k_instances_:
            _k_instances_[class_instance] = class_instance()
        return _k_instances_[class_instance]

    return get_instance
