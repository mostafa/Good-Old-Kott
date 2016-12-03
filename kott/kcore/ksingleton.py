# -*- coding: utf-8 -*-
"""docstring."""


def kSingleton(class_instance):
    """docstring."""
    k_instances = {}

    def get_instance():
        """docstring."""
        if class_instance not in k_instances:
            k_instances[class_instance] = class_instance()
        return k_instances[class_instance]

    return get_instance
