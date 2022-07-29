

import os
import pandas as pd
import plotly.express as px
from params.burak_params import param_names
from params.burak_params import PIDRParser, GPAParser, MAGParser, ARSPParser, RCOUParser, BAROParser
from params.burak_params import IMUParser




with open("00000002.log", "r") as input:
    for line in input:
        if line.strip('\n').startswith('RCOU'):

            RCOUParser.update(line)

df = RCOUParser.get_data_frame()

fig = px.line(df)
fig.show()


