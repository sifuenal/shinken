
### Will be populated by the UI with it's own value
app = None


# Main impacts view
#@route('/host')
#@view('hostdetail')
def show_host(name):
    return get_data(name)



def get_data(name):
    h = app.datamgr.rg.hosts.find_by_name('localhost')
    return {'host' : h}



pages = {show_host : { 'routes' : ['/host/:name'], 'view' : 'hostdetail', 'static' : True}}