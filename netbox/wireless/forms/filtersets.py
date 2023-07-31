from django import forms
from django.utils.translation import gettext_lazy as _

from dcim.choices import LinkStatusChoices
from netbox.forms import NetBoxModelFilterSetForm
from tenancy.forms import TenancyFilterForm
from utilities.forms import add_blank_choice
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField
from wireless.choices import *
from wireless.models import *

__all__ = (
    'WirelessLANFilterForm',
    'WirelessLANGroupFilterForm',
    'WirelessLinkFilterForm',
)


class WirelessLANGroupFilterForm(NetBoxModelFilterSetForm):
    model = WirelessLANGroup
    parent_id = DynamicModelMultipleChoiceField(
        queryset=WirelessLANGroup.objects.all(),
        required=False,
        label=_('Parent group')
    )
    tag = TagFilterField(model)


class WirelessLANFilterForm(TenancyFilterForm, NetBoxModelFilterSetForm):
    model = WirelessLAN
    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        (_('Attributes'), ('ssid', 'group_id', 'status')),
        (_('Tenant'), ('tenant_group_id', 'tenant_id')),
        (_('Authentication'), ('auth_type', 'auth_cipher', 'auth_psk')),
    )
    ssid = forms.CharField(
        required=False,
        label=_('SSID')
    )
    group_id = DynamicModelMultipleChoiceField(
        queryset=WirelessLANGroup.objects.all(),
        required=False,
        null_option='None',
        label=_('Group')
    )
    status = forms.ChoiceField(
        label=_('Status'),
        required=False,
        choices=add_blank_choice(WirelessLANStatusChoices)
    )
    auth_type = forms.ChoiceField(
        label=_('Authentication type'),
        required=False,
        choices=add_blank_choice(WirelessAuthTypeChoices)
    )
    auth_cipher = forms.ChoiceField(
        label=_('Authentication cipher'),
        required=False,
        choices=add_blank_choice(WirelessAuthCipherChoices)
    )
    auth_psk = forms.CharField(
        label=_('Pre-shared key'),
        required=False
    )
    tag = TagFilterField(model)


class WirelessLinkFilterForm(TenancyFilterForm, NetBoxModelFilterSetForm):
    model = WirelessLink
    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        (_('Attributes'), ('ssid', 'status',)),
        (_('Tenant'), ('tenant_group_id', 'tenant_id')),
        (_('Authentication'), ('auth_type', 'auth_cipher', 'auth_psk')),
    )
    ssid = forms.CharField(
        required=False,
        label=_('SSID')
    )
    status = forms.ChoiceField(
        label=_('Status'),
        required=False,
        choices=add_blank_choice(LinkStatusChoices)
    )
    auth_type = forms.ChoiceField(
        label=_('Authentication type'),
        required=False,
        choices=add_blank_choice(WirelessAuthTypeChoices)
    )
    auth_cipher = forms.ChoiceField(
        label=_('Authentication cipher'),
        required=False,
        choices=add_blank_choice(WirelessAuthCipherChoices)
    )
    auth_psk = forms.CharField(
        label=_('Pre-shared key'),
        required=False
    )
    tag = TagFilterField(model)
