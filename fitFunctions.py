import numpy as np

def fitFunction(freq, r_w, l_para, l_lc, c_lc = 4.7e-12 , r_para = 1):
    #c_lc = 7.35e-12
    r_para = 5.05
    omega = 2.*np.pi*freq
    Z = r_para + 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs((50.)/(Z + 50.)))

def fitFunctionTest(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return 20*np.log10(abs((50.-1.j/(omega*1.8e-9))/(Z + 50.-1.j/(omega*1.8e-9))))

def fitFunctionPhase(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return np.angle((50.-1.j/(omega*1.8e-9))/(Z + 50.-1.j/(omega*1.8e-9)))/np.pi * 180

def fitFunctionPhase2(freq, r_w, l_para, l_lc, c_lc=4.7e-12):
    omega = 2.*np.pi*freq
    Z = 1.j*omega*l_para + 1./(1.j*omega*c_lc + 1./((omega/(500*10**6))**2*r_w + 1.j*omega*l_lc))
    return np.angle((50.)/(Z + 50.))/np.pi * 180