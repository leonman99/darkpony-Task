from fastapi import FastAPI 

app=FastAPI()

# @app.get('/')
# def index():
#     return {'data':{'name':'Leo'}}

@app.get('/content')
def index():
    return {'data':{'name':'Leo'}}

@app.get('/content/{id}')
def index():
    return {'data':{'name':'Leo'}}

@app.get('/content/section/{abbr}')
def index(abbr: str):

    # return data from Header Section
    if (abbr=="hdr"):
        return {'data':{'logo'}}
    # return data from Body Section
    elif (abbr=="bd"):
        return {'data':{
            'Carousel Pictures':{'Picture1','Picture2','Picture3'},
            'About Us Text',
            'Article List':{'Article1','Article2','Article3','Article4'},
            'Videos':{'video1','video2'}
        }}
    # return data from Footer Section
    elif (abbr=="ftr")
        return {'data':{
            'Contact Information':{
                'name':{'Leonidas Achilleos'},
                'email':{'lacman05@gmail.com'},
                'phone':{'96196460'},
                'working':{'8:00 - 16:00, monday to friday'}
            },
            'Quote List':{
                'Get busy living or get busy dying.',
                'If you think lifting is dangerous, try being weak. Being weak is dangerous.',
                'Beware of little expenses; a small leak will sink a great ship.',
                'Dogs’ lives are too short. Their only fault, really.',
                'Testing leads to failure, and failure leads to understanding.'
            }
        }}

@app.get('/quotes')
def index():
    return {'data':{'Get busy living or get busy dying.',
    'If you think lifting is dangerous, try being weak. Being weak is dangerous.',
    'Beware of little expenses; a small leak will sink a great ship.',
    'Dogs’ lives are too short. Their only fault, really.',
    'Testing leads to failure, and failure leads to understanding.'}}

@app.get('/videos')
def index():
    return {'data':{'Video1','Video2'}}

@app.get('/images')
def about ():
    return {'data':{'all images'}}

@app.get('/images/carousel')
def about ():
    return {'data':{'all carousel images'}}

@app.get('/contact')
def about ():
        return {'data':{'name':{'Leonidas Achilleos'},
        'email':{'lacman05@gmail.com'},
        'phone':{'96196460'},
        'working':{'8:00 - 16:00, monday to friday'}
        }}

@app.get('/contact/{field}')
def about (field: str):
    if (field=="name"):
        return {'data':{'Leonidas Achilleos'}}
    elif (field=="email"):
        return {'data':{'lacman05@gmail.com'}}
    elif (field=="mobile"):
        return {'data':{'96196460'}}
    elif (field=="working"):
        return {'data':{'8:00 - 16:00, monday to friday'}}