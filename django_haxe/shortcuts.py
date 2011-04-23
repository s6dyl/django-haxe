#coding:utf-8
from .conf import HAXE_TEMPLATE_DIR, HAXE_CACHE_DIR
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import commands
import hashlib
import mimetypes
import os
import tempfile
import urlparse


def render_to_response(*args, **kwargs):
    response_filename = render_to_file(*args, **kwargs)
    response_text = open(response_filename, 'rb').read()
    mimetype = mimetypes.types_map['.swf']
    return HttpResponse(response_text, mimetype=mimetype)


def render_to_file(classname, dictonary, context_instance=None, with_cache=True, params=''):
    filename = '%s.hx' % classname
    cache_dir = HAXE_CACHE_DIR + '/'
    _make_dir(cache_dir)
    template_name = urlparse.urljoin(HAXE_TEMPLATE_DIR, filename)
    code_text = render_to_string(template_name, dictonary, context_instance)
    result = hashlib.md5('%s:%s' % (code_text, settings.SECRET_KEY)).hexdigest()
    result = '%s.swf' % result
    mv_result_to = urlparse.urljoin(cache_dir, result)
    if not os.path.isfile(mv_result_to) or not with_cache:
        dirname = tempfile.mkdtemp(dir=cache_dir) + '/'
        code_filename = urlparse.urljoin(dirname, filename)
        open(code_filename, 'w').write(code_text)
        cmd = 'cd %(dirname)s; haxe -main %(classname)s -swf9 %(result)s %(params)s' % locals()
        commands.getoutput(cmd)
        mv_result_from = urlparse.urljoin(dirname, result)
        os.rename(mv_result_from, mv_result_to)
        os.remove(code_filename)
        os.removedirs(dirname)
    return mv_result_to

def _make_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        pass