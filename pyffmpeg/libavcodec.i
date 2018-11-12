%module(moduleimport="from . import $module") libavcodec_c

%{
#include "libavcodec/avcodec.h"
#include "libavutil/frame.h"
%}

%include <stdint.i>
%include <typemaps.i>
// %include <attribute.i>
// %include "numpy.i"

// Deprecated functions, just don't include them. This is a modern wrapper.
%ignore refcounted_frames;
%ignore av_set_cpu_flags_mask;
%ignore av_parse_cpu_flags;
%ignore avcodec_encode_audio2;
%ignore avcodec_decode_audio4;
%ignore avcodec_encode_video2;
%ignore avcodec_decode_video2;
%ignore av_register_codec_parser;
%ignore av_parser_next;
%ignore avcodec_find_best_pix_fmt2;


%ignore AV_LOG_MAX_OFFSET;
%ignore av_vlog;
%ignore av_log_default_callback;
%ignore av_log_format_line;
%ignore av_log_format_line2;

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
