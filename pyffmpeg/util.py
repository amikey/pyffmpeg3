import platform

def LoadLibrary(libname):
    if platform.system() == 'Linux':
        from ctypes import cdll
        return cdll.LoadLibrary("lib" + libname + ".so")
    elif platform.system() == 'Darwin':
        from ctypes import cdll
        return cdll.LoadLibrary("lib" + libname + ".dylib")
    else:
        from ctypes import windll
        return windll.LoadLibrary(str(libname + ".dll"))


def enum(start, names):
    return dict(zip(names, range(start, start+len(names))))
