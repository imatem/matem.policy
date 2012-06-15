from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_matem_policy():
    """Set up the additional products required for the matem site policy.
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """

    # Load the ZCML configuration for the matem.policy package.
    fiveconfigure.debug_mode = True
    import matem.policy
    zcml.load_config('configure.zcml', matem.policy)
    fiveconfigure.debug_mode = False

    # We need to tell the testing framework that these product should be
    # available. This can't happen until after we have loaded the ZCML.
    # This is *only* necessary for packages outside the Products.*
    # namespace which are also declared as Zope 2 products, using
    # <five:registerPackage /> in ZCML.
    ztc.installProduct('Collage')

# The order here is important: We first call the (deferred) function
# which installs the products we need for the matem package.
# Then, we let PloneTestCase set up this product on installation.
setup_matem_policy()
ptc.setupPloneSite(products=['matem.policy'])


class TestCase(ptc.PloneTestCase):
    """We use this base class for all the tests in this package.
    If necessary, we can put common utility or setup code in here.
    """
