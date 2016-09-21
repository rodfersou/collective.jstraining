from plone.app.testing import PloneSandboxLayer, PLONE_FIXTURE, \
    IntegrationTesting
from plone.testing import z2
from zope.configuration import xmlconfig


class CollectiveJSTrainingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.jstraining
        xmlconfig.file(
            'configure.zcml',
            collective.jstraining,
            context=configurationContext
        )
        z2.installProduct(app, 'collective.jstraining')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'collective.jstraining')


COLLECTIVE_JSTRAINING_FIXTURE = CollectiveJSTrainingLayer()

COLLECTIVE_JSTRAINING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_JSTRAINING_FIXTURE,),
    name="CollectiveJSTTrainingLayer:Integration"
)
