import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from astropy.coordinates import (CartesianRepresentation,CartesianDifferential,SphericalRepresentation,SphericalDifferential)
from astropy.coordinates import ICRS, Galactic, GalacticLSR, Galactocentric

def cartesian_3d(cf):
    """ Plots 3d vector velocities in cartesian coordinates 
    
    Parameters
    ----------
    cf : ICRS 
        ICRS coordinate frame representation in cartesian coordinates
    """
    assert cf.representation_type == CartesianRepresentation
    assert cf.differential_type == CartesianDifferential
    x = cf.x.value
    y = cf.y.value
    z = cf.z.value

    v_x = cf.v_x.value
    v_y = cf.v_y.value
    v_z = cf.v_z.value

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.quiver(x,y,z,v_x,v_y,v_z,normalize=True,length=10,linewidth=1,color='black')
    ax.set_xlabel('x (pc)')
    ax.set_ylabel('y (pc)')
    ax.set_zlabel('z (pc)')
    plt.show()

def equitorial_3d(cf):
    """ Plots 3d vector velocities in equitorial coordinates. Arrow heads aren't
    showing up for some reason
    
    Parameters
    ----------
    cf : ICRS 
        ICRS coordinate frame representation in equitorial coordinates 
    """    
    #assert cf.representation_type == SphericalRepresentation
    #assert cf.differential_type == SphericalDifferential

    ra = cf.ra.value
    dec = cf.dec.value
    d = cf.distance.value

    pmra = cf.pm_ra_cosdec.value
    pmdec = cf.pm_dec.value
    rv = cf.radial_velocity.value

    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    ax.quiver(ra,dec,d,pmra,pmdec,rv,normalize=True,color='black',linewidth=1)
    ax.set_xlabel('ra (deg)')
    ax.set_ylabel('dec (deg)')
    ax.set_zlabel('Distance (deg)')
    plt.show() 

def equitorial_2d(cf):
    """ Plots 2d vector velocities in equitorial coordinates. 
    
    Parameters
    ----------
    cf : ICRS 
        ICRS coordinate frame representation in equitorial coordinates 
    """    
    #assert cf.representation_type == SphericalRepresentation
    #assert cf.differential_type == SphericalDifferential

    ra = cf.ra.value
    dec = cf.dec.value
    
    pmra = cf.pm_ra_cosdec.value
    pmdec = cf.pm_dec.value

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.quiver(ra,dec,-pmra,pmdec,color='black')
    ax.set_xlabel('ra (deg)')
    ax.set_ylabel('dec (deg)')
    plt.gca().invert_xaxis()
    plt.show()
