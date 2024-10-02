import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    
    clear()
    
    put_html (
        '<p align="center">'
        '<h2><img src="https://img.freepik.com/free-vector/creative-did-you-know-think-concept-background-with-light-bulb_1017-53664.jpg?ga=GA1.2.2003631022.1724151815&semt=ais_hybrid" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    response = requests.get(url)
    
    data = json.loads(response.text)
    
    useless_fact = data['text']
    
    style(put_text(useless_fact), 'color:#3454D1; font-size: 30px')
    
    put_buttons(
        [dict(label ='Generate', value='outlinbe-success', color='outline-success')],
        onclick=get_fun_fact
    )


if __name__ == '__main__':
    
    put_html(
         '<p align="center">'
        '<h2><img src="https://img.freepik.com/free-vector/creative-did-you-know-think-concept-background-with-light-bulb_1017-53664.jpg?ga=GA1.2.2003631022.1724151815&semt=ais_hybrid" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    put_buttons(
         [dict(label='Generate', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    hold()







