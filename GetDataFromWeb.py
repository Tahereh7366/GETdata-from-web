#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import io
import requests as rq


# In[25]:


##url = "https://www.fipiran.com/Market/LupBourse"
url = "http://www.tsetmc.com/Loader.aspx?ParTree=15"
fopen = rq.get(url).content


# In[26]:


html = pd.read_html(io.StringIO(fopen.decode("utf-8")), header=0, index_col=0)
html


# In[27]:


type(html)


# In[28]:


html=pd.DataFrame(html[1])


# In[29]:


html


# In[30]:


html[:1]


# In[ ]:




