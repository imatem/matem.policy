# -*- coding: utf-8 -*-

from five import grok
from matem.event import _
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.autoform import directives as form
from plone.supermodel import model
from zope import schema


class IPage(model.Schema):
    """A folder for Seminars.
    """

    title_en = schema.TextLine(
        title=_(
            u'label_page_title',
            default=u'Title'
        ),
        description=_(
            u'help_page_title',
            default=u'Title in english'
        ),
        required=False,
    )

    form.widget('body_es', WysiwygFieldWidget)
    body_es = schema.Text(
        title=_(
            u'label_seminar_details',
            default=u'Details'
        ),
        description=_(
            u'help_seminar_details',
            u'Details about the seminar'
        ),
        required=False,
    )

    form.widget('body_en', WysiwygFieldWidget)
    body_en = schema.Text(
        title=_(
            u'label_seminar_details',
            default=u'Details'
        ),
        description=_(
            u'help_seminar_details',
            u'Details about the seminar in english'
        ),
        required=False,
    )

    ##TODO: Add the details field for english


class View(grok.View):
    grok.context(IPage)
    grok.require('zope2.View')
