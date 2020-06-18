import numpy as np

def fitFunction(freq, r_w, l_para, l_lc, c_lc = 4.7e-12 , r_para=0.1e-9 , r_w2= 0.1e-9 , l_wafer = 10e-9):

    # l_para = 9.05913e-8
    # l_lc = 7.98457e-8
    # c_lc = 7.31807e-12
    #r_w = 0

    #r_para = 5.05
    omega = 2.*np.pi*freq
    Z = r_para+1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs((50.-1.j/(omega*1.8e-9))/(Z + 50.-1.j/(omega*1.8e-9))))

def fitFunctionTest(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs((50.-1.j/(omega*1.8e-9))/(Z + 50.-1.j/(omega*1.8e-9))))

# Backup
#Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
#20*np.log10(abs((50.))/(Z + 50.)))

# Theoretisch erwartbar
# Z = r_para + 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./( r_w + 1.j*omega*l_lc + ( gamma**2 * omega**2 * l_lc * l_wafer)/( 1.j*omega*l_wafer + r_wafer)))

# Idee
# Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_wafer + r_w + 1.j*omega*l_lc))

def fitFunctionPhase(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return np.angle((50.-1.j/(omega*1.8e-9))/(Z + 50.-1.j/(omega*1.8e-9)))/np.pi * 180

def fitFunctionPhase2(freq, r_w, l_para, l_lc, c_lc=4.7e-12, r_para=0.1e-9):
    omega = 2.*np.pi*freq
    Z = r_para +1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return np.angle((50.)/(Z + 50.),deg= True)+5*(omega/500e6)