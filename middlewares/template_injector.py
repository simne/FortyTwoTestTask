from django.conf import settings
import re

class TemplateInjector(object):
    
    def process_response(self, request, response):
        #return if admin
        if request.get_full_path().startswith('/admin'):
            return response
                
        functions = re.findall(r'{{{(.*?)}}}', response.content)
        
        #if no template vars return response
        if len(functions) == 0:
            return response
        
        #apply funciton to every match found
        for fn in functions:
            try:
                imported = __import__(settings.TEMPLATE_INJECTOR_INCLUDES + '.' + fn)                
                result = eval('imported.' + fn + '.' + fn + '()')
                response.content = re.sub(r'{{{%s}}}' % fn, result, response.content)
                result = imported = None
            except ImportError:
                response.content = re.sub(r'{{{%s}}}' % fn, '', response.content)
            
        return response

