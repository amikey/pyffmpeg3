%module(moduleimport="from . import $module") libavutil_c

%{
#include "libavutil/error.h"
#include "libavutil/opt.h"
%}

%include <stdint.i>
%include <typemaps.i>
// %include <attribute.i>
// %include "numpy.i"

%include "libavutil/error.h"
%include "libavutil/opt.h"
