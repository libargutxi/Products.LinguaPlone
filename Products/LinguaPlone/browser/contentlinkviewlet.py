from Acquisition import aq_inner, aq_parent
from AccessControl.SecurityManagement import getSecurityManager
from zope.component import getMultiAdapter
from plone.app.layout.viewlets import ViewletBase
class MultilingualContentViewlet(ViewletBase):

    def update(self):
        # We have to check the view permission on the translated object, because
        # getTranslations returns all objects, no matter the workflow state

        context = aq_inner(self.context)
        current = context.Language()
        context_state = getMultiAdapter(
            (context, self.request), name=u'plone_context_state')
        context = context_state.canonical_object()
        _checkPermission = getSecurityManager().checkPermission
        self.translations = []
        for lang, content in context.getTranslations(review_state=False).items():
            if lang != current and _checkPermission('View', content):
                self.translations.append(content)

