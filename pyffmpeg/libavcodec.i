%module(threads="1", moduleimport="from . import $module") libavcodec_c

%{
#include "libavcodec/avcodec.h"
%}
%include <libavutil/samplefmt.h>
%include <libavutil/attributes.h>
%include <libavutil/avutil.h>
%include <libavutil/buffer.h>
%include <libavutil/cpu.h>
%include <libavutil/channel_layout.h>
%include <libavutil/dict.h>
%include <libavutil/frame.h>
%include <libavutil/log.h>
%include <libavutil/pixfmt.h>
%include <libavutil/rational.h>

%include <libavcodec/avcodec.h>
%include <libavutil/samplefmt.h>
%include <libavutil/attributes.h>
%include <libavutil/avutil.h>
%include <libavutil/buffer.h>
%include <libavutil/cpu.h>
%include <libavutil/channel_layout.h>
%include <libavutil/dict.h>
%include <libavutil/frame.h>
%include <libavutil/log.h>
%include <libavutil/pixfmt.h>
%include <libavutil/rational.h>

%include <libavcodec/avcodec.h>
