import sys,traceback
import time
from contextlib import contextmanager
def try_except(f,exctype=Exception,re_raise=False,log_traceback=False,tries=1,delay=0,back_off=0):
    def handle_problems(*args, **kwargs):
        try:
            i=0
            while i<tries:
               f(*args, **kwargs)
               i=i+1
               time.sleep(delay*60*back_off)
        except exctype:
              exc_type, exc_instance, exc_traceback = sys.exc_info()
              formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
              message = '\n{0}\n{1}:\n{2}'.format(
                formatted_traceback,
                exc_type.__name__,
                exc_instance
            )
              if log_traceback==True:
                 traceback.print_exception(exc_type, exc_value, exc_tb)
              if re_raise==True:
                 raise 
              print(exc_type(message))
        finally:
            pass
    return handle_problems
@contextmanager
def handle_error_context(func,re_raise=True,exctype=ValueError,log_traceback=True):
    try:
        yield func
    except exctype as e:
        print('caught:', e)
        if log_traceback==True:
            exc_type, exc_value, exc_tb = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_tb)
        if re_raise==True:
             raise
    else:
        print('no exception was thrown')
    finally:
        pass
