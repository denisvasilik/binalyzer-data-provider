# -*- coding: utf-8 -*-
"""
    binalyzer_data_provider.io
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Data providers are used by templates for reading, modifying or writing data.

    :copyright: 2020 Denis Vasilík
    :license: MIT
"""

from binalyzer_core import DataProvider


class BufferedIODataProvider(DataProvider):

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def read(self, template):
        """Read from the buffered IO :attr:`~binalyzer.binalyzer.BindingContext.stream`
        using the position given by the :attr:`~binalyzer.binalyzer.BindingContext.template`.
        """
        absolute_address = template.absolute_address.value
        size = template.size.value
        self.data.seek(absolute_address)
        return self.data.read(size)

    def write(self, template, value):
        """Write to the buffered IO :attr:`~binalyzer.binalyzer.BindingContext.stream`
        using the position given by the :attr:`~binalyzer.binalyzer.BindingContext.template`.
        """
        self.data.seek(template.absolute_address.value)
        self.data.write(value)
