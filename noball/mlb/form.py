#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from service.const import LEAGUE_TUPLES

__author__ = 'Shinichi Nakagawa'


class SearchForm(forms.Form):
    query_word = forms.CharField(max_length=255)


class PytagorasForm(forms.Form):
    year = forms.IntegerField(max_value=9999, required=True)
    league = forms.ChoiceField(choices=LEAGUE_TUPLES, required=True)