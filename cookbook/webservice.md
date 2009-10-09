---
layout: default
title: Webservice + WSDL
---

# Webservice + WSDL

Optio's  [soaplib](http://trac.optio.webfactional.com/) makes it really straightforward to write SOAP web service views by using a decorator to specify types. Plus it's the only Python library, as of today, which is able to generate WSDL documents for your web service. 



    import web 
    from soaplib.wsgi_soap import SimpleWSGISoapApp
    from soaplib.service import soapmethod
    from soaplib.serializers import primitive as soap_types

    urls = ("/hello", "HelloService",
            "/hello.wsdl", "HelloService",
            )
    render = web.template.Template("$def with (var)\n$:var")


    
    class SoapService(SimpleWSGISoapApp):
        """Class for webservice """

        #__tns__ = 'http://test.com'
    
        @soapmethod(soap_types.String,_returns=soap_types.String)
        def hello(self,message):
            """ Method for webservice"""
            return "Hello world "+message
     


    class HelloService(SoapService):
        """Class for web.py """
        def start_response(self,status, headers):
            web.ctx.status = status
            for header, value in headers:
                web.header(header, value)
    
    
        def GET(self):
            response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
            return render("\n".join(response))
    
    
        def POST(self):
            response = super(SimpleWSGISoapApp, self).__call__(web.ctx.environ, self.start_response)
            return render("\n".join(response))
     
    app=web.application(urls, globals())
    
    if __name__ == "__main__":
        app.run()




You can test it with a soaplib client: 

    >>> from soaplib.client import make_service_client
    >>> from test import HelloService
    >>> client = make_service_client('http://localhost:8080/hello', HelloService())
    >>> client.hello('John')
    'Hello world John'

And you can view the WSDL in [http://localhost:8080/hello.wsdl](http://localhost:8080/hello.wsdl)

For more information of webservice see: [soaplib](http://trac.optio.webfactional.com/),